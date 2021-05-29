from MyProjectForGithub.addThread import message_ as m
from MyProjectForGithub.addThread import printlog as p

def generateConstant(parametrs):
    n = len(parametrs)
    parametrList = []
    i = 0
    back = 0
    while i < n:
        x = m(parametrs[i]['message'])
        if x == 'back':
            back += 1
            if back == 3:
                back = backStep3x()
                if back == 'restart' or back == 'back':
                    return back
            if i > 0:
                del parametrList[-1]
                i -= 1
                continue
            else:
                return 'back'
        back = 0

        for func in parametrs[i]['functions']:
            x = func(x)
            if x == 'error':
                break
        if x == 'error':
            continue
        parametrList.append(x)
        i += 1
    return parametrList

def value_more_or_equal_zero(value):
    if value <= 0:
        p('The number must be greater than zero')
        return 'error'
    return value

def value_more_zero(value):
    if value < 0:
        p('The number must be greater than zero')
        return 'error'
    return value

def toInteger(value):
    try:
        value = int(value)
    except ValueError:
        p('Please enter an integer')
        return 'error'
    except:
        p('Program error')
        return 'error'
    return value

def toFloat(value):
    try:
        value = float(value)
    except ValueError:
        p('Please enter the number')
        return 'error'
    except:
        p('Program error')
        return 'error'
    return value

def backStep3x():
    back = m('\nPress to continue - 1\n'
             'Press to restart the operation - 2\n'
             'Press any key to enter the Menu : ')
    if back == '2':
        back = 'restart'
        return back  # restart
    if back != '1':
        back = 'back'
        return back  # exit to the menu
    return 0