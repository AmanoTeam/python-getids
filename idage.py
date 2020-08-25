#!/bin/env python
import json
import math
from datetime import datetime

ages = open("ages.json")

nids = json.load(ages)

min_id = list(nids.keys())[0]
max_id = list(nids.keys())[-1]

def get_date(id):
    if id < int(min_id):
        return (-1, datetime.fromtimestamp(nids[min_id]/1000))
    elif id > int(max_id):
        return (1, datetime.fromtimestamp(nids[max_id]/1000))
    else:
        lid = int(min_id)
        for i in nids.keys():
            if id <= int(i):
                # calculate middle date
                uid = int(i)
                lage = nids[str(lid)]/1000
                uage = nids[i]/1000

                idratio = ((id - lid) / (uid - lid))
                mid_date = math.floor((idratio * (uage - lage)) + lage)
                return (0, datetime.fromtimestamp(mid_date))
            else:
                lid = int(i)


def get_age(id):
    d = get_date(id)
    return (
        "older_than" if d[0] < 0 else "newer_than" if d[0] > 0 else "aprox",
        f"{d[1].month}/{d[1].year}"
    )

