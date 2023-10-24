def mostFreqDig(a):
    freq = [0]*10
    while a > 0:
        d = a % 10
        freq[d] += 1
        a //= 10

    print(freq)
    max_num = -1
    max_count = -1
    for i, el in enumerate(freq):
        if el > max_count:
            max_count = el
            max_num = i

    return max_num, max_count


############### main program ############
num, count = mostFreqDig(1235322430043)
print(num, count)
