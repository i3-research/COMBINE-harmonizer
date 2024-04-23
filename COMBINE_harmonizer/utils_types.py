# -*- coding: utf-8 -*-

from typing import Any, Optional

import pandas as pd
import numpy as np

#####
# to types
#####


def to_center(val):
    '''
    Format center-id.
    '''
    int_val = to_int(val)
    if not isinstance(int_val, int):
        return int_val

    return f'{int_val:02d}'


def to_bool(val: Optional[str | np.float64]) -> str:
    '''
    to bool type
    '''
    if val in ['N', 'n', '0', '0.0', 'False', 'false', 0, 0.0, False, 'No', 'FALSE', 'no']:
        return 'FALSE'

    if val in ['Y', 'y', '1', '1.0', 'True', 'true', 1, 1.0, True, 'Yes', 'YES', '1 Yes', '1 YES', 'TRUE', 'yes']:
        return 'TRUE'

    if val in ['U', 'u', 'un', 'DK', 'unknown']:
        return 'unknown'

    if val in ['-', '*', '~', '?', '', None]:
        return ''

    if pd.isnull(val):
        return ''

    print(f'[WARN] unable to bool: val: ({val}/{type(val)})')

    return ''


def to_int(val: Any, is_suppress_warning: bool = False) -> int:
    '''
    to int type
    '''
    if pd.isnull(val):
        return ''

    if val in ['*', '-']:
        return ''

    try:
        ret = int(float(val))
        return ret
    except Exception as e:
        if not is_suppress_warning:
            print(f'[WARN] unable to int: val ({val}/{type(val)}) e: {e}')
        return val


def to_float(val: Any) -> float:
    '''
    to float type
    '''
    if pd.isnull(val):
        return ''

    if val in ['*', '-']:
        return ''

    try:
        return float(val)
    except Exception as e:
        print(f'[WARN] unable to float: val ({val}/{type(val)}) e: {e}')
        return val


def to_str(val: Any) -> str:
    '''
    to str type
    '''
    if pd.isnull(val):
        return ''

    if val in [False]:
        return 'FALSE'

    if val in [True]:
        return 'TRUE'

    return str(val)


def to_lower(val: Any) -> str:
    '''
    to lowercase.
    '''
    return to_str(val).lower()


#####
# to inv types
#####
def to_inv_bool(val) -> float:
    '''
    bool to float (0.0 or 1.0)
    '''

    if pd.isnull(val):
        return np.nan

    if not isinstance(val, str):
        return float(val)

    if val in ['true', 'TRUE', 'True']:
        return 1.0
    elif val in ['false', 'FALSE', 'False']:
        return 0.0
    elif val in ['unknown']:
        return np.nan

    print(f'[WARN] to_inv_bool: invalid val: {val}')
    return 0.0


def to_inv_int(val) -> float:
    '''
    int to float (assuming already int).
    '''
    if pd.isnull(val):
        return float('nan')

    return float(val)


def to_inv_float(val) -> float:
    '''
    float to float
    '''
    if pd.isnull(val):
        return float('nan')

    return float(val)


def to_inv_text(val) -> str:
    '''
    inverse text: still the same value.
    '''
    return val
