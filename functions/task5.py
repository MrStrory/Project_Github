from MyProjectForGithub.addThread import message_ as m
from MyProjectForGithub.addThread import printlog as p
from MyProjectForGithub.addThread import get_list_thread as get
from MyProjectForGithub.addThread import refresh
import MyProjectForGithub.functions.generateData as generateData

parametrs = [
    {
        'message' : 'Multiplication table for n-digit numbers, where n = ',
        'functions' : [generateData.toInteger, generateData.value_more_zero]
    }
]


def announce():
    p('\nMultiplication table\n')

def task5():
    refresh()
    announce()
    parametrList = generateData.generateConstant(parametrs)
    number = parametrList[0]
    pow = number * 2

    limit = 10 ** number

    for j in range(1, limit):
        for i in range(1, limit):
            ind = ''
            coeff = 0
            b = pow - 1
            while (j * i) < 10 ** b:
                coeff += 1
                b -= 1
            for a in range(coeff):
                ind += ' '
            p(ind + ' ' + str(j * i), end=' ')
        p()
    return get()

if __name__ == '__main__':
    task5()