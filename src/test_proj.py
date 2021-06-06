""""This file consists of all the test cases"""
from proj import DataAccess
from proj import main

tst = DataAccess()


def test_marks():
    """"To test marks method"""
    assert tst.marks(1200) == 1


def test_hobbies():
    """"To test hobbies method"""
    assert tst.hobbies(1201) == 2


def test_travel():
    """"To test travel method"""
    assert tst.travel(1214) == 3


def test_languages():
    """"To test languages method"""
    assert tst.languages(1210) == 4


def test_domain():
    """"To test domain method"""
    assert tst.domain(1203) == 5


def test_main():
    """"To test for all kind of entries that can
    be made by the user
    """
    assert main(0, 0) == 1
    assert main(1100, 1) == 1
    assert main(100, 4) == 1
    assert main(15, 5) == 1
    assert main(-1, 2) == 1
    assert main(1199, 3) == 1
    assert main(1218, 1) == 2
    assert main(1280, 2) == 2
    assert main(1299, 3) == 2
    assert main(1300, 4) == 2
    assert main(1400, 5) == 2
    assert main(1201, 'abed') == 3
    assert main(1202, 0) == 4
    assert main(1203, -25) == 4
    assert main(1204, 6) == 5
    assert main(1205, 100) == 5
    assert main(1206, 1) == 6
    assert main(1207, 2) == 6
    assert main(1208, 3) == 6
    assert main(1209, 4) == 6
    assert main(1210, 5) == 6
