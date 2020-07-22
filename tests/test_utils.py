from ttracker.utils import timestamp_to_datetime
from datetime import datetime


def test_timestamp_to_datetime():
    timestamp = '637304631881165025'
    expected = datetime(2020, 7, 16, 2, 26, 28, 116503)
    result = timestamp_to_datetime(timestamp)
    assert result == expected
