from MyProjectForGithub.addThread import message_ as m
from MyProjectForGithub.addThread import printlog as p
from MyProjectForGithub.addThread import get_list_thread as get
from MyProjectForGithub.addThread import refresh
import MyProjectForGithub.functions.generateData as generateData

parametrs = [
    {
        'message' : 'Enter the height of the triangle: ',
        'functions' : [generateData.toInteger, generateData.value_more_zero]
    }
]

def announce():
    p('\nTriangle height h\n')

def task9():
    refresh()
    announce()
    parametrList = generateData.generateConstant(parametrs)
    h = parametrList[0]
    j = 1
    ipow = 10
    pow = 1
    baseInd = ' '

    while h >= ipow:
        ipow *= 10
        pow += 1
        baseInd += ' '

    while j <= h:
        coeff = 0
        ipow = pow
        while j < 10 ** ipow:
            coeff += 1
            ipow -= 1
        k = 1
        while k <= (h - j):
            p(baseInd, '')
            k += 1
        l = 1
        while l <= j:
            ind = ''
            if coeff == 1:
                p(j, '')
            else:
                i = 1
                while i < coeff - 1:
                    ind += ' '
                    i += 1
                p(ind + ' ' + str(j), '')
            l += 1
        p()
        j += 1
    return get()

if __name__ == '__main__':
    task9()