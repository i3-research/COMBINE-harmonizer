# -*- coding: utf-8 -*-

from typing import Any

import pandas as pd
pd.options.mode.copy_on_write = True
import numpy as np

from .constants import *

from . import utils_types
from . import cfg


_MAPPING = {
}

_RANK_MAPPING = {
}


def init_mapping(filename: str, column: str, column_postfix: str = ''):
    '''
    Initialize mapping of the study-specific variables to the standardized variables.
    '''
    excel = pd.ExcelFile(filename)
    sheet_names = list(excel.sheet_names)
    valid_sheet_names = list(filter(lambda x: x not in SHEET_RESERVED_TABS, sheet_names))
    column_with_postfix = column if not column_postfix else f'{column}-{column_postfix}'

    for idx, sheet_name in enumerate(valid_sheet_names):
        df = pd.read_excel(excel, sheet_name, dtype='O')
        print(f'[INFO] init_mapping ({idx}/{len(valid_sheet_names)}): {sheet_name}')
        _update_mapping(sheet_name, df, column, column_with_postfix)

    cfg_dict_map = cfg.config.get('dictionary_map', None)
    if cfg_dict_map is None:
        return

    cfg_sheet_names = cfg_dict_map.keys()
    for idx, sheet_name in enumerate(cfg_sheet_names):
        the_list = cfg_dict_map[sheet_name]
        if not the_list:
            continue

        print(f'[INFO] init_mapping (cfg_dict_map) ({idx}/{len(cfg_sheet_names)}): {sheet_name}')
        df = pd.DataFrame(the_list)
        _update_mapping(sheet_name, df, column, column_with_postfix)


def _update_mapping(sheet_name: str, df: pd.DataFrame, column: str, column_with_postfix: str):
    global _MAPPING

    if len(df) == 0:
        return

    _MAPPING[sheet_name] = {}

    # check the whether to use followup column.
    iter_column = column_with_postfix if column_with_postfix in df.columns else column
    if iter_column not in df.columns:
        print(f'[INFO] utils_mapping._update_mapping: ({sheet_name}): {iter_column} not in df.columns')  # noqa
        return

    for _, row in df.iterrows():
        if pd.isnull(row[iter_column]) or row[iter_column] == '':
            continue

        name = row['name']
        value = row[iter_column]
        _MAPPING[sheet_name][value] = name

        value_float = utils_types.to_float(value, is_suppress_warning=True)
        if isinstance(value_float, float):
            if value_float in _MAPPING[sheet_name] and _MAPPING[sheet_name][value_float] != name:
                print(f'[WARN] possible conflicting setup: sheet_name: {sheet_name} value: {value} value_float: {value_float} name: {name} map: {_MAPPING[sheet_name][value_float]}')  # noqa
            _MAPPING[sheet_name][value_float] = name

        value_int = utils_types.to_int(value, is_suppress_warning=True)
        if isinstance(value_int, int) and value_int == value_float:
            if value_int in _MAPPING[sheet_name] and _MAPPING[sheet_name][value_int] != name:
                print(f'[WARN] possible conflicting setup: sheet_name: {sheet_name} value: {value} value_int: {value_int} name: {name} map: {_MAPPING[sheet_name][value_int]}')  # noqa
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

    print(f'[WARN] unable to get value: sheet_name: {sheet_name} value: {value} value_float: {value_float} value_int: {value_int}')  # noqa

    return ''


def init_rank_mapping(filename: str, column: str = DEFAULT_ORDINAL_COLUMN):
    '''
    Initialize inverse mapping from standardized variables to the corresponding rank.
    '''
    global _RANK_MAPPING

    excel = pd.ExcelFile(filename)
    sheet_names = list(excel.sheet_names)
    valid_sheet_names = list(filter(lambda x: x not in SHEET_RESERVED_TABS, sheet_names))

    for _, sheet_name in enumerate(valid_sheet_names):
        df = pd.read_excel(excel, sheet_name, dtype='O')
        _update_rank_mapping(sheet_name, df, column)

    cfg_dict_map = cfg.config.get('dictionary_map', None)
    if cfg_dict_map is None:
        return

    for sheet_name, the_list in cfg_dict_map.items():
        if not the_list:
            continue
        df = pd.DataFrame(the_list)
        _update_rank_mapping(sheet_name, df, column)


def _update_rank_mapping(sheet_name: str, df: pd.DataFrame, column: str):
    global _RANK_MAPPING

    if column not in df.columns:
        return

    df[column] = df[column].astype(float)

    _RANK_MAPPING[sheet_name] = {}
    for _, row in df.iterrows():
        if pd.isnull(row['name']) or row['name'] == '':
            continue

        name = row['name']
        value = row[column]

        _RANK_MAPPING[sheet_name][name] = value


def get_rank_mapping_value(sheet_name: str, value: str) -> float:
    '''
    Get rank mapping value to the rank.
    '''
    if pd.isnull(value):
        return np.nan

    if value not in _RANK_MAPPING[sheet_name]:
        if value != '':
            print(f'[WARN] unable to get value: sheet_name: {sheet_name} value: {value}')
        return np.nan

    return _RANK_MAPPING[sheet_name][value]
