from MyProjectForGithub.addThread import message_ as m
from MyProjectForGithub.addThread import printlog as p
from MyProjectForGithub.addThread import get_list_thread as get
from MyProjectForGithub.addThread import refresh
import MyProjectForGithub.functions.generateData as generateData

parametrs = [
    {
        'message' : 'Enter the amount of the deposit: ',
        'functions' : [generateData.toFloat, generateData.value_more_zero]
    },
    {
        'message' : 'Enter the number of months: ',
        'functions' : [generateData.toInteger, generateData.value_more_zero]
    },
]

def announce():
    p('\nDeposit amount through while\n')

def task3():
    refresh()
    announce()
    parametrList = generateData.generateConstant(parametrs)
    money = parametrList[0]
    month = parametrList[1]
    coeff = 0.07
    i = 0
    if month == 1:
        monthPrint = str(month) + ' month'
    else:
        monthPrint = str(month) + ' months'
    while i < month:
        money += (money * coeff)
        i += 1
    money = round(money, 2)
    p('After  ' + monthPrint + ' the amount of the deposit will be ' + str(money) + ' dollars')
    return get()

if __name__ == '__main__':
    task3()