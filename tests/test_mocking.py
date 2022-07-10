import pytest


class SomeClass:
    def calculate_pi(self):
        return 3.41


@pytest.fixture()
def someclass_instance():
    return SomeClass()


class TestMyPytestWithMocks:
    def test_without_mock(self, someclass_instance):
        assert someclass_instance.calculate_pi() == 3.41

    def test_simple_mock_with_lamda(self, someclass_instance, monkeypatch):
        fake_pi_value = 4.00

        # replace the original function with a fake function that returns 4.00 as pi
        monkeypatch.setattr(someclass_instance, 'calculate_pi', lambda *args: fake_pi_value)

        assert someclass_instance.calculate_pi() == fake_pi_value
