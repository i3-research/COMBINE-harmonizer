# -*- coding: utf-8 -*-

from typing import Any

import pandas as pd
import numpy as np

from .constants import *

from . import utils_types
from . import cfg


_MAPPING = {
}

_INV_MAPPING = {
}


def init_mapping(filename: str, column: str, column_postfix: str = ''):
    '''
    Initialize mapping of the study-specific variables to the standardized variables.
    '''
    excel = pd.ExcelFile(filename)
    sheet_names = list(excel.sheet_names)
    valid_sheet_names = list(filter(lambda x: x not in SHEET_RESERVED_TABS, sheet_names))
    postfix_column = column if not column_postfix else f'{column}-{column_postfix}'

    for _, sheet_name in enumerate(valid_sheet_names):
        df = pd.read_excel(excel, sheet_name, dtype='O')
        _init_mapping_update_mapping(sheet_name, df, column, postfix_column)

    cfg_dict_map = cfg.config.get('dictionary_map', None)
    if cfg_dict_map is None:
        return

    for sheet_name, the_list in cfg_dict_map.items():
        if not the_list:
            continue

        df = pd.DataFrame(the_list)
        _init_mapping_update_mapping(sheet_name, df, column, postfix_column)


def _init_mapping_update_mapping(sheet_name: str, df: pd.DataFrame, column: str, postfix_column: str):
    global _MAPPING

    if len(df) == 0:
        return

    _MAPPING[sheet_name] = {}

    # check the whether to use followup column.
    each_column = postfix_column if postfix_column in df.columns else column

    for _, row in df.iterrows():
        if pd.isnull(row[each_column]) or row[each_column] == '':
            continue

        name = row['name']
        value = row[each_column]
        _MAPPING[sheet_name][value] = name

        value_float = utils_types.to_float(value)
        if isinstance(value_float, float):
            if value_float in _MAPPING[sheet_name] and _MAPPING[sheet_name][value_float] != name:
                print(f'[WARN] possible conflicting setup: sheet_name: {sheet_name} value: {value} value_float: {value_float} name: {name} map: {_MAPPING[sheet_name][value_float]}')
            _MAPPING[sheet_name][value_float] = name

        value_int = utils_types.to_int(value)
        if isinstance(value_int, int) and value_int == value_float:
            if value_int in _MAPPING[sheet_name] and _MAPPING[sheet_name][value_int] != name:
                print(f'[WARN] possible conflicting setup: sheet_name: {sheet_name} value: {value} value_int: {value_int} name: {name} map: {_MAPPING[sheet_name][value_int]}')
            _MAPPING[sheet_name][value_int] = name


def get_mapping_value(sheet_name: str, value: str) -> Any:
    '''
    Get mapping value
    '''
    if pd.isnull(value):
        return ''

    if value == '' and '' not in _MAPPING[sheet_name]:
        return

    if value in _MAPPING[sheet_name]:
        return _MAPPING[sheet_name][value]

    value_float = utils_types.to_float(value)
    if value_float in _MAPPING[sheet_name]:
        return _MAPPING[sheet_name][value_float]

    value_int = utils_types.to_int(value, is_suppress_warning=True)
    if value_int in _MAPPING[sheet_name]:
        return _MAPPING[sheet_name][value_int]

    print(f'[WARN] unable to get value: sheet_name: {sheet_name} value: {value} value_float: {value_float} value_int: {value_int}')

    return ''


def init_inv_mapping(filename: str, column: str = '_inv'):
    '''
    Initialize inverse mapping from standardized variables to the corresponding rank.
    '''
    global _INV_MAPPING

    excel = pd.ExcelFile(filename)
    sheet_names = list(excel.sheet_names)
    valid_sheet_names = list(filter(lambda x: x not in SHEET_RESERVED_TABS, sheet_names))

    for _, sheet_name in enumerate(valid_sheet_names):
        df = pd.read_excel(excel, sheet_name, dtype='O')
        _init_inv_mapping_update_inv_mapping(sheet_name, df, column)

    cfg_dict_map = cfg.config.get('dictionary_map', None)
    if cfg_dict_map is None:
        return

    for sheet_name, the_list in cfg_dict_map.items():
        if not the_list:
            continue
        df = pd.DataFrame(the_list)
        _init_inv_mapping_update_inv_mapping(sheet_name, df, column)


def _init_inv_mapping_update_inv_mapping(sheet_name: str, df: pd.DataFrame, column: str):
    global _INV_MAPPING

    if column not in df.columns:
        return

    df[column] = df[column].astype(float)

    _INV_MAPPING[sheet_name] = {}
    for _, row in df.iterrows():
        if pd.isnull(row['name']) or row['name'] == '':
            continue

        name = row['name']
        value = row[column]

        _INV_MAPPING[sheet_name][name] = value


def get_inv_mapping_value(sheet_name: str, value: str) -> Any:
    '''
    Get inverse mapping value to the rank.
    '''
    if pd.isnull(value):
        return np.nan

    if value == '' and '' not in _INV_MAPPING[sheet_name]:
        return np.nan

    if value not in _INV_MAPPING[sheet_name]:
        print(f'[WARN] unable to get value: sheet_name: {sheet_name} value: {value}')
        return np.nan

    return _INV_MAPPING[sheet_name][value]
