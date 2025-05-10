# -*- coding: utf-8 -*-

import pandas as pd
pd.options.mode.copy_on_write = True
import numpy as np
import itertools
import copy

from .constants import DATA_DICT_VAR_NAME, DATA_DICT_VAR_TYPE, RESERVED_COLUMNS, SHEET_MAIN, MAX_INT
from . import utils_types
from . import utils_mapping
from . import utils_flatten_index
from . import utils_data_dict


def build_value_map(excel_filename: str, sheet_name: str):
    df = utils_data_dict.load_data_dict(excel_filename, sheet_name)

    ret = {}
    for idx, each in df.iterrows():
        the_var = each[DATA_DICT_VAR_NAME]
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
# build-numeric-value-map
#####
def build_numeric_value_map(filename: str, sheet_name: str):
    df = utils_data_dict.load_data_dict(filename, sheet_name)
    is_valid_dict = df[DATA_DICT_VAR_NAME].isnull() == False
    is_valid_type = df[DATA_DICT_VAR_TYPE].isnull() == False
    is_valid = is_valid_dict & is_valid_type
    df_valid = df[is_valid].reset_index(drop=True)

    ret = {}
    for idx, each in df_valid.iterrows():
        the_var = each[DATA_DICT_VAR_NAME]
        the_type = each[DATA_DICT_VAR_TYPE]

        print(f'build_numeric_value_map: ({idx}/{len(df_valid)}) variable: {the_var} type: {the_type}')  # noqa
        ret[the_var] = _build_numeric_value_map(the_type)

    return ret


def _build_numeric_value_map(the_type):
    if the_type == 'bool':
        return utils_types.to_numeric_bool
    elif the_type == 'int':
        return utils_types.to_numeric_int
    elif the_type == 'float':
        return utils_types.to_numeric_float
    elif the_type in utils_mapping._RANK_MAPPING:
        return lambda val: utils_mapping.get_rank_mapping_value(the_type, val)
    else:
        print(f'[INFO] _build_numeric_value_map: to inv-text: type: {the_type}')
        return utils_types.to_numeric_text


#####
# normalize-value
#####
def normalize_value(
        df: pd.DataFrame,
        value_map,
        flatten_ids: list[str] = None,
        unique_id_map=None,
        order_map=None,
) -> pd.DataFrame:
    len_columns = len(df.columns)
    for idx, column in enumerate(df.columns):
        print(f'({idx}/{len_columns}) normalize_value: column: {column}')
        df[f'{column}.orig'] = df[column].copy()
        if column in value_map:
            df[column] = df[f'{column}.orig'].apply(lambda x: value_map[column](x))

    if flatten_ids is not None:
        utils_flatten_index.flatten_index(df, flatten_ids, unique_id_map=unique_id_map)

    if order_map is not None:
        df = reorder_columns(df, order_map)

    return df


#####
# build_variable_order_map
#####
def build_variable_order_map(excel_filename: str, sheet_name: str) -> dict:
    df = utils_data_dict.load_data_dict(excel_filename, sheet_name)
    is_valid_dict = df[DATA_DICT_VAR_NAME].isnull() == False
    is_valid_type = df['type'].isnull() == False
    is_valid = is_valid_dict & is_valid_type
    df_valid = df[is_valid]

    order_map_reserved = {each: idx for idx, each in enumerate(RESERVED_COLUMNS)}
    order_map_other = {
        row[DATA_DICT_VAR_NAME]: idx + len(RESERVED_COLUMNS)
        for idx, row in df_valid.iterrows()
        if row[DATA_DICT_VAR_NAME] not in RESERVED_COLUMNS
    }
    order_map = copy.deepcopy(order_map_reserved)
    order_map.update(order_map_other)

    if sheet_name == SHEET_MAIN:
        # XXX hack for duplicated columns
        # derived from Dictionary/00-check-data-dict-dup-main.ipynb
        order_map['MRIDate'] = 907
        order_map['MRITime'] = 908

        order_map['birthDate'] = 176

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

    reserved_columns = list(filter(lambda x: x in columns_without_orig, RESERVED_COLUMNS))
    other_columns = list(filter(lambda x: x not in RESERVED_COLUMNS, columns_without_orig))

    columns = reserved_columns + other_columns
    columns_and_origs = list(itertools.chain.from_iterable(
        [_column_and_orig(each, columns_with_orig) for each in columns]))

    return df[columns_and_origs]


def _get_order(x, order_map):
    if x not in order_map:
        print(f'[WARN] not in order_map: {x}')
        return MAX_INT

    return order_map[x]


def _column_and_orig(column, columns_with_orig):
    ret = [column]
    if column + '.orig' in columns_with_orig:
        ret += [column + '.orig']

    return ret


#####
# cc to cc/kg
#####
def cc_to_cc_per_kg(
        df: pd.DataFrame,
        df_birth_weight: pd.DataFrame,
        columns: list[str],
        birth_weight_g_column: str
):
    '''
    assume df contains no birth_weight_g_column
    '''

    df_merge = df
    is_df_with_birth_weight_column = birth_weight_g_column in df.columns

    if not is_df_with_birth_weight_column:
        birth_weight_columns = ['center', 'subjectID', birth_weight_g_column]
        df_birth_weigth_with_columns = df_birth_weight[birth_weight_columns]

        df_merge = df.merge(df_birth_weigth_with_columns, on=['center', 'subjectID'], how='left')

    for column in columns:
        is_valid = (df_merge[birth_weight_g_column].isnull() ==
                    False) & (df_merge[column].isnull() == False)
        df_merge.loc[is_valid, column] = df_merge[is_valid].apply(
            lambda x: f'{(
                float(x[column]) * 1000 / float(x[birth_weight_g_column])):.1f}',
            axis=1)
        df_merge.loc[is_valid == False, column] = np.nan

    if not is_df_with_birth_weight_column:
        del df_merge[birth_weight_g_column]

    return df_merge


def numeric_values(df: pd.DataFrame, numeric_value_map: dict) -> pd.DataFrame:
    df_ret = df.copy()
    for idx, column in enumerate(df_ret.columns):
        column_list = column.split(':')
        var_name_idx = 1 if len(column_list) >= 2 else 0
        var_name = column_list[var_name_idx]

        if var_name not in numeric_value_map:
            print(f'[WARN] ({idx}/{len(df_ret.columns)}) not in numeric_value_map: {var_name}')
            continue

        print(f'[INFO] ({idx}/{len(df_ret.columns)}) to numeric value: column: {column} var_name: {var_name}')  # noqa
        df_ret.loc[:, column] = df_ret[column].apply(numeric_value_map[var_name])

    return df_ret
