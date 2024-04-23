# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np


def total_modified_sarnat_score(df: pd.DataFrame, columns: list[str]) -> pd.Series:
    '''
    Compute total modified Sarnat Score
    '''
    s = pd.Series(data=[np.nan] * len(df), index=df.index)
    for idx, column in enumerate(columns):
        is_valid = df[column].isnull() == False
        print(f'[INFO] ({idx}/{len(columns)}) column: {column} valid: ({is_valid.sum()}/{len(df)})')

        is_valid_nan = s.isnull() & is_valid
        s.loc[is_valid_nan] = 0
        s.loc[is_valid] += df.loc[is_valid, column]

    return s
