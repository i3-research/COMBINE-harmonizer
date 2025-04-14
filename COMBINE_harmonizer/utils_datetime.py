# -*- coding: utf-8 -*-

from typing import Optional

from datetime import datetime
import pandas as pd
pd.options.mode.copy_on_write = True


def date_to_day(the_date: str, birth_date: str) -> Optional[int]:
    '''
    Convert date to days after birth date for data privacy concern.
    '''
    if pd.isnull(the_date) or the_date == '':
        return ''

    try:
        the_datetime = datetime.strptime(the_date, '%Y-%m-%d')
    except Exception as e:
        if not pd.isnull(the_date):
            print(f'[WARN] date_to_day: unable to strptime: the_date: {the_date}')
        return the_date

    try:
        birth_datetime = datetime.strptime(birth_date, '%Y-%m-%d')
    except Exception as e:
        if not pd.isnull(birth_date):
            print(f'[WARN] date_to_day: unable to strptime: birth_date: {birth_date}')
        return the_date

    the_diff = the_datetime - birth_datetime

    return the_diff.days


def _parse_datetime(the_date, the_time) -> Optional[datetime]:
    try:
        the_datetime = datetime.strptime(f'{the_date} {the_time}', '%Y-%m-%d %H:%M:%S')
        return the_datetime
    except Exception as e:
        if not pd.isnull(the_date) and not pd.isnull(the_time):
            print(
                f'[WARN] datetime_to_day_hr: unable to strptime (with %S): the_date: {the_date} the_time: {the_time}')

    try:
        the_datetime = datetime.strptime(f'{the_date} {the_time}', '%Y-%m-%d %H:%M')
        return the_datetime
    except Exception as e:
        if not pd.isnull(the_date) and not pd.isnull(the_time):
            print(
                f'[WARN] datetime_to_day_hr: unable to strptime (with %M): the_date: {the_date} the_time: {the_time}')

    return None


def datetime_to_day_hr(the_date: str, the_time: str, birth_date: str, birth_time: str) -> tuple[Optional[int], Optional[int]]:
    '''
    Convert date time to (days, hr) after birth date for data privacy concern.
    '''
    if pd.isnull(the_time) or the_time == '':
        the_days = date_to_day(the_date, birth_date)
        return (the_days, '')

    the_datetime = _parse_datetime(the_date, the_time)
    if the_datetime is None:
        print(f'[WARN] datetime_to_day_hr: invalid the_datetime: {the_date} {the_time}')
        return (the_date, the_time)

    birth_datetime = _parse_datetime(birth_date, birth_time)
    if birth_datetime is None:
        print(f'[WARN] datetime_to_day_hr: invalid birth_datetime: {birth_date} {birth_time}')
        return (the_date, the_time)

    the_diff = the_datetime - birth_datetime
    diff_days = the_diff.days
    diff_hr = int(the_diff.seconds / 3600)

    if diff_days < 0 and diff_hr > 0:
        diff_days += 1
        diff_hr -= 24

    return (diff_days, diff_hr)


def anonymize_birth_date(birth_date: str) -> str:
    '''
    Anonymize birth date by retaining only YYYY-mm.
    '''
    return '-'.join(birth_date.split('-')[:2])


def anonymize_birth_time(birth_time: str) -> str:
    '''
    Anonymize birth time by retaining only HH.
    '''
    return birth_time.split(':')[0]
