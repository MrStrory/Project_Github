def numberRank (numb):
    rank = 1
    while numb >= (10 ** rank):
        rank += 1
    return rank

def factorial (numb):
    if numb == 0:
        f = 1
    else:
        i = 1
        f = 1
        while i <= numb:
            f *= i
            i += 1
    return f