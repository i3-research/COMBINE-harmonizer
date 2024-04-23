# -*- coding: utf-8 -*-

from typing import Optional

import pandas as pd

from . import utils_types


#####
# get columns
#####
def get_columns(df: pd.DataFrame, category: str, subcategory: str) -> list[str]:
    is_valid = (df['Category'] == category) & (df['Subcategory'] == subcategory)
    df_valid = df[is_valid]
    return list(df_valid['Standardized_VariableNames_Dictionary'])


#####
# unique-id
#####
def unique_id(df: pd.DataFrame, subject_id_idx: str = 'subjectID', center_id_idx: str = 'center') -> pd.Series:
    '''
    Construct unique-id (center_id:subject_id)
    '''

    return df.apply(lambda x: f'{x[center_id_idx]}:{x[subject_id_idx]}', axis=1)


#####
# valid columns
#####
def valid_columns(df: pd.DataFrame, columns: list[str], debug_df=False, debug_columns=True) -> pd.DataFrame:
    valid_columns = [column for column in df.columns if column in columns]

    if debug_df:
        for idx, column in enumerate(df.columns):
            if column not in valid_columns:
                print(f'({idx}/{len(df.columns)}) {column} not in columns')

    if debug_columns:
        for idx, column in enumerate(columns):
            if column not in valid_columns:
                print(f'({idx}/{len(columns)}) {column} not in df')

    return df[valid_columns]


#####
# postprocess
#####
def postprocess(df: pd.DataFrame, subject_id_idx: str = 'subjectID', center_id_idx: str = 'center', first_columns: Optional[list[str]] = None) -> pd.DataFrame:
    '''
    Postprocess after normalize columns
    '''

    df[center_id_idx] = df[center_id_idx].apply(utils_types.to_center)
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
# column info
#####
def column_info(df: pd.DataFrame):
    for idx, column in enumerate(df.columns):
        invalid = df[column].isnull().sum()
        valid = len(df) - invalid
        # XXX remove column values
        # print(f'({idx}/{len(df.columns)}) {column}: ({valid}/{invalid}) {list(df[column].unique())}')
        print(f'({idx}/{len(df.columns)}) {column}: ({valid}/{invalid})')
