import pytest

fo


class TestDevice:

    LATITUDE = 1
    LONGITUDE = 1

    PT =[LATITUDE, LONGITUDE]

    def test_get_nearby_point():

        newpt = get_nearby_point(PT, 0.5, 90)
        assert newpt[0] is not None
        assert newpt[1] is not None
        assert newpt[0] >= 1
        assert newpt[0] <= 2
        assert newpt[0] >= 1
        assert newpt[0] <= 2
