# -*- coding: utf-8 -*-

import pandas as pd
pd.options.mode.copy_on_write = True
import numpy as np


def total_modified_sarnat_score(df: pd.DataFrame, columns: list[str]) -> pd.Series:
    '''
    Compute total modified Sarnat Score
    '''
    s = pd.Series(data=[np.nan] * len(df), index=df.index)
    for idx, column in enumerate(columns):
        s_column = df[column].astype(np.float64)
        is_valid = s_column.isnull() == False
        print(f'[INFO] ({idx}/{len(columns)}) column: {column} ({df[column].dtype}) valid: ({is_valid.sum()}/{len(df)})')  # noqa

        is_valid_nan = s.isnull() & is_valid
        s.loc[is_valid_nan] = 0
        s.loc[is_valid] += s_column[is_valid]

    return s
