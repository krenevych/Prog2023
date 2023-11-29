def parse(p: str):
    p_out = {}
    while True:
        print(p)
        k = p.find('x')
        if p[k+1] == '^':
            deg = p[k+2]
            print(deg)
        if k == -1:
            break
        p = p[k+1:]


    return p_out

parse("x^2-7657x+3")