from MyProjectForGithub.addThread import message_ as m
from MyProjectForGithub.addThread import printlog as p
from MyProjectForGithub.addThread import get_list_thread as get
from MyProjectForGithub.addThread import refresh
from MyProjectForGithub.functions.PascalTriangle.PascalTriangle_cell import cell_
from MyProjectForGithub.functions.PascalTriangle.PascalTriangle_mathOper import numberRank
from MyProjectForGithub.functions.PascalTriangle.PascalTriangle_mathOper import factorial

def main ():
    refresh()
    announce()
    constantGenerate()
    if h == 'back':
        return get()
    triangle(h)
    return get()

def announce():
    p("\nPascal's triangle\n")

def constantGenerate ():
    global h
    while True:
        try:
            h = m('Enter the height of the triangle (starts at zero): ')
            if h == 'back':
                return h
            h = int(h)
            if h < 0:
                p('You must enter a positive number or 0')
                continue
            break
        except ValueError:
            p('Please enter an integer')
        except Exception:
            p('Program error')
    global baseInd
    baseInd = baseIndResult(h)
    global baseIndCoeff
    baseIndCoeff = baseIndCoeffResult(h)

def baseIndCoeff_ (numb):
    baseIndCoeff = numberRank(numb)
    return baseIndCoeff

def bigNumb(n):
    m = n // 2
    return bicoeff(n, m)

def bicoeff (n, m):
    while m <= n:
        nf = factorial(n)
        mf = factorial(m)
        nmf = factorial(n - m)

        bicoeff = int(nf/(mf * nmf))
        return bicoeff

def baseInd_ (baseIndCoeff):
    baseInd = ''
    for i in range(baseIndCoeff):
        baseInd += ' '
    return baseInd

def baseIndResult (h):
    baseIndCoeff = baseIndCoeffResult(h)
    baseInd = baseInd_(baseIndCoeff)
    return baseInd

def baseIndCoeffResult (h):
    func = lambda n: bicoeff(n, n // 2)
    numb = func(h)
    # numb = bigNumb(h)
    baseIndCoeff = baseIndCoeff_(numb)
    return baseIndCoeff

def empty_ (cellNumb, baseInd):
    empty = ''
    for i in range(cellNumb):
        empty += baseInd
    return empty

def triangle (h):
    n = 0
    while n <= h:
        m = 0
        cellNumb = h - n
        # генерируем количество ячеек перед числом
        empty = empty_(cellNumb, baseIndResult(h))
        # принт пустые ячейки
        p(empty, '')
        while m <= n:
            numb = bicoeff(n, m)
            # принт numb
            cell = cell_(baseIndCoeff, numb)
            p(cell, '')
            # принт cell
            p(baseInd, '')
            m += 1
        p()
        n += 1


if __name__ == '__main__':
    main()


