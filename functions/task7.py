from MyProjectForGithub.addThread import message_ as m
from MyProjectForGithub.addThread import printlog as p
from MyProjectForGithub.addThread import get_list_thread as get
from MyProjectForGithub.addThread import refresh
import MyProjectForGithub.functions.generateData as generateData

parametrs = [
    {
        'message' : 'Enter the number: ',
        'functions' : [generateData.toInteger]
    },
    {
        'message' : 'Enter step: ',
        'functions' : [generateData.toInteger]
    },
    {
        'message' : 'Enter limit: ',
        'functions' : [generateData.toInteger]
    }
]

def announce():
    p('\nArithmetic progression\n')

def task7():
    refresh()
    announce()
    parametrList = generateData.generateConstant(parametrs)
    numb = parametrList[0]
    step = parametrList[1]
    limit = parametrList[2]

    if step > 0 and numb > limit:
        p('the number cannot be more than the limit with a positive step')
    if step < 0 and numb < limit:
        p('the number cannot be less than the limit with a negative step')

        if step > 0:
            for i in range(numb, (limit + 1), step):
                p(i, ' ')
        elif step < 0:
            for i in range(numb * -1, (limit * -1) + 1, step * -1):
                p(str(i * -1), ' ')
        else:
            p('Endless row ' + str(numb))

    return get()

if __name__ == '__main__':
    task7()