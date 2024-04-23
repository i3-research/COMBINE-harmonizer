# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import itertools
import copy

from . import constants
from . import utils_types
from . import utils_mapping
from . import utils_flatten_index
from . import utils_data_dict


_RESERVED_COLUMNS = ['_study', 'center', 'subjectID', 'uniqueID', 'MRI_ID', 'followupCenter', 'followupID', 'uniqueFollowupID', '_flatten_index']


def build_value_map(excel_filename: str, sheet_name: str):
    df = utils_data_dict.load_data_dict(excel_filename, sheet_name)

    ret = {}
    for idx, each in df.iterrows():
        the_var = each[constants.DATA_DICT_VAR_NAME]
        the_type = each['type']

        print(f'build_value_map: ({idx}/{len(df)}) variable: {the_var} type: {the_type}')
        ret[the_var] = _build_value_map(the_type)

    return ret


def _build_value_map(the_type):
    if the_type == 'bool':
        return utils_types.to_bool
    elif the_type == 'int':
        return utils_types.to_int
    elif the_type == 'float':
        return utils_types.to_float
    elif the_type == 'text':
        return utils_types.to_str
    elif the_type == 'center':
        return utils_types.to_center
    elif the_type == 'date':
        return utils_types.to_str
    elif the_type == 'time':
        return utils_types.to_str
    elif the_type in utils_mapping._MAPPING:
        return lambda x: utils_mapping.get_mapping_value(the_type, x)
    else:
        print(f'[WARN] _build_value_map: unable to build value map: type: {the_type}')
        return None


#####
# build-inv-value-map
#####
def build_inv_value_map(filename: str, sheet_name: str):
    df = utils_data_dict.load_data_dict(filename, sheet_name)
    is_valid_dict = df[constants.DATA_DICT_VAR_NAME].isnull() == False
    is_valid_type = df[constants.DATA_DICT_VAR_TYPE].isnull() == False
    is_valid = is_valid_dict & is_valid_type
    df_valid = df[is_valid].reset_index(drop=True)

    ret = {}
    for idx, each in df_valid.iterrows():
        the_var = each[constants.DATA_DICT_VAR_NAME]
        the_type = each[constants.DATA_DICT_VAR_TYPE]

        print(f'build_inv_value_map: ({idx}/{len(df_valid)}) variable: {the_var} type: {the_type}')
        ret[the_var] = _build_inv_value_map(the_type)

    return ret


def _build_inv_value_map(the_type):
    if the_type == 'bool':
        return utils_types.to_inv_bool
    elif the_type == 'int':
        return utils_types.to_inv_int
    elif the_type == 'float':
        return utils_types.to_inv_float
    elif the_type in utils_mapping._INV_MAPPING:
        return lambda x: utils_mapping.get_inv_mapping_value(the_type, x)
    else:
        print(f'[INFO] _build_inv_value_map: to inv-text: type: {the_type}')
        return utils_types.to_inv_text


#####
# normalize-value
#####
def normalize_value(df: pd.DataFrame, value_map, flatten_ids: list[str] = None, subject_id_idx: str = 'subjectID', center_id_idx: str = 'center', unique_id_map=None, order_map=None) -> pd.DataFrame:
    len_columns = len(df.columns)
    new_columns = []
    for idx, column in enumerate(df.columns):
        print(f'({idx}/{len_columns}) normalize_value: column: {column}')
        df[f'{column}.orig'] = df[column].copy()
        if column in value_map:
            df[column] = df[f'{column}.orig'].apply(lambda x: value_map[column](x))

    if flatten_ids is not None:
        utils_flatten_index.flatten_index(df, flatten_ids, subject_id_idx=subject_id_idx, center_id_idx=center_id_idx, unique_id_map=unique_id_map)

    if order_map is not None:
        df = reorder_columns(df, order_map)

    return df


#####
#
#####
def build_order_map(excel_filename: str, sheet_name: str) -> dict:
    df = utils_data_dict.load_data_dict(excel_filename, sheet_name)
    is_valid_dict = df[constants.DATA_DICT_VAR_NAME].isnull() == False
    is_valid_type = df['type'].isnull() == False
    is_valid = is_valid_dict & is_valid_type
    df_valid = df[is_valid]

    order_map_reserved = {each: idx for idx, each in enumerate(_RESERVED_COLUMNS)}
    order_map_other = {row[constants.DATA_DICT_VAR_NAME]: idx + len(_RESERVED_COLUMNS) for idx, row in df_valid.iterrows() if row[constants.DATA_DICT_VAR_NAME] not in _RESERVED_COLUMNS}
    order_map = copy.deepcopy(order_map_reserved)
    order_map.update(order_map_other)

    if sheet_name == constants.SHEET_MAIN:
        # XXX hack for duplicated columns
        order_map['MRIDate'] = 581
        order_map['MRITime'] = 582

        order_map['birthDate'] = 132

    return order_map


#####
# reorder columns
#####
def reorder_columns(df: pd.DataFrame, order_map: dict) -> pd.DataFrame:
    '''
    reorder_columns
    '''
    columns_without_orig = list(filter(lambda x: not x.endswith('.orig'), df.columns))
    columns_with_orig = list(filter(lambda x: x.endswith('.orig'), df.columns))

    columns_without_orig.sort(key=lambda x: _get_order(x, order_map))
    columns_with_orig.sort(key=lambda x: _get_order(x[:-5], order_map))

    reserved_columns = list(filter(lambda x: x in columns_without_orig, _RESERVED_COLUMNS))
    other_columns = list(filter(lambda x: x not in _RESERVED_COLUMNS, columns_without_orig))

    columns = reserved_columns + other_columns
    columns_and_origs = list(itertools.chain.from_iterable([_column_and_orig(each, columns_with_orig) for each in columns]))

    return df[columns_and_origs]


def _get_order(x, order_map):
    if x not in order_map:
        print(f'[WARN] not in order_map: {x}')
        return constants.MAX_INT

    return order_map[x]


def _column_and_orig(column, columns_with_orig):
    ret = [column]
    if column + '.orig' in columns_with_orig:
        ret += [column + '.orig']

    return ret


#####
# cc to cc per kg
#####
def cc_to_cc_per_kg(df, df_main, columns, birth_weight_g_column) -> pd.DataFrame:
    main_columns = ['center', 'subjectID', birth_weight_g_column]
    df_main_with_columns = df_main[main_columns]

    df_merge = df.merge(df_main_with_columns, on=['center', 'subjectID'], how='left')

    for column in columns:
        is_valid = (df_merge[birth_weight_g_column].isnull() == False) & (df_merge[column].isnull() == False)
        df_merge.loc[is_valid, column] = df_merge[is_valid].apply(lambda x: '%.1f' % (float(x[column]) * 1000 / float(x[birth_weight_g_column])), axis=1)
        df_merge.loc[is_valid == False, column] = np.nan

    del df_merge[birth_weight_g_column]

    return df_merge


def inv_values(df: pd.DataFrame, inv_value_map: dict) -> pd.DataFrame:
    df_ret = df.copy()
    for idx, column in enumerate(df_ret.columns):
        column_list = column.split(':')
        var_name_idx = 1 if len(column_list) >= 2 else 0
        var_name = column_list[var_name_idx]

        if var_name not in inv_value_map:
            print(f'[WARN] ({idx}/{len(df_ret.columns)}) not in _INV_VALUE_MAP: {var_name}')
            continue

        print(f'[INFO] ({idx}/{len(df_ret.columns)}) to inv: column: {column} var_name: {var_name}')
        df_ret[column] = df_ret[column].apply(inv_value_map[var_name])

    return df_ret
