from MyProjectForGithub.addThread import message_ as m
from MyProjectForGithub.addThread import printlog as p
from MyProjectForGithub.addThread import get_list_thread as get
from MyProjectForGithub.addThread import refresh
import MyProjectForGithub.functions.generateData as generateData

parametrs = [
    {
        'message' : 'Enter the number you want to tetrate: ',
        'functions' : [generateData.toInteger]
    },
    {
        'message' : 'Enter the degree of tetration: ',
        'functions' : [generateData.toInteger, generateData.value_more_zero]
    }
]

def announce():
    p('\nNumber tetration\n')

def task11():
    refresh()
    announce()
    parametrList = generateData.generateConstant(parametrs)
    numb = parametrList[0]
    tetration = parametrList[1]
    res = numb
    for i in range(1, tetration):
        pow = numb ** res
        res = pow
    p(res)
    return get()

if __name__ == '__main__':
    task11()