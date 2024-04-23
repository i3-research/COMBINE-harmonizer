# -*- coding: utf-8 -*-

import nbformat

from nbconvert.preprocessors import ExecutePreprocessor


def exec_ipynb(filename: str, timeout: int = 1800, kernel_name: str = 'python3') -> nbformat.NotebookNode:
    '''
    exec_ipynb

    Executing ipynb.

    :param filename
    :param timeout
    :param kernel_name
    '''
    with open(filename) as f:
        nb_in = nbformat.read(f, nbformat.NO_CONVERT)

    ep = ExecutePreprocessor(timeout=timeout, kernel_name=kernel_name)

    nb_out, resources = ep.preprocess(nb_in)

    return nb_out
