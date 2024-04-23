# -*- coding: utf-8 -*-

import pandas as pd
from tqdm import tqdm
import statsmodels.api as sm


#####
# linear regression
#####
def lr(df: pd.DataFrame, x_columns: list[str], y_columns: list[str]):
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
