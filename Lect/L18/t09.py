def readFile(file_name):
    try:
        with open(file_name) as f:
            a = f.read()
            d = int(a)
            print(d)

    except FileNotFoundError as err:
        print("файл не існує", err.filename)

readFile("input2.txt")