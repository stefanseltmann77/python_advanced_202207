import pytest
from sqlalchemy import create_engine


class DBSQlite:
    def __enter__(self):
        self.engine = create_engine('sqlite:///:memory:')
        self.conn = self.engine.connect()
        return self.conn

    def __exit__(self, type, value, traceback):
        self.conn.close()


@pytest.fixture()
def database():
    # IMPORTANT: pass the context manager with yield.
    with DBSQlite() as db:
        # setup
        yield db  # actual test
        # teardown


@pytest.fixture()
def database_demodata(database):
    # setup some testdata
    database.execute("CREATE TABLE staff (staff_id integer, last_name varchar)")
    database.execute("INSERT INTO staff (staff_id, last_name) "
                     "VALUES (1, 'Pavlow'), (2, 'Skinner'), (3, 'Freud')")
    return database
