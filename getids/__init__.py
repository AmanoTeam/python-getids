"""
Python port of the GetIDs engine that calculates the date of creation for Telegram accounts using known creation dates.

This module provides two functions, `get_date_as_string` and `get_date_as_datetime`, which calculate the date of creation for Telegram accounts using known creation dates.
"""

import json
import math
from typing import Tuple
import os.path
from datetime import datetime

path = os.path.dirname(__file__)

with open(os.path.join(path, "ages.json")) as ages_file:
    ages_json: dict = json.load(ages_file)

min_id = list(ages_json.keys())[0]
max_id = list(ages_json.keys())[-1]


def get_date_as_datetime(id: int) -> Tuple[int, datetime]:
    """
    Calculates the date of creation for Telegram accounts using known creation dates, returning a `datetime` object.

    :param id: The ID of the account to calculate the creation date for.
    :return: A tuple containing the result of the calculation and the date of creation as a `datetime` object.
    """

    if id < int(min_id):
        return (-1, datetime.fromtimestamp(ages_json[min_id] / 1000))
    elif id > int(max_id):
        return (1, datetime.fromtimestamp(ages_json[max_id] / 1000))

    lower_id = int(min_id)
    for i in ages_json.keys():
        if id <= int(i):
            # calculate middle date
            uid = int(i)
            lage = ages_json[str(lower_id)] / 1000
            uage = ages_json[i] / 1000

            idratio = (id - lower_id) / (uid - lower_id)
            mid_date = math.floor((idratio * (uage - lage)) + lage)
            return (0, datetime.fromtimestamp(mid_date))

        lower_id = int(i)


def get_date_as_string(id: int) -> Tuple[str, str]:
    """
    Calculates the date of creation for Telegram accounts using known creation dates, returning a string in the format `MM/YYYY`.

    :param id: The ID of the account to calculate the creation date for.
    :return: A tuple containing the result of the calculation and the date of creation as a string in the format `MM/YYYY`.
    """

    d = get_date_as_datetime(id)
    return (
        "older_than" if d[0] == -1 else "newer_than" if d[0] == 1 else "aprox",
        f"{d[1].month}/{d[1].year}",
    )


# Aliases for backwards compatibility
get_date = get_date_as_datetime
get_age = get_date_as_string

__all__ = ["get_date_as_string", "get_date_as_datetime"]
