# -*- coding: utf-8 -*-

from typing import Any, TypedDict, Optional

import pandas as pd
pd.options.mode.copy_on_write = True
import json
import requests
import time
import copy
import os
import re

from . import constants
from . import utils_data_dict
from . import utils_types

_TOKEN = ''
_HOST = ''


class REDCapEvent(TypedDict, total=False):
    event_name: str
    arm_num: int
    day_offset: int
    offset_min: int
    offset_max: int
    unique_event_name: str
    custom_event_label: str


class REDCapFormEvent(TypedDict, total=False):
    arm_num: int
    unique_event_name: str
    form: str


class REDCapRepeatedFormEvent(TypedDict, total=False):
    event_name: str
    form_name: str
    custom_form_label: str


class REDCapColumn(TypedDict, total=False):
    field_name: str
    form_name: str
    section_header: str
    field_type: str
    field_label: str
    select_choices_or_calculations: str
    field_note: str
    text_validation_type_or_show_slider_number: str
    text_validation_min: str
    text_validation_max: str
    identifier: str
    branching_logic: str
    required_field: str
    custom_alignment: str
    question_number: str
    matrix_group_name: str
    matrix_ranking: str
    field_annotation: str

    form_category: str
    form_repeated: bool


type REDCapColumnMap = dict[str, REDCapColumn]


class REDCapFilenameInfo(constants.FilenameInfo):
    '''
    REDCapFilenameInfo
    '''

    map: REDCapColumnMap
    '''
    column map
    '''

    id: str
    '''
    id
    '''


type REDCapSheetColumnMap = dict[str, REDCapColumnMap]


def init_redcap(token: str, host: str):
    '''
    Initalize REDCap
    '''
    global _TOKEN
    global _HOST

    _TOKEN = token
    _HOST = host


#####
# REDCap Column Map
#####
def build_redcap_column_map(excel_filename: str, sheet_name: str) -> REDCapColumnMap:
    '''
    Construct REDCap payload
    '''
    excel = pd.ExcelFile(excel_filename)
    df_valid = utils_data_dict.load_data_dict(excel_filename, sheet_name)

    ret = {}
    for idx, each in df_valid.iterrows():
        the_var = each[constants.DATA_DICT_VAR_NAME]
        the_type = each[constants.DATA_DICT_VAR_TYPE]

        ret[the_var] = _build_redcap_column(the_type, each, excel)

    info_MRI_ID = {
        constants.DATA_DICT_CATEGORY: constants.CATEGORY_POST_INTERVENTION,
        constants.DATA_DICT_SUBCATEGORY: constants.SUBCATEGORY_MRI,
        'redcap': 'mri_id',

    }
    ret['MRI_ID'] = _build_redcap_column('text', info_MRI_ID, None)
    info_uniqueFollowupID = {
        constants.DATA_DICT_CATEGORY: constants.CATEGORY_FOLLOW_UP,
        constants.DATA_DICT_SUBCATEGORY: constants.SUBCATEGORY_IDENTITY,
        'redcap': 'unique_followup_id',
    }
    ret['uniqueFollowupID'] = _build_redcap_column('text', info_uniqueFollowupID, None)
    info_center_orig = {
        constants.DATA_DICT_CATEGORY: constants.CATEGORY_FOLLOW_UP,
        constants.DATA_DICT_SUBCATEGORY: constants.SUBCATEGORY_FOLLOWUP,
        'redcap': 'center_orig',
    }
    ret['center_orig'] = _build_redcap_column('text', info_center_orig, None)

    return ret


def _build_redcap_column(the_type: str, data_dict_info: constants.DataDict, excel: pd.ExcelFile) -> REDCapColumn:
    redcap_type = ''
    choices = ''
    choices_dict = {}
    annotation = ''
    form_name = ''

    if the_type == constants.BASIC_TYPE_TEXT:
        redcap_type = 'text'
    elif the_type == constants.BASIC_TYPE_INT:
        redcap_type = 'text'
    elif the_type == constants.BASIC_TYPE_FLOAT:
        redcap_type = 'text'
    elif the_type == constants.BASIC_TYPE_CENTER:
        redcap_type = 'text'
    elif the_type == constants.BASIC_TYPE_BOOL:
        redcap_type = 'yesno'
    elif the_type == constants.BASIC_TYPE_DATE:
        redcap_type = 'text'
    elif the_type == constants.BASIC_TYPE_TIME:
        redcap_type = 'text'
    elif the_type in excel.sheet_names:
        choices_dict, choices = _build_redcap_value_map_choices(excel, the_type)
        if len(choices_dict) == 0:
            redcap_type = 'text'
        else:
            redcap_type = 'radio' if len(choices_dict) < 30 else 'dropdown'
        annotation = the_type
    else:
        print(f'[WARN] _build_redcap_map: unable to parse type: {the_type}')

    category = data_dict_info['Category']
    subcategory = data_dict_info['Subcategory']
    form_name = redcap_form_name(category, subcategory)

    return {
        'field_name': data_dict_info['redcap'],
        'form_name': form_name,
        'form_category': category,
        'form_repeated': False,
        'section_header': '',
        'field_type': redcap_type,
        'field_label': data_dict_info['redcap'],
        'choices_dict': choices_dict,
        'select_choices_or_calculations': choices,
        'field_note': annotation,
        'text_validation_type_or_show_slider_number': '',
        'text_validation_min': '',
        'text_validation_max': '',
        'identifier': '',
        'branching_logic': '',
        'required_field': '',
        'custom_alignment': '',
        'question_number': '',
        'matrix_group_name': '',
        'matrix_ranking': '',
        'field_annotation': '',
    }


def _build_redcap_value_map_choices(excel: pd.ExcelFile, the_type: str) -> tuple[dict[str, int], str]:
    df = pd.read_excel(excel, the_type)
    is_valid = df['name'].isnull() == False
    df_valid = df[is_valid]

    df_name_dedup = df_valid['name'].drop_duplicates()

    valid_names = list(df_name_dedup)
    ret_dict = {each: idx + 1 for idx, each in enumerate(valid_names)}
    ret_list = [f'{idx + 1}, {each}' for idx, each in enumerate(valid_names)]

    return ret_dict, ' | '.join(ret_list)


def default_redcap_column(column: str) -> REDCapColumn:
    return {
        'field_name': column,
        'form_name': '',
        'section_header': '',
        'field_type': 'text',
        'field_label': column,
        'select_choices_or_calculations': '',
        'field_note': '',
        'text_validation_type_or_show_slider_number': '',
        'text_validation_min': '',
        'text_validation_max': '',
        'identifier': '',
        'branching_logic': '',
        'required_field': '',
        'custom_alignment': '',
        'question_number': '',
        'matrix_group_name': '',
        'matrix_ranking': '',
        'field_annotation': '',
    }


#####
# REDCap Filename Info
#####
def build_redcap_filename_infos(redcap_sheet_column_map: REDCapSheetColumnMap) -> list[REDCapFilenameInfo]:
    '''
    build_redcap_filename_infos
    '''
    return [_build_redcap_filename_info(each, redcap_sheet_column_map) for each in constants.FILENAME_INFOS if each.get('is_merge', True)]


def _build_redcap_filename_info(filename_info: constants.FilenameInfo, redcap_sheet_column_map: REDCapSheetColumnMap) -> REDCapFilenameInfo:
    ret: REDCapFilenameInfo = copy.deepcopy(filename_info)

    category = filename_info['category']
    sheet_name = constants.CATEGORY_SHEET_MAP[category]
    ret['map'] = redcap_sheet_column_map[sheet_name]

    filename = filename_info['name']
    filename_list = filename.split('-')

    # id
    the_id = '_'.join(filename_list[:2])
    ret['id'] = the_id

    return ret


#####
# Construct REDCap columns from REDCap Filename Info
#####
def redcap_columns(input_dir: str, filename_info: REDCapFilenameInfo) -> list[REDCapColumn]:
    filename = filename_info['name']
    filename_id = filename_info['id']
    column_map = filename_info['map']

    full_filename = os.sep.join([input_dir, filename])
    df = pd.read_csv(full_filename, dtype='O')
    is_repeated = constants.FLATTEN_INDEX in df.columns

    valid_columns = [column for column in df.columns if column not in constants.REDCAP_EXCLUDE_FILEINFO_COLUMNS and column not in filename_info.get(
        'exclude_columns', [])]
    df = df[valid_columns]

    ret = [copy.deepcopy(_get_redcap_column_map(each, column_map))
           for each in df.columns if not each.endswith('.orig')]

    category = filename_info['category']
    subcategory = filename_info['subcategory']
    form_name = redcap_form_name(category, subcategory)

    # postprocess REDCap column
    is_summary = filename_info.get('summary', False)
    for each in ret:
        each['field_name'] += f'_{filename_id}'
        each['form_name'] = form_name
        each['form_category'] = category
        if is_repeated:
            each['form_repeated'] = True
        if is_summary:
            each['form_name'] += '_summary'
            each['form_repeated'] = False

        if 'choices_dict' in each:
            del each['choices_dict']

    return ret


def _get_redcap_column_map(column: str, column_map: dict[str, REDCapColumn]) -> REDCapColumn:
    if column not in column_map:
        print(f'[WARN] _get_redcap_column_map: {column} not in the_map')
        return default_redcap_column(column)

    if pd.isnull(column_map[column]['field_name']):
        print(
            f"[ERROR] _get_redcap_column_map: invalid field_name: column: {column} map: {column_map[column]['field_name']}")

    return column_map[column]


def redcap_form_name(category: str, subcategory: str) -> str:
    # XXX hack for identifier
    if category == constants.CATEGORY_PRE_INTERVENTION and subcategory == constants.SUBCATEGORY_IDENTITY:
        return constants.REDCAP_ID_FORM

    category_abbrev = constants.CATEGORY_ABBREVIATE_MAP[category]
    subcategory_abbrev = constants.SUBCATEGORY_ABBREVIATE_MAP[subcategory]
    form_name_list = [subcategory_abbrev]
    if category_abbrev:
        form_name_list = [category_abbrev, subcategory_abbrev]
    form_name = '_'.join(form_name_list)

    return re.sub(r' ', '_', form_name).lower()


def all_redcap_columns(input_dir: str, filename_infos: list[REDCapFilenameInfo]) -> pd.DataFrame:
    # id form
    id_redcap_columns = [default_redcap_column(each) for each in constants.REDCAP_ID_COLUMNS]
    for each in id_redcap_columns:
        each['form_name'] = constants.REDCAP_ID_FORM
        each['form_category'] = constants.CATEGORY_PRE_INTERVENTION
        each['form_repeated'] = False

    all_redcap_columns = id_redcap_columns

    # form from filename_infos
    for filename_info in filename_infos:
        each_redcap_columns = redcap_columns(input_dir, filename_info)
        all_redcap_columns += each_redcap_columns

    df_all_redcap_columns = pd.DataFrame(all_redcap_columns)
    df_all_redcap_columns = df_all_redcap_columns.fillna('')

    return df_all_redcap_columns


#####
# REDCap event
#####
def redcap_event(event_name: str, event_label: str, arm_num: int = 1) -> REDCapEvent:
    unique_event_name = redcap_unique_event_name(event_name, arm_num)
    return {
        'event_name': event_name,
        'arm_num': arm_num,
        'day_offset': 0,
        'offset_min': 0,
        'offset_max': 0,
        'unique_event_name': unique_event_name,
        'custom_event_label': event_label,
    }


def redcap_unique_event_name(event_name: str, arm_num: int = 1) -> str:
    return f"{re.sub(r' ', '_', re.sub(r'-', '', event_name))}_arm_{arm_num}".lower()


def redcap_form_event(form_name: str, form_category: str, arm_num: int = 1) -> REDCapFormEvent:
    event_name = constants.CATEGORY_EVENT_MAP[form_category]
    unique_event_name = redcap_unique_event_name(event_name, arm_num)

    return {
        "arm_num": arm_num,
        "unique_event_name": unique_event_name,
        "form": form_name,
    }


def redcap_repeated_form_event(form_name: str, form_category: str, arm_num: int = 1) -> REDCapRepeatedFormEvent:
    event_name = constants.CATEGORY_EVENT_MAP[form_category]
    unique_event_name = redcap_unique_event_name(event_name, arm_num)

    return {
        'event_name': unique_event_name,
        'form_name': form_name,
        'custom_form_label': '',
    }


#####
# Normalize Filename Info
#####
def redcap_normalize_filename_info(filename_info: REDCapFilenameInfo, input_dir: str, valid_columns: Optional[list] = None, column_name_map: Optional[dict] = None, is_complete=True, flatten_sep=1000, exclude_columns: Optional[list[str]] = None) -> pd.DataFrame:
    '''
    redcap_normalize_filename_info
    '''
    if column_name_map is None:
        column_name_map = {}
    if exclude_columns is None:
        exclude_columns = constants.REDCAP_EXCLUDE_FILEINFO_COLUMNS

    filename = filename_info['name']
    column_info_map = filename_info['map']
    filename_id = filename_info['id']

    # 1. read file
    full_filename = os.sep.join([input_dir, filename])
    df = pd.read_csv(full_filename, dtype='O')
    df = df.fillna('')
    if valid_columns is not None:
        df = df[valid_columns]

    valid_columns = list(filter(lambda x: not x.endswith('.orig'), df.columns))
    if 'exclude_columns' in filename_info:
        valid_columns = list(
            filter(lambda x: not x in filename_info['exclude_columns'], valid_columns))
    df = df[valid_columns]

    # 2. redcap-normalize
    for column in df.columns:
        df.loc[:, column] = df[column].apply(lambda x: redcap_normalize(x, column, column_info_map))

    # 3. postprocess after normalize
    df['study_unique_id'] = df.apply(lambda x: f"{x['_study']}:{x['uniqueID']}", axis=1)

    # 4. rename
    all_column_name_map = {column: f"{column_info['field_name']}_{filename_id}" for column,
                           column_info in column_info_map.items() if column not in exclude_columns}
    all_column_name_map.update(column_name_map)

    df_rename = df.rename(columns=all_column_name_map)

    # 5. event name
    category = filename_info['category']
    subcategory = filename_info['subcategory']
    form_name = redcap_form_name(category, subcategory)
    event_name = constants.CATEGORY_EVENT_MAP[category]
    unique_event_name = redcap_unique_event_name(event_name)
    df_rename['redcap_event_name'] = unique_event_name

    # 6. complete
    is_summary = filename_info.get('summary', False)
    if is_complete:
        full_form_name = form_name if not is_summary else f'{form_name}_summary'
        df_rename[f'{full_form_name}_complete'] = '2'

    # 7. redcap_repeat_instance
    if '_flatten_index' in df_rename:
        df_rename['redcap_repeat_instrument'] = form_name

        df_rename['redcap_repeat_instance'] = df_rename['_flatten_index'].apply(
            lambda x: _flatten_to_repeat_instance(x, flatten_sep))

    else:
        df_rename['redcap_repeat_instrument'] = ''

        df_rename['redcap_repeat_instance'] = ''

    # 8. exclude columns
    valid_columns = list(filter(lambda x: x not in exclude_columns, df_rename.columns))
    df_rename = df_rename[valid_columns]

    return df_rename


def _flatten_to_repeat_instance(flatten: str, flatten_sep: int) -> str:
    flatten_list = [int(each) for each in flatten.split('@')]
    df = pd.DataFrame({'flatten': flatten_list})
    df['index'] = df.index

    len_df = len(df)
    df['flatten_sep'] = df['index'].apply(lambda idx: flatten_sep ** (len_df - 1 - idx))
    df['idx'] = df['flatten'] * df['flatten_sep']

    repeat_instance = int(df['idx'].sum())
    # XXX hack repeat_instance == 0
    if repeat_instance == 0:
        repeat_instance = 1

    return str(repeat_instance)


def redcap_normalize(val: Any, column: str, column_map: REDCapColumnMap) -> str:
    if val == '':
        return ''

    if column not in column_map:
        if column not in ['_study', 'uniqueID', '_flatten_index']:
            print(f'[WARN] redcap_normalize: not in the_map: val: {val} column: {column}')
        return str(val)

    column_info = column_map[column]
    field_type = column_info['field_type']
    if field_type == 'text':
        return str(val)
    elif field_type == 'yesno':
        ret_bool = utils_types.to_bool(val)
        if ret_bool == 'FALSE':
            return '0'
        elif ret_bool == 'TRUE':
            return '1'
        else:
            return ''
    elif field_type == 'radio' or field_type == 'dropdown':
        choice_dict = column_info['choices_dict']

        if val not in choice_dict:
            print(
                f'[WARN] redcap_normalize: val not in choice_dict: val: {val} column: {column} type: {field_type}')
            return ''

        choice_val = choice_dict[val]
        return str(choice_val)

    print(f'[WARN] redcap_normalize: invalid type: val: {val} column: {column} type: {field_type}')
    return ''


#####
# REDCap Operations
#####
def import_redcap_data(content: str, data: Any) -> tuple[Exception, Any]:
    """put data to REDCap

    Args:
        content (str): content-type (record, metadata, ...)
        data (list): list of data

    Returns:
        err, dict: err, result
    """
    json_str = json.dumps(data)

    params = {
        'content': content,
        'action': 'import',
        'data': json_str,
        'token': _TOKEN,
        'format': 'json',
        'returnFormat': 'json',
    }

    try:
        r = requests.post(_HOST, data=params, verify=False)
        time.sleep(0.1)
    except Exception as e:
        print(f'[ERROR] (put_redcap_data) unable to post: e: {e}')
        return e, {}

    err = ''
    result = []

    try:
        result = r.json()
    except Exception as e:
        err = 'unable to r.json: r.content: %s' % (r.content)

    if r.status_code >= 400:
        if type(result) == dict and 'error' in result:
            err = result['error']
        return Exception(err), {}

    return None, result


def put_redcap_data(content: str, data: Any) -> tuple[Exception, Any]:
    """put data to REDCap

    Args:
        content (str): content-type (record, metadata, ...)
        data (list): list of data

    Returns:
        err, dict: err, result
    """
    json_str = json.dumps(data)

    params = {
        'content': content,
        'type': 'flat',
        'data': json_str,
        'token': _TOKEN,
        'format': 'json',
        'returnFormat': 'json',
    }

    try:
        r = requests.post(_HOST, data=params, verify=False)
        time.sleep(0.1)
    except Exception as e:
        print(f'[ERROR] (put_redcap_data) unable to post: e: {e}')
        return e, {}

    err = ''
    result = []

    try:
        result = r.json()
    except Exception as e:
        err = 'unable to r.json: r.content: %s' % (r.content)

    if r.status_code >= 400:
        if type(result) == dict and 'error' in result:
            err = result['error']
        return Exception(err), {}

    return None, result


def delete_redcap_data(the_ids: list[str], content='record') -> tuple[Exception, Any]:
    """delete data from REDCap

    Args:
        content (str): content-type (record, metadata, ...)
        data (list): list of data

    Returns:
        err, dict: err, result
    """

    params = {
        'content': content,
        'action': 'delete',
        'returnFormat': 'json',
        'token': _TOKEN,
    }

    for idx, each in enumerate(the_ids):
        params.update({f'{content}s[{idx}]': each})

    try:
        r = requests.post(_HOST, data=params, verify=False)
        time.sleep(1)
    except Exception as e:
        return e, {}

    err = ''
    result = []

    try:
        result = r.json()
    except Exception as e:
        err = 'unable to r.json: r.content: %s' % (r.content)

    if r.status_code >= 400:
        if type(result) == dict and 'error' in result:
            err = result['error']
        return Exception(err), {}

    return None, result


def get_redcap_data(params: dict, is_raw_data=True, is_raw_header=True) -> tuple[Exception, Any]:
    """get data from REDCap

    Args:
        params (dict): query.

    Returns:
        err, list: err, list of the results
    """

    raw_or_label_data = 'raw' if is_raw_data else 'label'
    raw_or_label_header = 'raw' if is_raw_header else 'label'

    params.update({
        'action': 'export',
        'token': _TOKEN,
        'format': 'json',
        'returnFormat': 'json',
        'rawOrLabel': raw_or_label_data,
        'rawOrLabelHeaders': raw_or_label_header,
    })

    to_remove_keys = []
    to_update = {}
    for key, val in params.items():
        if type(val) == list and len(val):
            for idx, each_val in enumerate(val):
                to_update['%s[%s]' % (key, idx)] = each_val
            to_remove_keys.append(key)

    for key in to_remove_keys:
        del params[key]

    params.update(to_update)

    try:
        r = requests.post(_HOST, data=params, verify=False)
        time.sleep(0.1)
    except Exception as e:
        return e, []

    err = ''
    result = []
    try:
        result = r.json()
    except Exception as e:
        err = 'unable to r.json: r.content: %s' % (r.content)

    if r.status_code >= 400:
        if type(result) == dict and 'error' in result:
            err = result['error']
        return Exception(err), []

    return None, result
