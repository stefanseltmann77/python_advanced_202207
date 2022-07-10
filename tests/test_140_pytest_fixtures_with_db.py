class TestMyPytestWithDBFixture:
    """By starting with 'Test' the class is regarded a test class"""

    def test_do_stuff_with_db(self, database):
        # the database fixture is automatically available via the conftest.py
        test_value = 1
        assert database.execute(f"SELECT {test_value}").fetchone() == (test_value,)

    def test_do_stuff_with_db_filled_with_dummydata(self, database_demodata):
        result = database_demodata.execute("SELECT * FROM staff").fetchall()
        current_rowcount = len(result)

        database_demodata.execute("INSERT INTO staff (staff_id, last_name) VALUES (4, 'Maslow')")
        result_update = database_demodata.execute("SELECT * FROM staff").fetchall()
        updated_rowcount = len(result_update)

        assert current_rowcount < updated_rowcount
