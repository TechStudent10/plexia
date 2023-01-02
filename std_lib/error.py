import sys

TYPES = {
    "var": "Variable"
}

class Error:
    _type = "Error"
    def __init__(self, message):
        self.message = message

    def throw(self, stack_trace):
        err_msg = f"{self._type} (on <module>)"
        if len(stack_trace) > 1:
            err_msg += ":"
        separator = "-" * (len(err_msg) + 3)
        for stack in stack_trace:
            _type = TYPES[stack[0]]
            name = stack[1]
            err_msg += f"\n\t{_type}, {name}"
        err_msg += f"\n{self.message}"
        print(separator)
        print(err_msg)
        print(separator)
        print("Exiting program...")
        sys.exit()

class TypeError(Error):
    _type = "TypeError"

class SyntaxError(Error):
    _type = "SyntaxError"

class UnknownKeywordError(Error):
    _type = "UnknownKeywordError"