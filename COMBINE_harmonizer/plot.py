# -*- coding: utf-8 -*-


def format_scientific_notation(val):
    '''
    Format scientific notation
    '''
    if _is_orig_val(val):
        return f'{val:.3f}'

    val_str = f'{val:.3e}'
    val_tuple = val_str.split('e')
    exponent = int(val_tuple[1])
    ret = val_tuple[0] + ' \\times 10^{%s}' % (exponent)

    return ret


def _is_orig_val(val: float) -> bool:
    if val > 10 ** 5 or val < -10 ** 5:
        return False

    if val >= 0.001 or val < -0.001:
        return f'{val:.3f}'
