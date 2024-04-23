# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
from tqdm import tqdm
import statsmodels.api as sm

import matplotlib.pyplot as plt

from . import plot


def logit(df: pd.DataFrame, x_columns: list[str], y_columns: list[str]):
    rets = []
    y_column0 = y_columns[0]
    for x_column in x_columns:
        for y_column in y_columns:
            pvalue = np.nan
            tvalue = np.nan
            b0 = np.nan
            b1 = np.nan
            b1_abs = np.nan
            the_OR = np.nan

            ret_logit, meta = _logit(df, x_column, y_column)

            if ret_logit is not None:
                pvalue = ret_logit.pvalues[x_column]
                tvalue = ret_logit.tvalues[x_column]
                b0 = ret_logit.params['const']
                b1 = ret_logit.params[x_column]
                b1_abs = np.abs(b1)
                the_OR = np.exp(b1)

            ret = {
                'x': x_column,
                'y': y_column,
                'ret': ret_logit,
                'pvalue': pvalue,
                'tvalue': tvalue,
                'b0': b0,
                'b1': b1,
                'b1_abs': b1_abs,
                'OR': the_OR,  # https://stats.oarc.ucla.edu/stata/faq/how-do-i-interpret-odds-ratios-in-logistic-regression/
                'valid': meta['valid'],
                'valid_x': meta['valid_x'],
                'valid_y': meta['valid_y'],
                'valid_percent': float(meta['valid_percent']),
            }
            rets.append(ret)

    df_ret = pd.DataFrame(rets)
    return df_ret


def _logit(df: pd.DataFrame, x: str, y: str):
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

    try:
        # formulate as:
        #    z = b_0 + b_1 \times x
        #
        #    z = log(\frac{y}{1 - y}), where 0 < y < 1
        #      => y = \frac{e^z}{1 + e^z}
        #
        print(f'_logit: to eval: x: {x} y: {y}')
        if is_valid.sum() < 20:
            print(f'[WARN] _logit: too few valid samples: x: {x} y: {y} valid: {is_valid.sum()}')
            return None, meta

        X = sm.add_constant(valid_x)
        model = sm.Logit(valid_y, X)
        res = model.fit()
        print(f'_logit: done: x: {x} y: {y}')
        res.summary()

        return res, meta
    except Exception as e:
        print(f'[WARN] unable to _logit: e: {e}')
        return None, meta


def plot_logit(df, x_column, y_column, x_column_info=None, y_column_info=None):
    '''
    plot logit
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

    try:
        X = sm.add_constant(valid_x)
        mod = sm.Logit(valid_y, X)
        ret = mod.fit()
        # print(f'_logit: x: {x} y: {y}')
        ret.summary()
    except Exception as e:
        print(f'[WARN] unable to _logit: e: {e}')
        return

    b0 = ret.params['const']
    b1 = ret.params[x_column]
    pvalue = ret.pvalues[x_column]
    tvalue = ret.tvalues[x_column]
    OR = np.exp(b1)

    fig = plt.figure(dpi=600)

    true_y = valid_y
    pred_y = valid_x.apply(lambda x: _sigmoid(x * b1 + b0))

    b0_str = plot.format_scientific_notation(b0)
    b1_str = plot.format_scientific_notation(b1)
    pvalue_str = plot.format_scientific_notation(pvalue)
    OR_str = plot.format_scientific_notation(OR)

    # title
    plus_sign = ' + ' if b1 >= 0 else ' '
    title = '$\\log\\left(\\frac{p}{1 - p}\\right) = %s%s%sx$\n$(n = %s, OR \\approx %s, p \\approx %s)$' % (b0_str, plus_sign, b1_str, len(df_valid), OR_str, pvalue_str)
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
    ax = plt.gca()
    min_x, max_x = ax.get_xlim()
    valid_x = pd.Series(np.arange(min_x, max_x, 0.0001))
    pred_y = valid_x.apply(lambda x: _sigmoid(x * b1 + b0))

    plt.plot(valid_x, pred_y)

    ax.set_xlim([min_x, max_x])
    plt.minorticks_off()

    return fig


def _sigmoid(x):
    return np.exp(x) / (1 + np.exp(x))
