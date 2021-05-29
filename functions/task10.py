from MyProjectForGithub.addThread import message_ as m
from MyProjectForGithub.addThread import printlog as p
from MyProjectForGithub.addThread import get_list_thread as get
from MyProjectForGithub.addThread import refresh
import MyProjectForGithub.functions.generateData as generateData

parametrs = [
    {
        'message' : 'Enter the number of Fibonacci numbers: ',
        'functions' : [generateData.toInteger, generateData.value_more_zero]
    }
]

def announce():
    p('\nFibonacci numbers\n')

def task10():
    refresh()
    announce()
    numb1 = 0
    numb2 = 1

    parametrList = generateData.generateConstant(parametrs)
    limit = parametrList[0]

    if limit == 1:
        p(numb1)
    elif limit == 2:
        p(str(numb1) + ' ' + str(numb2))
    elif limit > 2:
        p(str(numb1) + ' ' + str(numb2), ' ')
        for i in range(limit - 2):
            fib = numb1 + numb2
            p(fib, ' ')
            numb1 = numb2
            numb2 = fib
    return get()

if __name__ == '__main__':
    task10()