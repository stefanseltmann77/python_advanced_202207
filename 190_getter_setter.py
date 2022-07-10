##########################################################################################################
## A class recieves a path as input and schould sanitize it for storage

# correct path = "/user/btelligent/python_training"
# not wanted alternative = "/user/btelligent/python_training/"
# not wanted alternative = r"\user\btelligent\python_training"

path = "/user/btelligent/python_training"
path_alt1 = "/user/btelligent/python_training/"
path_alt2 = r"\user\btelligent\python_training"

# This would be the JAVA approach
class ClassWithPath(object):
    def __init__(self, path=None):
        if path: self.set_path(path)

    def set_path(self, path_input):
        path_tmp = path_input.replace("\\", "/")
        self.path = path_tmp[:-1] \
            if path_tmp.endswith("/") else path_tmp

    def get_path(self):
        return self.path

# works perfectly
cwp = ClassWithPath(path)
cwp.set_path(path_alt1)
cwp.set_path(path_alt2)
assert(path == cwp.get_path())


# This would be the Python approach
class ClassWithPath(object):
    def __init__(self, path=None):
        self._path = None
        if path: self.path = path

    @property
    def path(self): # the getter
        return self._path

    @path.setter
    def path(self, value): # the setter
        path_tmp = value.replace("\\", "/")
        self._path = path_tmp[:-1] \
            if path_tmp.endswith("/") else path_tmp

# works perfectly
cwp = ClassWithPath(path)
cwp.path = path_alt1
cwp.path = path_alt2
assert(path == cwp.path)

