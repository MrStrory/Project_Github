from MyProjectForGithub.addThread import message_ as m
from MyProjectForGithub.addThread import printlog as p
from MyProjectForGithub.addThread import get_list_thread as get
from MyProjectForGithub.addThread import refresh
import MyProjectForGithub.functions.generateData as generateData

parametrs = [
    {
        'message' : 'Enter the first number: ',
        'functions' : [generateData.toInteger]
    },
    {
        'message' : 'Enter the second number: ',
        'functions' : [generateData.toInteger]
    }
]

def announce():
    p('\nMultiplication of two numbers\n')

def task6(name):
    refresh()
    announce()
    p(name + ' enter 2 numbers and the program will multiply them')
    while True:
        parametrList = generateData.generateConstant(parametrs)
        numb1 = parametrList[0]
        numb2 = parametrList[1]

        res = numb1 * numb2
        p('The result of the multiplication: ' + str(res))
        next = m('To complete the execution write back\nPress any key to continue: ')
        if next == 'back':
            break
    return get()

if __name__ == '__main__':
    task6(name = 'please')