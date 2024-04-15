from t08 import InputNonNegIntException, InputNonIntException, InputNegException
def inputNonNegInt(*args, **kwargs):
    """ функція введення з клавіатури лише невід’ємних цілих чисел."""
    s = input(*args, **kwargs)
    try:
        n = int(s)
        if n < 0:
            raise InputNegException("Число від'ємне", s, n)

    except ValueError:
        raise InputNonIntException("Число не ціле", s)
    return n


try:
    s = inputNonNegInt("Введіть ціле невід'ємне число ")
    print(s)
# except InputNonNegIntException as err:
#     print(err)
except InputNegException as err:
    print(err)
    print(abs(err.to_int_converted))
except InputNonIntException as err:
    print(err)
    print("Введіть ціле число")
