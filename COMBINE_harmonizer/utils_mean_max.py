# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np


def safe_mean(the_list: list[float]) -> float:
    '''
    safe mean
    '''
    valid_list = list(filter(lambda x: pd.isnull(x) == False, the_list))
    if len(valid_list) == 0:
        return np.nan

    return sum(valid_list) / len(valid_list)


def safe_max(the_list: list[float]) -> float:
    '''
    safe max
    '''
    valid_list = list(filter(lambda x: pd.isnull(x) == False, the_list))
    if len(valid_list) == 0:
        return np.nan

    return max(valid_list)
