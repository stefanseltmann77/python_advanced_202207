from functools import singledispatchmethod

class TestClass:

    @singledispatchmethod
    def connect(self, target):
        if self.TG_TEST == target:
            return f"connect to {target}"
        elif self.TG_PROD == target:
            return f"connect different to {target}"


    @connect.register
    def _(self, target: str):
        print(f"string {target}")

    @connect.register
    def _(self, target: int):
        raise NotImplementedError()


if __name__ == '__main__':
    TestClass().connect('abc')
    TestClass().connect(123)
