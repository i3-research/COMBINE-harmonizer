# -*- coding: utf-8 -*-

import os
import os.path
import logging
import yaml

config = {}


def init(filename: str='../config.yaml'):
    global config
    if not os.path.exists(filename):
        logging.error(f'filename not exists: {filename} pwd: {os.getcwd()}')
        return

    with open(filename, 'r') as f:
        config = yaml.full_load(f)
