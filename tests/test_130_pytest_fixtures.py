import pytest


@pytest.fixture
def dummy_data() -> list[list[int]]:
    return [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


@pytest.fixture(scope='session')
def dummy_data_session_scope() -> list[list[int]]:
    return [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


class TestMyPytestWithFixtures:
    """By starting with 'Test' the class is regarded a test class"""

    def test_do_some_trivial_test(self, dummy_data, dummy_data_session_scope):
        assert len(dummy_data) == 3
        assert len(dummy_data_session_scope) == 3

    def test_do_some_trivial_test_that_changes_the_mutable_data(self, dummy_data, dummy_data_session_scope):
        some_row = dummy_data.pop()
        assert some_row == [7, 8, 9]  # checks the last element of the list

        some_row = dummy_data_session_scope.pop()
        assert some_row == [7, 8, 9]  # checks the last element of the list

    def test_do_some_trivial_test_that_changes_the_mutable_data_again(self, dummy_data, dummy_data_session_scope):
        """This test succeeds only if the second fixture is on session level and the order of tests is not altered."""
        some_row = dummy_data.pop()
        assert some_row == [7, 8, 9]  # checks the last element of the list AGAIN, because the fixture is rerun

        some_row = dummy_data_session_scope.pop()
        assert some_row == [4, 5, 6]  # checks the second to last element of the list,
        # because the fixture has session scope and keeps its state
