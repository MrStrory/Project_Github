from MyProjectForGithub.addThread import message_ as m
from MyProjectForGithub.addThread import printlog as p
from MyProjectForGithub.addThread import get_list_thread as get
from MyProjectForGithub.addThread import refresh
import math

def main():
    refresh()
    while True:
        announce()
        act = calc()
        if act == 'back':
            return get()
        if act == 'restart':
            continue
        break
    return get()

def announce ():
    p('\nCalculator\n')
    p('+    addition\n-    subtraction\n*    multiplication\n/    division\nlog  logarithm of the first number to the base of the second'
      '\npow  raising the first number to the power of the second\nlogn decimal logarithm\n!    factorial\nsq   square root of a number\n')

def calc():
    i = 0
    while i < 3:
        try:
            if i == 0:
                n1 = m('Enter the first number: ')
                if n1 == 'back':
                    return 'back'
                if float(n1) % 1 == 0:
                    n1 = int(n1)
                else:
                    n1 = float(n1)
            if i == 1:
                oper = m('Enter operation: ')
                if oper == 'back':
                    i -= 1
                    continue
                if not checkOper(oper):
                    p('Invalid operation')
                    continue
                if oper == 'logn':
                    res = math.log10(n1)
                    p(res)
                    return None
                if oper == '!':
                    res = math.factorial(n1)
                    p(res)
                    return None
                if oper == 'sq':
                    res = math.sqrt(n1)
                    p(res)
                    return None
            if i == 2:
                n2 = m('Enter the second number : ')
                if n2 == 'back':
                    i -= 1
                    continue
                if float(n2) % 1 == 0:
                    n2 = int(n2)
                else:
                    n2 = float(n2)
        except ValueError:
            p('Enter the number')
            continue
        except DeprecationWarning:
            pass
        except:
            p('Program error')
            continue
        i += 1

    if oper == '+':
        res = n1 + n2
    if oper == '-':
        res = n1 - n2
    if oper == '*':
        res = n1 * n2
    if oper == '/':
        if n2 == 0:
            p('cannot be divided by zero')
        else:
            res = n1 / n2
    if oper == 'log':
        res = math.log(n1, n2)
    if oper == 'pow':
        res = math.pow(n1, n2)
    p(res)

def checkOper(oper):
    operations = ['+', '-', '*', '/', 'log', 'logn', '!', 'pow', 'sq']
    for i in operations:
        if oper == i:
            return True
    return False



if __name__ == '__main__':
    main()
