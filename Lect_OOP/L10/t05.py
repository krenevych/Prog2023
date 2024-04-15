from t06 import InputNonNegIntException
def inputNonNegInt(*args, **kwargs):
    """ функція введення з клавіатури лише невід’ємних цілих чисел."""
    s = input(*args, **kwargs)
    try:
        n = int(s)
        if n < 0:
            raise InputNonNegIntException("Число від'ємне",
                                          InputNonNegIntException.ERROR_CODE_NEGATIVE,
                                          s, n)

    except ValueError:
        raise InputNonNegIntException("Число не ціле",
                                      InputNonNegIntException.ERROR_CODE_NOT_INTEGER,
                                      s)
    return n


try:
    s = inputNonNegInt("Введіть ціле невід'ємне число ")
    print(s)
except InputNonNegIntException as err:
    print("InputNonNegIntException")
    print(err.message)
    print("код помилки", err.err_code)
    print(err.orig_value)
    print(err.to_int_converted)
