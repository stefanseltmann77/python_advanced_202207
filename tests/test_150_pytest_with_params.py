import pytest


def make_str_to_lower(input_str: str):
    return input_str.lower()


def divide_numbers(counter, denominator):
    return counter / denominator


class TestMyPytestWithParams:
    """By starting with 'Test' the class is regarded a test class"""

    @pytest.mark.parametrize('input_str', ('A', 'b', 'C'))
    def test_make_str_to_lower(self, input_str):
        assert make_str_to_lower(input_str) == input_str.lower()

    @pytest.mark.parametrize('counter,denominator,result', [(4, 2, 2), (10, 5, 2), (9, 3, 3)])
    def test_divide_numbers(self, counter, denominator, result):
        assert divide_numbers(counter, denominator) == result
