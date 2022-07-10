from enum import Enum, unique
from typing import Final


class DataBaseHandle:
    TG_TEST: Final[str] = 'sqlite'
    TG_PROD: Final[str] = 'msserver'

    def connect(self, target: str):
        if self.TG_TEST == target:
            return f"connect to {target}"
        elif self.TG_PROD == target:
            return f"connect different to {target}"


db = DataBaseHandle()
print(db.connect(target=DataBaseHandle.TG_TEST))


@unique
class DBTargets(Enum):
    TEST = 'sqlite'
    PROD = 'msserver'


class DataBaseHandleAlternate:

    def connect(self, target: DBTargets):
        if DBTargets.TEST is target:
            return f"connect to {target}"
        elif DBTargets.PROD is target:
            return f"connect different to {target}"


db = DataBaseHandleAlternate()
print(db.connect(target=DBTargets.TEST))


@unique
class DBTargets(Enum):
    TEST = 'sqlite'
    PROD = 'msserver'

    def __eq__(self, other):
        return other == self.value


assert DBTargets.TEST == 'sqlite'
assert DBTargets.TEST == DBTargets.TEST.value
assert DBTargets.TEST is DBTargets.TEST
assert DBTargets.TEST == DBTargets.TEST

assert not DBTargets.TEST == 'notsqlite'
assert not DBTargets.TEST == DBTargets.PROD.value
assert DBTargets.TEST is not DBTargets.PROD
assert not DBTargets.TEST == DBTargets.PROD
