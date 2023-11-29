
def getSum(file_name):
    with open(file_name) as f:
        lst = [float(el) for el in f.read().split()]
        return sum(lst)

if __name__ == '__main__':
    suma = getSum("input02.txt")
    print(suma)