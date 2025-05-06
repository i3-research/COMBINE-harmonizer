# -*- coding: utf-8 -*-

from typing import Optional

import re
import time

import pandas as pd
pd.options.mode.copy_on_write = True
from .constants import FLATTEN_MERGE_COLUMNS, FLATTEN_INDEX, FLATTEN_FOLLOW_UP_COLUMNS


def flatten_filename_prefix(filename: str):
    filename_prefix = re.sub(r'\.csv$', '', filename)
    the_list = filename_prefix.split('-')
    try:
        int_suffix = int(the_list[1][:2])
        return '-'.join(the_list[:2])
    except:
        return the_list[0]


def flatten_sheet_name(filename: str):
    filename_prefix = re.sub(r'\.csv$', '', filename)
    filename_prefix = re.sub(r'before-baseline', 'bb', filename_prefix)
    filename_prefix = re.sub(r'post-normo', 'pn', filename_prefix)
    return filename_prefix


def flatten_columns_with_prefix(df: pd.DataFrame, prefix: str) -> pd.DataFrame:
    column_map = {
        column: f'{prefix}:{column}' for column in df.columns if column not in FLATTEN_MERGE_COLUMNS}
    df_renamed = df.rename(columns=column_map)
    return df_renamed


def flatten(df: pd.DataFrame) -> pd.DataFrame:
    # setup index
    index = FLATTEN_MERGE_COLUMNS.copy()
    # special columns for follow-up columns
    for column in FLATTEN_FOLLOW_UP_COLUMNS:
        if column in df:
            index.append(column)

    # index and columns
    index_and_columns = index + [FLATTEN_INDEX]

    # flatten-index
    df[FLATTEN_INDEX] = df[FLATTEN_INDEX].apply(_tuple_flatten_column)

    # setup value columns (not in index_and_columns)
    value_columns = list(filter(lambda column: column not in index_and_columns, df.columns))

    # pivot
    print(f'_flatten: to pivot_table: df: {len(df)}')
    start_timestamp = time.time()
    df_pivot = pd.pivot_table(df, index=index, columns=[
                              FLATTEN_INDEX], values=value_columns, aggfunc=_agg)
    end_timestamp = time.time()
    print(f'_flatten: after pivot_table: time: {end_timestamp - start_timestamp}')

    # change multi-indexed columns to flattened columns.
    df_pivot.columns = df_pivot.columns.to_flat_index()
    print(f'_flatten: after to_flat_index')
    column_map = {column: _str_pivot_column(column) for column in df_pivot.columns}
    df_pivot = df_pivot.rename(columns=column_map).reset_index()

    return df_pivot


def _tuple_flatten_column(x):
    return tuple([int(each) for each in x.split('@')])


def _agg(the_list):
    if pd.isnull(the_list).any():
        return the_list

    if len(the_list) > 1:
        print(f'[WARN] _agg: the_list > 1: {len(the_list)}')

    return the_list.iloc[0]


def _str_pivot_column(x):
    last_x = x[-1]
    last_x_str = '@'.join([str(each) for each in last_x])
    return ':'.join(x[:-1] + (last_x_str,))


def flatten_column_tuple(column: str) -> tuple[str, str, Optional[tuple]]:
    column_list = column.split(':')

    prefix = ''
    var_name = ''
    postfix = None
    if len(column_list) == 1:
        var_name = column_list[0]
    elif len(column_list) == 2:
        prefix = column_list[0]
        var_name = column_list[1]
    elif len(column_list) == 3:
        prefix = column_list[0]
        var_name = column_list[1]
        postfix = column_list[2].split('@')
    else:
        prefix = column_list[0]
        var_name = column_list[1]
        postfix = column_list[2].split('@')
        print(f"[WARN] flatten_column_tuple: > 2 ':' in column: {column}")

    return prefix, var_name, postfix


def flatten_column_prefix(column: str) -> str:
    column_list = column.split(':')
    prefix = column_list[0] if len(column_list) >= 2 else ''
    return prefix
