# -*- coding: utf-8 -*-


import argparse
import nbformat

from COMBINE_harmonizer import exec_ipynb


def parse_args():
    '''
    Returns:
        TYPE: Description
    '''
    parser = argparse.ArgumentParser(description='running zz-exec.ipynb')
    parser.add_argument('-f', '--filename', type=str, required=True, help="zz-exec.ipynb filename")
    parser.add_argument('-t', '--timeout', type=int, required=False, default=1800, help='timeout')
    parser.add_argument('-k', '--kernel', type=str, required=False, default='python3', help="kernel (python3, ir)")

    args = parser.parse_args()

    return args


def main():
    """Summary
    """
    args = parse_args()

    filename = args.filename
    kernel_name = args.kernel
    timeout = args.timeout

    print(f'[INFO] to exec: filename: {filename}')
    nb_out = exec_ipynb.exec_ipynb(filename, timeout=timeout, kernel_name=kernel_name)

    print(f'[INFO] to save results: filename: {filename}')
    with open(filename, 'w') as f:
        nbformat.write(nb_out, f)
    print(f'[INFO] done: filename: {filename}')


if __name__ == '__main__':
    main()
