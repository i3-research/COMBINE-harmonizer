# -*- coding: utf-8 -*-

import pandas as pd
from . import constants


def load_data_dict(filename: str, sheet_name: str) -> pd.DataFrame:
    '''
    Load Data Dictionary with filling the category column

    :param filename
    :param sheet_name

    :return dataframe for data dictionary.
    '''
    excel = pd.ExcelFile(filename)
    df_data_dict = pd.read_excel(excel, sheet_name=constants.SHEET_VARIABLES, dtype='O')

    is_valid_var = df_data_dict[constants.DATA_DICT_VAR_NAME].isnull() == False
    is_valid_type = df_data_dict[constants.DATA_DICT_VAR_TYPE].isnull() == False
    is_valid = is_valid_var & is_valid_type
    df_data_dict_valid = df_data_dict[is_valid].reset_index(drop=True)

    df_data_dict_valid = _fill_category(df_data_dict_valid)

    sheet_names = df_data_dict_valid[constants.DATA_DICT_CATEGORY].apply(lambda x: constants.CATEGORY_SHEET_MAP.get(x, None))
    is_valid_sheet_name = sheet_names == sheet_name

    df_data_dict_valid = df_data_dict_valid[is_valid_sheet_name]

    return df_data_dict_valid


def _fill_category(df: pd.DataFrame) -> pd.DataFrame:
    category = ''

    for idx, row in df.iterrows():
        var_name = row[constants.DATA_DICT_VAR_NAME]
        if pd.isnull(var_name):
            continue

        orig_category = row[constants.DATA_DICT_CATEGORY]

        if not pd.isnull(orig_category):
            category = orig_category
            continue

        df.loc[idx, constants.DATA_DICT_CATEGORY] = category

    return df
