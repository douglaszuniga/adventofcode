from functions.trebuchet import is_number
from functions.trebuchet import calibrate
from functions.trebuchet import get_calibration_value


def test_1_is_a_number():
    """When input is 1 then is_number should return true"""
    assert is_number('1') is True


def test_a_is_not_a_number():
    """When input is a then is_number should return true"""
    assert is_number('a') is False


def test_sample_01():
    input = "1abc2"
    expected = 12
    assert calibrate(input) is expected


def test_sample_02():
    input = "pqr3stu8vwx"
    expected = 38
    assert calibrate(input) is expected


def test_sample_03():
    input = "a1b2c3d4e5f"
    expected = 15
    assert calibrate(input) is expected


def test_sample_04():
    input = "treb7uchet"
    expected = 77
    assert calibrate(input) is expected


def test_calibration_value():
    assert get_calibration_value("test_trebuchet_input") is 142
