# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np

from scipy import stats
from tqdm import tqdm

import matplotlib.pyplot as plt

from . import plot


def corr(df: pd.DataFrame, x_columns: list[str], y_columns: list[str]) -> pd.DataFrame:
    '''
    Compute correlation between x columns and y columns

    :param df The input dataframe
    :param x_columns: x columns
    :param y_columns: y columns

    :return The pd.DataFrame with [x, y, corr, r2, pvalue, valid, valid_x, valid_y, valid_percent]
    '''
    rets = []
    y_column0 = y_columns[0]
    for x_column in tqdm(x_columns):
        for y_column in y_columns:
            corr = np.nan
            r2 = np.nan
            pvalue = np.nan

            coeff, meta = _corr_coeff(df, x_column, y_column)

            if coeff is not None:
                corr = coeff.statistic
                r2 = corr * corr
                pvalue = coeff.pvalue

            ret = {
                'x': x_column,
                'y': y_column,
                'corr': corr,
                'r2': r2,
                'pvalue': pvalue,
                'valid': meta['valid'],
                'valid_x': meta['valid_x'],
                'valid_y': meta['valid_y'],
                'valid_percent': float(meta['valid_percent']),
            }
            rets.append(ret)

    df_ret = pd.DataFrame(rets)
    return df_ret


def _corr_coeff(df: pd.DataFrame, x: str, y: str):
    is_valid_x = df[x].isnull() == False
    is_valid_y = df[y].isnull() == False
    is_valid = is_valid_x & is_valid_y
    df_valid = df[is_valid]
    valid_x = df_valid[x].astype(float)
    valid_y = df_valid[y].astype(float)

    meta = {
        'valid': is_valid.sum(),
        'valid_x': is_valid_x.sum(),
        'valid_y': is_valid_y.sum(),
        'df': len(df),
        'valid_percent': float(is_valid.sum()) / float(len(df)),
    }

    print(f'_corr_coeff: to eval: x: {x} y: {y} valid_x: {is_valid_x.sum()} valid_y: {is_valid_y.sum()}')
    if is_valid.sum() < 20:
        print(f'[WARN] _corr_coeff: too few valid samples: x: {x} y: {y} valid: {is_valid.sum()}')
        return None, meta

    ret = stats.pearsonr(valid_x, valid_y)
    print(f'_corr_coeff: done: x: {x} y: {y}')

    return ret, meta


def plot_corr(df, x_column, y_column, x_column_info=None, y_column_info=None):
    '''
    plot corr
    '''

    x = df[x_column]
    y = df[y_column]
    is_valid_x = x.isnull() == False
    is_valid_y = y.isnull() == False
    is_valid = is_valid_x & is_valid_y
    columns = [x_column, y_column]
    df_valid = df[is_valid][columns].astype('float64')

    # XXX hack for 01:bloodValueClmEqPerLMin
    # if x_column == '01:bloodValueClmEqPerLMin':
    #     is_valid_hack = df_valid[x_column] > 50
    #     df_valid = df_valid[is_valid_hack]

    valid_x = df_valid[x_column]
    valid_y = df_valid[y_column]
    df_valid['_count'] = 1
    df_groupby = df_valid.groupby([x_column, y_column], as_index=False).agg({'_count': 'sum'})
    del df_valid['_count']

    m, b, *_ = stats.linregress(valid_x, valid_y)

    ret = stats.pearsonr(valid_x, valid_y)

    fig = plt.figure(dpi=600)
    x_mean = valid_x.mean()
    y_for_x_mean = m * x_mean + b
    m_str = f'{m:.2f}'
    b_str = f'{b:.2f}'
    pvalue_str = plot.format_scientific_notation(ret.pvalue)
    r2value_str = plot.format_scientific_notation(ret.statistic**2)

    # true_y = valid_y
    # pred_y = valid_x * m + b
    # r2_value2 = r2_score(true_y, pred_y)
    # r2_value2_str = plot.format_scientific_notation(r2_value2)

    # title
    plus_sign = ' + ' if b >= 0 else ' '
    title = '$y = %sx%s%s$\n$(n = %s, R^2 \\approx %s, p \\approx %s)$' % (m_str, plus_sign, b_str, len(df_valid), r2value_str, pvalue_str)
    plt.title(title)

    # heat-map / scatter-plot
    if df_groupby['_count'].max() > 2:
        plt.scatter(x=df_groupby[x_column], y=df_groupby[y_column], c=df_groupby['_count'], cmap='plasma')
        cbar = plt.colorbar()
        cbar.ax.set_ylabel('number of patients', rotation=270, labelpad=7)
    else:
        plt.scatter(x=df_groupby[x_column], y=df_groupby[y_column], color='#0f0c7c')

    # x-label and y-label
    if x_column_info is not None:
        x_title = f"{x_column_info['title']}"
        if x_column_info['unit']:
            x_title += f" ({x_column_info['unit']})"
        plt.xlabel(x_title)
    if y_column_info is not None:
        y_title = f"{y_column_info['title']}"
        if y_column_info['unit']:
            y_title += f" ({y_column_info['unit']})"
        plt.ylabel(y_title)

    # line
    plt.axline(xy1=(x_mean, y_for_x_mean), slope=m, label='')

    plt.minorticks_off()

    return fig
