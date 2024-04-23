# -*- coding: utf-8 -*-

from typing import Optional, Any
import pandas as pd
import numpy as np
import scipy
from scipy import stats
from tqdm import tqdm
import re
import statsmodels.api as sm

_MAPPING = {
}

_INV_MAPPING = {
}


_MAPPING_EXCLUDE_SHEET_NAMES = [
    'Sheet1',
    'follow-up',
    'AnalysisOutcome',
    'naming convention',
]


def init_mapping(filename: str, column: str, column_postfix: str = ''):
    global _MAPPING

    excel = pd.ExcelFile(filename)
    sheet_names = list(excel.sheet_names)
    valid_sheet_names = list(filter(lambda x: x not in _MAPPING_EXCLUDE_SHEET_NAMES, sheet_names))
    postfix_column = column if not column_postfix else f'{column}-{column_postfix}'
    
    for idx, sheet_name in enumerate(valid_sheet_names):
        _MAPPING[sheet_name] = {}
        df = pd.read_excel(excel, sheet_name, dtype='O')
        
        # check the whether to use followup column.
        each_column = postfix_column if postfix_column in df.columns else column

        print(f'({idx}/{len(valid_sheet_names)}) init_mapping: sheet_name: {sheet_name} column: {column} each_column: {each_column}')
        
        for idx, row in df.iterrows():
            if pd.isnull(row[each_column]) or row[each_column] == '':
                continue
                
            name = row['name']
            value = row[each_column]
            _MAPPING[sheet_name][value] = name

            value_float = to_float(value)
            if isinstance(value_float, float):
                if value_float in _MAPPING[sheet_name] and _MAPPING[sheet_name][value_float] != name:
                    print(f'[WARN] possible conflicting setup: sheet_name: {sheet_name} value: {value} value_float: {value_float} name: {name} map: {_MAPPING[sheet_name][value_float]}')
                _MAPPING[sheet_name][value_float] = name
                
            value_int = to_int(value)
            if isinstance(value_int, int) and value_int == value_float:
                if value_int in _MAPPING[sheet_name] and _MAPPING[sheet_name][value_int] != name:
                    print(f'[WARN] possible conflicting setup: sheet_name: {sheet_name} value: {value} value_int: {value_int} name: {name} map: {_MAPPING[sheet_name][value_int]}')
                _MAPPING[sheet_name][value_int] = name


def get_mapping_value(sheet_name: str, value: str) -> Any:
    if pd.isnull(value):
        return ''

    if value == '' and '' not in _MAPPING[sheet_name]:
        return 
        
    value_int = to_int(value, is_suppress_warning=True)

    if value_int not in _MAPPING[sheet_name]:
        print(f'[WARN] unable to get value: sheet_name: {sheet_name} value: {value} value_int: {value_int}')
        return ''
    
    return _MAPPING[sheet_name][value_int]


def init_inv_mapping(filename: str):
    global _INV_MAPPING

    excel = pd.ExcelFile(filename)
    sheet_names = list(excel.sheet_names)
    valid_sheet_names = list(filter(lambda x: x not in _MAPPING_EXCLUDE_SHEET_NAMES, sheet_names))
    column = '_inv'

    for idx, sheet_name in enumerate(valid_sheet_names):
        df = pd.read_excel(excel, sheet_name, dtype='O')

        if column not in df.columns:
            continue

        
        print(f'({idx}/{len(valid_sheet_names)}) init_mapping: sheet_name: {sheet_name}')

        df[column] = df[column].astype(float)
        
        _INV_MAPPING[sheet_name] = {}
        for idx, row in df.iterrows():
            if pd.isnull(row['name']) or row['name'] == '':
                continue
                
            name = row['name']
            value = row[column]
            
            _INV_MAPPING[sheet_name][name] = value


def get_inv_mapping_value(sheet_name: str, value: str) -> Any:
    if pd.isnull(value):
        return np.nan

    if value == '' and '' not in _INV_MAPPING[sheet_name]:
        return np.nan
        
    if value not in _INV_MAPPING[sheet_name]:
        print(f'[WARN] unable to get value: sheet_name: {sheet_name} value: {value}')
        return np.nan
    
    return _INV_MAPPING[sheet_name][value]


#####
# unique-id
#####
def unique_id(df: pd.DataFrame, subject_id_idx: str='subjectID', center_id_idx: str='center') -> pd.Series:

    return df.apply(lambda x: f'{x[center_id_idx]}:{x[subject_id_idx]}', axis=1)


#####
# postprocess
#####
def postprocess(df: pd.DataFrame, subject_id_idx: str='subjectID', center_id_idx: str='center', first_columns: Optional[list[str]]=None) -> pd.DataFrame:
    df[center_id_idx] = df[center_id_idx].apply(to_center)
    df['uniqueID'] = unique_id(df, subject_id_idx, center_id_idx)
    if first_columns is None:
        first_columns = [center_id_idx, subject_id_idx, 'uniqueID']
    post_columns = [column for column in df.columns if column not in first_columns]
    columns = first_columns + post_columns
    df = df[columns]

    return df


#####
# check empty
#####
def check_empty(df: pd.DataFrame):
    for idx, column in enumerate(df.columns):
        print(f"({idx}/{len(df.columns)}) column: {column} ({len(df) - df[column].isnull().sum()} / {df[column].isnull().sum()})")


#####
# valid columns
#####
def valid_columns(df: pd.DataFrame, columns: list[str], debug_df=False, debug_columns=True) -> pd.DataFrame:
    valid_columns = [column for column in df.columns if column in columns]

    if debug_df:
        for idx, column in enumerate(df.columns):
            if column not in valid_columns:
                print(f'({idx}/{len(df.columns)} {column} not in columns')

    if debug_columns:
        for idx, column in enumerate(columns):
            if column not in valid_columns:
                print(f'({idx}/{len(columns)} {column} not in df')

    
    return df[valid_columns]


#####
# column info
#####
def column_info(df: pd.DataFrame):
    for idx, column in enumerate(df.columns):
        invalid = df[column].isnull().sum()
        valid = len(df) - invalid
        print(f'({idx}/{len(df.columns)}) {column}: ({valid}/{invalid}) {list(df[column].unique())}')


#####
# to types
#####
def to_center(val):
    int_val = to_int(val)
    if not isinstance(int_val, int):
        return int_val
        
    return f'{int_val:02d}'


def to_bool(val: Optional[str | np.float64]) -> str:
    if val in ['N', 'n', '0', '0.0', 'False', 'false', 0, 0.0, False, 'No', 'FALSE', 'no']:
        return 'false'

    if val in ['Y', 'y', '1', '1.0', 'True', 'true', 1, 1.0, True, 'Yes', 'YES', '1 Yes', '1 YES', 'TRUE', 'yes']:
        return 'true'

    if val in ['U', 'u', 'un', 'DK', 'unknown']:
        return 'unknown'

    if val in ['-', '*', '~', '?', '', None]:
        return ''

    if pd.isnull(val):
        return ''

    print(f'[WARN] unable to bool: val: ({val}/{type(val)})')

    return ''


def to_int(val: Any, is_suppress_warning: bool=False) -> int:
    if pd.isnull(val):
        return ''

    if val in ['*', '-']:
        return ''
        
    try:
        ret = int(float(val))
        return ret
    except Exception as e:
        if not is_suppress_warning:
            print(f'[WARN] unable to int: val ({val}/{type(val)}) e: {e}')
        return val


def to_float(val: Any) -> float:
    if pd.isnull(val):
        return ''

    if val in ['*', '-']:
        return ''
        
    try:
        return float(val)
    except Exception as e:
        print(f'[WARN] unable to float: val ({val}/{type(val)}) e: {e}')
        return val


def to_str(val: Any) -> str:
    if pd.isnull(val):
        return ''

    if val in [False]:
        return 'false'

    if val in [True]:
        return 'true'

    return str(val)


def to_lower(val: Any) -> str:
    return to_str(val).lower()



#####
# to inv types
#####
def to_inv_bool(val) -> float:
    if pd.isnull(val):
        return np.nan
        
    if not isinstance(val, str):
        return float(val)

    if val in ['true']:
        return 1.0
    elif val in ['false']:
        return 0.0
    elif val in ['unknown']:
        return np.nan

    print(f'[WARN] to_inv_bool: invalid val: {val}')
    return 0.0


def to_inv_int(val) -> float:
    if pd.isnull(val):
        return float('nan')
        
    return float(val)


def to_inv_float(val) -> float:
    if pd.isnull(val):
        return float('nan')
        
    return float(val)


def to_inv_text(val) -> str:
    return val


#####
# build-redcap-map
#####
def _category_variable(category_variable):
    return re.sub(r' ', '_', category_variable).lower()


def build_redcap_map(excel_filename: str, sheet_name: str):
    excel = pd.ExcelFile(excel_filename)
    df = pd.read_excel(excel, sheet_name=sheet_name)
    is_valid_dict = df['Standardized_VariableNames_Dictionary'].isnull() == False
    is_valid_type = df['type'].isnull() == False
    is_valid = is_valid_dict & is_valid_type
    df_valid = df[is_valid].reset_index(drop=True)

    ret = {}
    for idx, each in df_valid.iterrows():
        the_var = each['Standardized_VariableNames_Dictionary']
        the_type = each['type']

        print(f'build_redcap_map: ({idx}/{len(df_valid)}) variable: {the_var} type: {the_type}')
        ret[the_var] = _build_redcap_map(the_type, each, excel)

    ret['MRI_ID'] = _build_redcap_map('text', {'redcap': 'mri_id'}, None)
    ret['subjectID_with_postfix'] = _build_redcap_map('text', {'redcap': 'subject_id_with_postfix'}, None)
    ret['subjectID_postfix'] = _build_redcap_map('text', {'redcap': 'subject_id_postfix'}, None)
    ret['uniqueFollowupID'] = _build_redcap_map('text', {'redcap': 'unique_followup_id'}, None)
    ret['center_orig'] = _build_redcap_map('text', {'redcap': 'center_orig'}, None)
    
    return ret


def _build_redcap_map(the_type, info, excel):
    redcap_type = ''
    choices = ''
    choices_dict = {}
    annotation = ''
    form_name = ''
    
    if the_type == 'text': 
        redcap_type = 'text'
    elif the_type == 'int': 
        redcap_type = 'text'
    elif the_type == 'float': 
        redcap_type = 'text'
    elif the_type == 'center': 
        redcap_type = 'text'
    elif the_type == 'bool': 
        redcap_type = 'yesno'
    elif the_type in excel.sheet_names:
        choices_dict, choices = _build_redcap_value_map_choices(excel, the_type)
        redcap_type = 'radio' if len(choices_dict) < 30 else 'dropdown'
        annotation = the_type
    else:
        print(f'_build_redcap_map: unable to parse type: {the_type}')


    if 'Category_Variables' in info and not pd.isnull(info['Category_Variables']):
        form_name = _category_variable(info['Category_Variables'])

    print(f"_build_redcap_map: field_name: {info['redcap']} field_type: {redcap_type} form_name: {form_name} choices: {choices}")
    return  {
        'field_name': info['redcap'],
        'form_name': form_name,
        'section_header': '',
        'field_type': redcap_type,
        'field_label': info['redcap'],
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


def _build_redcap_value_map_choices(excel, the_type):
    df = pd.read_excel(excel, the_type)
    is_valid = df['name'].isnull() == False
    df_valid = df[is_valid]

    valid_names = list(df_valid['name'])
    ret_dict = {each: idx + 1 for idx, each in enumerate(valid_names)}
    ret_list = [f'{val}, {key}' for key, val in ret_dict.items()]

    return ret_dict, ' | '.join(ret_list)


#####
# build category id map
#####
def build_category_id_map(excel_filename: str, sheet_name: str):
    excel = pd.ExcelFile(excel_filename)
    df = pd.read_excel(excel, sheet_name=sheet_name)
    
    is_valid = df['Category_Variables'].isnull() == False
    df_valid = df[is_valid]

    category_variables = list(df_valid['Category_Variables'].unique())
    category_id_map = {_category_variable(each): idx for idx, each in enumerate(category_variables)}
    return category_id_map


#####
# build-value-map
#####
def build_value_map(excel_filename: str, sheet_name: str):
    excel = pd.ExcelFile(excel_filename)
    df = pd.read_excel(excel, sheet_name=sheet_name)
    is_valid_dict = df['Standardized_VariableNames_Dictionary'].isnull() == False
    is_valid_type = df['type'].isnull() == False
    is_valid = is_valid_dict & is_valid_type
    df_valid = df[is_valid].reset_index(drop=True)

    ret = {}
    for idx, each in df_valid.iterrows():
        the_var = each['Standardized_VariableNames_Dictionary']
        the_type = each['type']

        print(f'build_value_map: ({idx}/{len(df_valid)}) variable: {the_var} type: {the_type}')
        ret[the_var] = _build_value_map(the_type)
    return ret


def _build_value_map(the_type):
    if the_type == 'bool':
        return to_bool
    elif the_type == 'int':
        return to_int
    elif the_type == 'float':
        return to_float
    elif the_type == 'text':
        return to_str
    elif the_type == 'center':
        return to_center
    elif the_type in _MAPPING:
        return lambda x: get_mapping_value(the_type, x)        
    else:
        print(f'[WARN] _build_value_map: unable to build value map: type: {the_type}')
        return None


#####
# build-inv-value-map
#####
def build_inv_value_map(df: pd.DataFrame):
    is_valid_dict = df['Standardized_VariableNames_Dictionary'].isnull() == False
    is_valid_type = df['type'].isnull() == False
    is_valid = is_valid_dict & is_valid_type
    df_valid = df[is_valid].reset_index(drop=True)

    ret = {}
    for idx, each in df_valid.iterrows():
        the_var = each['Standardized_VariableNames_Dictionary']
        the_type = each['type']

        print(f'build_inv_value_map: ({idx}/{len(df_valid)}) variable: {the_var} type: {the_type}')
        ret[the_var] = _build_inv_value_map(the_type)
        
    return ret


def _build_inv_value_map(the_type):
    if the_type == 'bool':
        return to_inv_bool
    elif the_type == 'int':
        return to_inv_int
    elif the_type == 'float':
        return to_inv_float
    elif the_type in _INV_MAPPING:
        return lambda x: get_inv_mapping_value(the_type, x)        
    else:
        print(f'[INFO] _build_inv_value_map: to inv-text: type: {the_type}')
        return to_inv_text


#####
# normalize-value
#####
def normalize_value(df, value_map, flatten_ids=None, subject_id_idx='subjectID', center_id_idx: str='center', unique_id_map=None):
    to_remove_columns = []

    len_columns = len(df.columns)
    for idx, column in enumerate(df.columns):
        print(f'({idx}/{len_columns}) normalize_value: column: {column}')
        df[f'{column}.orig'] = df[column].copy()
        if column in value_map:
            df[column] = df[f'{column}.orig'].apply(lambda x: value_map[column](x))
        else:
            to_remove_columns.append(column)

    if flatten_ids is not None:
        flatten_index(df, flatten_ids, subject_id_idx=subject_id_idx, center_id_idx=center_id_idx, unique_id_map=unique_id_map)

    '''
    for idx, column in enumerate(to_remove_columns):
        print(f'({idx}/{len(to_remove_columns)} to remove: {column}')
        del df[column]
        del df[f'{column}.orig']
    '''


#####
# flatten index
#####
def flatten_index(df: pd.DataFrame, flatten_ids: list[str], subject_id_idx: str='subjectID', center_id_idx: str='center', unique_id_map=None):
    df['_flatten_index_tmp'] = df.apply(lambda x: _flatten_index(x, flatten_ids), axis=1)
    if unique_id_map is None:
        unique_ids = list(df['_flatten_index_tmp'].unique())
        unique_ids.sort()
        unique_id_map = {each: each for each in unique_ids}

    df['_flatten_index'] = df['_flatten_index_tmp'].apply(lambda x: unique_id_map[x])
    del df['_flatten_index_tmp']

    print(f"flatten_index: flatten_ids: {flatten_ids} unique_id_map: {unique_id_map} the_type: {df['_flatten_index'].dtype}")

    _ensure_unique_flatten_index(df, subject_id_idx, center_id_idx)

    return df


def _flatten_index(the_series, flatten_ids):    
    the_list = [the_series[each] for each in flatten_ids]
    # the_list_str = ['' if pd.isnull(each) else str(each) for each in the_list]
    return the_list[0] if len(flatten_ids) == 1 else '@'.join([str(each) for each in the_list])


def _ensure_unique_flatten_index(df: pd.DataFrame, subject_id_idx: str='subjectID', center_id_idx: str='center'):
    sort_columns = [center_id_idx, subject_id_idx, 'uniqueID', '_flatten_index']
    df.sort_values(by=sort_columns, inplace=True)

    pre_unique_id = None
    pre_index = None
    count = 0
    for idx, row in df.iterrows():
        current_unique_id = row['uniqueID']
        current_idx = row['_flatten_index']
        if current_unique_id == pre_unique_id and current_idx == pre_index:
            count += 1
            print(f"[WARN] not unique: ({idx}/{len(df)}) unique_id: {current_unique_id} flatten_index: {current_idx}")
            # df.loc[idx, '_flatten_index'] += f'-{count:02d}'
        else:
            count = 0
        pre_unique_id = current_unique_id
        pre_index = current_idx


#####
# correlation-coefficient
#####
def corr(df, x_columns, y_columns):
    rets = []
    y_column0 = y_columns[0]
    for x_column in tqdm(x_columns):
        for y_column in y_columns:
            coeff, meta = _corr_coeff(df, x_column, y_column)
            
            ret = {
                'x': x_column,
                'y': y_column,
                'corr': coeff.statistic,
                'pvalue': coeff.pvalue,
                'valid': meta['valid'],
                'valid-x': meta['valid_x'],
                'valid-y': meta['valid_y'],
                'valid-percent': float(meta['valid_percent']),
            }
            rets.append(ret)
    
    df_ret = pd.DataFrame(rets)
    df_ret_pivot = pd.pivot_table(df_ret, index=['x'], columns=['y'], values=['corr', 'pvalue', 'valid', 'valid-percent', 'valid-x', 'valid-y'])
    df_ret_pivot = df_ret_pivot.sort_values(by=[('pvalue', y_column0)])
    return df_ret_pivot


def _corr_coeff(df: pd.DataFrame, x: str, y: str):
    is_valid_x = df[x].isnull() == False
    is_valid_y = df[y].isnull() == False
    is_valid = is_valid_x & is_valid_y
    df_valid = df[is_valid]
    valid_x = df_valid[x].astype(float)
    valid_y = df_valid[y].astype(float)

    ret = stats.pearsonr(valid_x, valid_y)
    return ret, {'valid': is_valid.sum(), 'valid_x': is_valid_x.sum(), 'valid_y': is_valid_y.sum(), 'df': len(df), 'valid_percent': float(is_valid.sum()) / float(len(df))}


#####
# linear regression
#####
def lr(df, x_columns, y_columns):
    rets = []
    y_column0 = y_columns[0]
    for x_column in tqdm(x_columns):
        for y_column in y_columns:
            ret_lr, meta = _lr(df, x_column, y_column)

            pvalue = ret_lr.pvalues[x_column]
            tvalue = ret_lr.tvalues[x_column]
            
            ret = {
                'x': x_column,
                'y': y_column,
                'ret': ret_lr,
                'pvalue': pvalue,
                'tvalue': tvalue,
                'valid': meta['valid'],
                'valid-x': meta['valid_x'],
                'valid-y': meta['valid_y'],
                'valid-percent': float(meta['valid_percent']),
            }
            rets.append(ret)
    
    df_ret = pd.DataFrame(rets)
    df_ret_pivot = pd.pivot_table(df_ret, index=['x'], columns=['y'], values=['tvalue', 'pvalue', 'valid', 'valid-percent', 'valid-x', 'valid-y'])
    df_ret_pivot = df_ret_pivot.sort_values(by=[('pvalue', y_column0)])
    return df_ret_pivot


def _lr(df: pd.DataFrame, x: str, y: str):
    is_valid_x = df[x].isnull() == False
    is_valid_y = df[y].isnull() == False
    is_valid = is_valid_x & is_valid_y
    df_valid = df[is_valid]
    valid_x = df_valid[x].astype(float)
    valid_y = df_valid[y].astype(float)

    X = sm.add_constant(valid_x)
    mod = sm.OLS(valid_y, X)
    res = mod.fit()
    print(f'_lr: x: {x} y: {y}')
    res.summary()

    return res, {'valid': is_valid.sum(), 'valid_x': is_valid_x.sum(), 'valid_y': is_valid_y.sum(), 'df': len(df), 'valid_percent': float(is_valid.sum()) / float(len(df))}


#####
# logistic regression
#####
def logit(df, x_columns, y_columns):
    rets = []
    y_column0 = y_columns[0]
    for x_column in tqdm(x_columns):
        for y_column in y_columns:
            ret_logit, meta = _logit(df, x_column, y_column)

            pvalue = ret_logit.pvalues[x_column]
            tvalue = ret_logit.tvalues[x_column]
            b0 = ret_logit.params['const']
            b1 = ret_logit.params[x_column]            
            
            ret = {
                'x': x_column,
                'y': y_column,
                'ret': ret_logit,
                'pvalue': pvalue,
                'tvalue': tvalue,
                'b0': b0,
                'b1': b1,
                'OR': np.exp(b1),  # https://stats.oarc.ucla.edu/stata/faq/how-do-i-interpret-odds-ratios-in-logistic-regression/
                'valid': meta['valid'],
                'valid-x': meta['valid_x'],
                'valid-y': meta['valid_y'],
                'valid-percent': float(meta['valid_percent']),
            }
            rets.append(ret)
    
    df_ret = pd.DataFrame(rets)
    df_ret_pivot = pd.pivot_table(df_ret, index=['x'], columns=['y'], values=['tvalue', 'pvalue', 'valid', 'valid-percent', 'valid-x', 'valid-y'])
    df_ret_pivot = df_ret_pivot.sort_values(by=[('pvalue', y_column0)])
    return df_ret


def _logit(df: pd.DataFrame, x: str, y: str):
    is_valid_x = df[x].isnull() == False
    is_valid_y = df[y].isnull() == False
    is_valid = is_valid_x & is_valid_y
    df_valid = df[is_valid]
    valid_x = df_valid[x].astype(float)
    valid_y = df_valid[y].astype(float)

    try: 
        X = sm.add_constant(valid_x)
        mod = sm.Logit(valid_y, X)
        res = mod.fit()
        print(f'_logit: x: {x} y: {y}')
        res.summary()

        return res, {'valid': is_valid.sum(), 'valid_x': is_valid_x.sum(), 'valid_y': is_valid_y.sum(), 'df': len(df), 'valid_percent': float(is_valid.sum()) / float(len(df))}
    except Exception as e:
        print(f'[WARN] unable to _logit: e: {e}')
        return None, {'valid': is_valid.sum(), 'valid_x': is_valid_x.sum(), 'valid_y': is_valid_y.sum(), 'df': len(df), 'valid_percent': float(is_valid.sum()) / float(len(df))}



def safe_mean(x):
    if not x:
        return np.nan
    return np.mean(x)


def safe_max(x):
    if not x:
        return np.nan
    return np.max(x)