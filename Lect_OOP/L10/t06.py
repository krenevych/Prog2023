class InputNonNegIntException(Exception):
    ERROR_CODE_NOT_INTEGER = 1
    ERROR_CODE_NEGATIVE = 2

    def __init__(self, message, err_code, orig_value, to_int_converted=None):
        self.message = message
        self.err_code = err_code
        self.orig_value = orig_value
        self.to_int_converted = to_int_converted

    def __str__(self):
        return (f"{self.message},"
                f" err_code={self.err_code},"
                f" orig_valur={self.orig_value},"
                f" to_int_converted={self.to_int_converted}")


