# minimum version of a pytest based unittests class

class TestMyMinimumPytestClasses:
    """By starting with 'Test' the class is regarded a test class"""

    def test_demo_that_something_is_true(self):
        """This test will automatically be detected via the test_*
        in the filename and the test_* at the function start"""
        assert True

    def test_demo_that_something_else_is_also_true(self):
        """This test will automatically be detected via the test_*
        in the filename and the test_* at the function start"""
        assert 1 == 1

    def this_is_no_test(self):
        pass

