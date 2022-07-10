import logging
import sys

import pytest


def divide_numbers(counter, denominator):
    return counter / denominator


def introduce_youself(name: str):
    print(f"Hello my name is '{name}'!")


def introduce_youself_with_logging(name: str):
    logger = logging.getLogger("test_logger")
    print(f"Hello my name is '{name}'!")
    logger.debug(f"special logging for {name=}!")


class TestMyPytestWithSpecialConditions:
    """By starting with 'Test' the class is regarded a test class"""

    def test_divide_numbers_exception_behavoir(self):
        with pytest.raises(ZeroDivisionError):
            divide_numbers(counter=1, denominator=0)
            # this test is successfull

    def test_introduce_youself(self, capsys):
        my_name = 'Testing God'
        introduce_youself(my_name)
        assert my_name in capsys.readouterr().out

    def test_introduce_youself_logged(self, caplog):
        caplog.set_level(level=logging.DEBUG)

        my_name = 'Testing God'
        introduce_youself_with_logging(my_name)

        logging_records = caplog.records
        assert any([my_name in record.msg
                    for record in logging_records
                    if record.levelno == logging.DEBUG])

    @pytest.mark.skip(reason="this is deprecated")
    def test_some_depreacted_function(self):
        ...
        # this is all skipped

    @pytest.mark.skipif(sys.version_info < (3, 7), reason="Typ hinting not supported yet")
    def test_with_some_typhint_featues(self):
        ...

        from typing import List
        my_typed_list: List[int] = [1, 2, 3]
        assert len(my_typed_list) == 3

    @pytest.mark.skipif(sys.version_info.major < 4, reason="Not running future tests for Python 4")
    def test_with_some_future_features(self):
        raise Exception("This exception should never be raised, in Python 3.x")

    @pytest.mark.group_a
    def test_special_mark1(self):
        assert True

    @pytest.mark.group_a
    @pytest.mark.group_b
    def test_special_mark2(self):
        assert True

    @pytest.mark.group_b
    @pytest.mark.group_c
    def test_special_mark3(self):
        assert True
