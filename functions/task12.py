from MyProjectForGithub.addThread import message_ as m
from MyProjectForGithub.addThread import printlog as p
from MyProjectForGithub.addThread import get_list_thread as get
from MyProjectForGithub.addThread import refresh
import MyProjectForGithub.functions.generateData as generateData
from MyProjectForGithub.functions.PascalTriangle.PascalTriangle_mathOper import numberRank

parametrs = [
    {
        'message' : 'Enter the number: ',
        'functions' : [generateData.toInteger, generateData.value_more_zero]
    }
]

def main():
    refresh()
    announce()
    parametrList = generateData.generateConstant(parametrs)
    if parametrList == 'back':
        return get()
    res = result(parametrList[0])
    display(res)
    return get()

def announce():
    p('\nThe sum of the extreme digits of the number\n')

def display(res):
    p(res)

def result(numb):
    rank = numberRank(numb)
    pow = rank - 1
    i = int(rank // 2 + rank % 2)
    summ = 0

    for j in range(i):
        if j > 0:
            numb %= 10 ** pow
            numb //= 10
            pow -= 2
        if pow == 0:
            summ += numb
            break
        n1 = numb // 10 ** pow
        n2 = numb % 10
        result = n1 * 10 + n2
        summ += result
    return summ

if __name__ == '__main__':
    main()

