from message import append_thredList
import oop.t1
import oop.t4
import otherFunc.calc as calc
import otherFunc.guessTheNumber as gn
import otherFunc.bSearch as bs
import analys as end
from message import message_ as m
from message import printlog as p
import info
# from functions import task1, task2
from functions.task1 import main as task1
from functions.task2 import main as task2
from functions.task3 import task3
from functions.task4 import task4
from functions.task5 import task5
from functions.task6 import task6
from functions.task7 import task7
from functions.task8 import task8
from functions.task9 import task9
from functions.task10 import task10
from functions.task11 import task11
from functions.task12 import main as task12
import listFunctions.task1 as lf1
import listFunctions.task2 as lf2
import listFunctions.task3 as lf3
import listFunctions.task4 as lf4
import listFunctions.task5 as lf5
import listFunctions.task6 as lf6
import listFunctions.task7 as lf7
import listFunctions.task8 as lf8
import listFunctions.task9 as lf9
import listFunctions.task10 as lf10
import listFunctions.task11 as lf11

def operations (name):
    threadList = []
    p('\nHow can I help you?')
    while True:
        operation = ''
        p('To work with math operations, click - 1')
        p('To work with lists, click - 2')
        p('For other operations, click - 3')
        p('for the finish - 0')
        operChoice = m('')
        if operChoice == '0' or operChoice == 'back':
            end.ending()
            return None
        elif operChoice == '1':
            while True:
                if operation == 'back':
                    break
                p('\nFor information write info')
                operation = m('Enter the number of the operation you want to perform: ')
                p()
                while True:
                    if operation == 'back':
                        break
                    if operation == '0':
                        end.ending()
                        return None
                    if operation == 'info':
                        info.info()
                        break
                    elif operation == '1':
                        threadList = task1()
                    elif operation == '2':
                        threadList = task2()
                    elif operation == '3':
                        threadList = task3()
                    elif operation == '4':
                        threadList = task4()
                    elif operation == '5':
                        threadList = task5()
                    elif operation == '6':
                        threadList = task6(name)
                    elif operation == '7':
                        threadList = task7()
                    elif operation == '8':
                        threadList = task8()
                    elif operation == '9':
                        threadList = task9()
                    elif operation == '10':
                        threadList = task10()
                    elif operation == '11':
                        threadList = task11()
                    elif operation == '12':
                        threadList = task12()
                    else:
                        p('\n'+name + ' you entered an incorrect value, check the correctness of the command\n')
                        break
                    append_thredList(threadList)
                    nextStep = m('\nTo end the program press - 0'
                                     '\nTo repeat the operation - 1'
                                     '\nExit to the menu - 2 (or any other key)\n')
                    p()
                    if nextStep == '0':
                        end.ending()
                        return None
                    if nextStep == '1':
                        continue
                    break
        elif operChoice == '2':
            while True:
                if operation == 'back':
                    break
                p('\nFor information write info')
                operation = m('Enter the number of the operation you want to perform: ')
                p()
                while True:
                    if operation == 'back':
                        break
                    elif operation == '0':
                        end.ending()
                        return None
                    elif operation == 'info':
                        info.listInfo()
                        break
                    elif operation == '1':
                        threadList = lf1.main()
                    elif operation == '2':
                        threadList = lf2.main()
                    elif operation == '3':
                        threadList = lf3.main()
                    elif operation == '4':
                        threadList = lf4.main()
                    elif operation == '5':
                        threadList = lf5.main()
                    elif operation == '6':
                        threadList = lf6.main()
                    elif operation == '7':
                        threadList = lf7.main()
                    elif operation == '8':
                        threadList = lf8.main()
                    elif operation == '9':
                        threadList = lf9.main()
                    elif operation == '10':
                        threadList = lf10.main()
                    elif operation == '11':
                        threadList = lf11.main()
                    else:
                        p('\n'+name + ' you entered an incorrect value, check the correctness of the command\n')
                        break
                    append_thredList(threadList)
                    nextStep = m('\nTo end the program press - 0'
                                     '\nTo repeat the operation - 1'
                                     '\nExit to the menu - 2 (or any other key )\n')
                    p()
                    if nextStep == '0':
                        end.ending()
                        return None
                    if nextStep == '1':
                        continue
                    break
        elif operChoice == '3':
            while True:
                if operation == 'back':
                    break
                p('\nFor information write info')
                operation = m('Enter the number of the operation you want to perform: ')
                p()
                while True:
                    if operation == 'back':
                        break
                    elif operation == '0':
                        end.ending()
                        return None
                    elif operation == 'info':
                        info.otherInfo()
                        break
                    elif operation == '1':
                        threadList = calc.main()
                    elif operation == '2':
                        threadList = gn.main()
                    elif operation == '3':
                        threadList = bs.main()
                    elif operation == '4':
                        threadList = oop.t1.creature()
                    elif operation == '5':
                        threadList = oop.t4.main()
                    else:
                        p('\n'+name + ' you entered an incorrect value, check the correctness of the command\n')
                        break
                    append_thredList(threadList)
                    nextStep = m('\nPress to end the program - 0'
                                     '\nTo repeat the operation - 1'
                                     '\nExit to the menu - 2 (or any other key)\n')
                    p()
                    if nextStep == '0':
                        end.ending()
                        return None
                    if nextStep == '1':
                        continue
                    break
        else:
            p('\n'+name + ' you entered an incorrect value, check the correctness of the command\n')