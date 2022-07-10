some_dict = {"a": 1, "b": 2, "c": 3}
some_key = [1,2]
if isinstance(some_key, str) and some_key in some_dict:
    result = some_dict[some_key]
else:
    result = None


some_dict = {"a": 1, "b": 2, "c": 3}
some_key = 8
try:
    result = some_dict[some_key]
except (TypeError, KeyError):
    result = None


class SomeObject(object):
    content = "ABCD"
    def __getitem__(self, item):
        return self.content[item]

    def __len__(self):
        return len(self.content)

some_input = "ABCD"                 # String
          # = ("A", "B", "C", "D")   # Tuple
          # = ["A", "B", "C", "D"]   # List
          # = SomeObject()           # Whatever

for i in range(len(some_input)):
    print(some_input[i])

