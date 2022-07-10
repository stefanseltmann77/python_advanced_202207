# example for class definition
from pathlib import Path


class CoolDataApplication:

    def __init__(self, path_to_datasets: str):
        self.path_to_datasets = path_to_datasets

    def do_data_magic(self): ...


class BiggerCoolDataApplication:

    def __init__(self, path_to_new_datasets: str, old_application: CoolDataApplication):
        self.path_to_new_datasets = path_to_new_datasets
        self.base_application = old_application

    def do_better_data_magic(self):
        _ = self.base_application.path_to_datasets


class CoolDataApplicationV2:

    def __init__(self, path_to_datasets: str):
        self.path_to_dataset = path_to_datasets

    def do_data_magic(self):
        ...

    @property
    def path_to_dataset(self):
        return str(self._path_to_dataset)

    @path_to_dataset.setter
    def path_to_dataset(self, value):
        path = Path(value)
        if path.is_dir():
            raise Exception("no directories allowed")
        else:
            self._path_to_dataset = path


year = 2020
user = ['Max']


def print_something(input, values):
    print(values)
    print(input)
    input += 1
    values.append('Michael')
    print(input)


print_something(year, user)
print(year)
print(user)


class DataBaseHandle:

    def __init__(self, configs):
        set_configs...

    def connect(self):
        url = self._build_connections_string()...

    def _build_connections_string(self): ...

    def _check_table_exists(self): ...

    def _check_dependencies(self): ...

    def drop_table(self, table_name):
        self._check_table_exists()
        self._check_dependencies()
        self.connect().execute(build_command)
        ...


class DataLakeFileConnection:

    def _get_service_client(self): ...

    @staticmethod
    def _match_filenames_by_filter(file_names: Sequence[str], filter_str: str) ...:

    def _download_rawbytes(self, **kwargs): ...

    def _parse_date_from_filename(self, **kwargs): ...

    def get_file_list(self, path):
        ... = self._parse_date_from_filename()

    def load_file_as_df(self, path):
        buffer = self._download_rawbytes()
        ...

    def load_file_as_excel(self):
        buffer = self._download_rawbytes()
        ...
