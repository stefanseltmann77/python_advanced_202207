from pathlib import Path
from typing import NamedTuple
import requests
from requests import Response

import pandas as pd
import pytest
from sqlalchemy.engine import ResultProxy


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
        monkeypatch.setattr(someclass_instance, 'calculate_pi', lambda *args: fake_pi_value)
        # the mock is only valid within this function.
        assert someclass_instance.calculate_pi() == fake_pi_value

    def test_simple_without_mock_again(self, someclass_instance, monkeypatch):
        # the mock is only isolated within the scope of the last test.
        assert someclass_instance.calculate_pi() == 3.41

    def test_web_crawling(self, monkeypatch):
        # testsetup:
        def fake_response(url):
            _ = url
            web_result = Response()
            web_result.status_code = 200
            return web_result

        # replacing a method of a module
        monkeypatch.setattr(requests, 'get', raising=True, value=fake_response)
        # replacing an attribute of a class
        monkeypatch.setattr(Response, 'text', raising=True, value='<h1>This is a website. New office in Berlin</h1>')

        # the actual test:
        result: Response = requests.get(url="http://www.btelligent_latest_news.de")
        assert result.status_code == 200
        assert "Berlin" in result.text

    def test_database_query(self, monkeypatch, database_demodata):
        class RecStaff(NamedTuple):
            staff_id: int
            last_name: str

        def fechall_fake(*args):
            return [RecStaff(staff_id=456, last_name='Hammet'),
                    RecStaff(staff_id=789, last_name='Hatfield')]

        result = database_demodata.execute("SELECT * FROM staff ORDER BY staff_id").fetchall()
        assert result.pop().last_name == 'Freud'

        monkeypatch.setattr(ResultProxy, 'fetchall', fechall_fake)
        result_mocked = database_demodata.execute("SELECT * FROM staff ORDER BY staff_id").fetchall()

        assert result_mocked.pop().last_name == 'Hatfield'


    def do_some_stuff(self):

        # ...
        df = pd.read_csv(Path('some_file.csv'))
        result = self.db.execute('SELECT * FROM table').fetchall()
        # ...


    def _load_csv_source(self, path):
        return pd.read_csv(path)

    def _do_specific_query(self):
        return self.db.execute('SELECT * FROM table').fetchall()

    def do_some_stuff_better_testable(self):

        # ...
        df = self._load_csv_source(Path('some_file.csv'))
        result = self._do_specific_query()
        # ...
