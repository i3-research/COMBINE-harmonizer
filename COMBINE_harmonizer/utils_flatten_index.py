# -*- coding: utf-8 -*-

import pandas as pd
pd.options.mode.copy_on_write = True
from . import constants


def flatten_index(df: pd.DataFrame, flatten_ids: list[str], subject_id_idx: str = 'subjectID', center_id_idx: str = 'center', unique_id_map=None):
    '''
    flatten index
    '''
    df[f'{constants.FLATTEN_INDEX}_tmp'] = df.apply(
        lambda x: _flatten_index(x, flatten_ids), axis=1)
    if unique_id_map is None:
        unique_ids = list(df[f'{constants.FLATTEN_INDEX}_tmp'].unique())
        unique_ids.sort()
        unique_id_map = {each: each for each in unique_ids}

    df[constants.FLATTEN_INDEX] = df[f'{constants.FLATTEN_INDEX}_tmp'].apply(
        lambda x: unique_id_map[x])
    del df[f'{constants.FLATTEN_INDEX}_tmp']

    print(f"flatten_index: flatten_ids: {flatten_ids} unique_id_map: {unique_id_map} the_type: {df[constants.FLATTEN_INDEX].dtype}")  # noqa

    _ensure_unique_flatten_index(df, subject_id_idx, center_id_idx)

    return df


def _flatten_index(the_series, flatten_ids):
    the_list = [the_series[each] for each in flatten_ids]
    # the_list_str = ['' if pd.isnull(each) else str(each) for each in the_list]
    return the_list[0] if len(flatten_ids) == 1 else '@'.join([str(each) for each in the_list])


def _ensure_unique_flatten_index(df: pd.DataFrame, subject_id_idx: str = 'subjectID', center_id_idx: str = 'center'):
    sort_columns = [center_id_idx, subject_id_idx, 'uniqueID', constants.FLATTEN_INDEX]
    df.sort_values(by=sort_columns, inplace=True)

    pre_unique_id = None
    pre_index = None
    count = 0
    for idx, row in df.iterrows():
        current_unique_id = row['uniqueID']
        current_idx = row[constants.FLATTEN_INDEX]
        if current_unique_id == pre_unique_id and current_idx == pre_index:
            count += 1
            print(f"[WARN] not unique: ({idx}/{len(df)}) unique_id: {current_unique_id} flatten_index: {current_idx}")  # noqa
            # df.loc[idx, '_flatten_index'] += f'-{count:02d}'
        else:
            count = 0
        pre_unique_id = current_unique_id
        pre_index = current_idx
