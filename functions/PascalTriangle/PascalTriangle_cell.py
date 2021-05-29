from MyProjectForGithub.functions.PascalTriangle.PascalTriangle_mathOper import numberRank

def cell_ (baseIndC, numb):
    rank = numberRank(numb)
    findC = fIndC(baseIndC, rank)
    lindC = lIndC(baseIndC, findC, rank)
    find = fInd(findC)
    lind = lInd(lindC)
    cell = find + str(numb) + lind
    return cell

def fIndC (baseIndC, rank):
    fIndC = baseIndC // 2 - rank // 2
    if baseIndC % 2 != 0 and rank % 2 == 0:
        fIndC += 1
    return int(fIndC)

def fInd (fIndC):
    fInd = ''
    for i in range(fIndC):
        fInd += ' '
    return fInd

def lIndC (baseIndC, fIndC, rank):
    lIndC = baseIndC - fIndC - rank
    return int(lIndC)

def lInd (lIndC):
    lInd = ''
    for i in range(lIndC):
        lInd += ' '
    return lInd

if __name__ == '__main__':
    baseIndC = (int(input('Basic indentation factor: ')))
    numb = (int(input('Number: ')))
    print(cell(baseIndC, numb))