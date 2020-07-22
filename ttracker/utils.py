import math
from datetime import datetime

EPOCH = 621355968000000000


def timestamp_to_datetime(timestamp):
    adjusted_timestamp = math.floor(int(timestamp) - EPOCH) / 10 ** 7
    return datetime.utcfromtimestamp(adjusted_timestamp)
