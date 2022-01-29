# tests/test_distance.py
from Nicktoolbox.distance import haversine


def test_length_of_hello_world():
    testval = haversine(48.865070, 2.380009, 48.235070, 2.393409)
    assert testval >= 69 and testval <= 71
