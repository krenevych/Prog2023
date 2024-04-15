class InputNonNegIntException(Exception): # Базовий клас нашого виключення
    def __init__(self, message, orig_value):
        self.message = message
        self.orig_value = orig_value

    def __str__(self):
        return (f"{self.message},"
                f" orig_valuу={self.orig_value}")

class InputNonIntException(InputNonNegIntException):
    def __init__(self, message, orig_value):
        super().__init__(message, orig_value)

    def __str__(self):
        return (f"InputNonIntException: "
                f"{self.message},"
                f" orig_valur={self.orig_value},"
                )

class InputNegException(InputNonNegIntException):
    def __init__(self, message, orig_value, to_int_converted):
        super().__init__(message, orig_value)
        self.to_int_converted = to_int_converted

    def __str__(self):
        return (f"InputNegException: "
                f"{self.message},"
                f" orig_valur={self.orig_value},"
                f" to_int_converted={self.to_int_converted}"
                )




