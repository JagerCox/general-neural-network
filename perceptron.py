import math


class Perceptron:

    snippet = ""
    memory_raw = []
    current_weight = -1
    correction_bia = 1  # Total sigma 0-1

    # Constructor

    def __init__(self, snippet_file="medium.snippet"):
        self.memory_raw = []
        self.correction_bia = 1
        self.current_weight = -1
        self.snippet = snippet_file

    # Private

    def _run_snippet_function(self, file_snippet, globals=None, locals=None):
        if globals is None:
            globals = {}
        globals.update({
            "__file__": file_snippet,
            "__name__": "__main__",
        })
        with open(file_snippet, 'rb') as file:
            exec(compile(file.read(), file_snippet, 'exec'), globals, locals)

    # Public

    def add_value_raw(self, value):
        locals_ = {}
        self.memory_raw.append(value)
        self._run_snippet_function(self.snippet, {'values': self.memory_raw}, locals_)
        self.current_weight = locals_['result']

    def sigma_value(self, test_value):
        return math.fabs((self.current_weight - test_value) * self.correction_bia)

    # Public properties

    def set_memory_raw(self, list_values):
        self.memory_raw = list_values

    def get_memory_raw(self):
        return self.memory_raw

    def set_weight(self, weight):
        self.current_weight = weight

    def get_weight(self):
        return self.current_weight

    def set_bias(self, value_bia):
        self.correction_bia = value_bia

    def clear_memory(self):
        self.memory_raw = []