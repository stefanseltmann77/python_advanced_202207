# minimum version of a pytest based unittests
def test_demo_that_something_is_true():
    """This test will automatically be detected via the test_*
    in the filename and the test_* at the function start"""
    assert True


def test_demo_that_something_else_is_also_true():
    """This test will automatically be detected via the test_*
    in the filename and the test_* at the function start"""
    assert 1 == 1


def this_is_no_test():
    """This function will be ignored, because it does NOT
    fit the pattern and doesn't start with test_* """
    raise Exception("This is line not allowed to be run")

# run this from the project root by just typing `./pytest` or `pytest` on windows.

# also run this with stating the specific file: ``pytest test_110_pytest_minimum.py``

# also run only the second test this with stating the specific test:
#   pytest test_110_pytest_minimum.py::test_demo_that_something_else_is_also_true
#   ``pytest test_110_pytest_minimum.py``
