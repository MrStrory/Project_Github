from message import message_ as m
from message import printlog as p
from message import openlog as ol

def hello ():
    ol('Welcome to the program')
    p('All your actions in the program will be recorded')
    global name
    name = m('Enter your name: ')
    p('Hello ' + name + ' what time is it? (enter the number)')
    try:
        time = int(m())
        if time >= 6 and time <= 11:
            p('Good morning '+name)
        elif time > 11 and time <= 18:
            p('Good day '+name)
        elif time > 18 and time <= 23:
            p('Good evening '+name)
        elif time >= 0 and time < 6:
            p('Well ' + name + " I can't sleep either")
        else:
            p('You entered an incorrect time')
            p('Good time of day ' + name)
    except ValueError:
        p('You entered an incorrect time')
        p('Good time of day ' + name)
    return name

