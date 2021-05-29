from message import message_ as m
from message import printlog as p
import time

def timeStart():
    time_ = 5
    for i in range(time_):
        if i != 0:
            p(str(time_))
        else:
            p('Launching the program through:\n' + str(time_))
        time.sleep(1)
        time_ -= 1

def timeEnd():
    time_ = 5
    for i in range(time_):
        if i != 0:
            p(str(time_))
        else:
            p('The end of the program in:\n' + str(time_))
        time.sleep(1)
        time_ -= 1

def bye(name):
    p(name + ' thank you for being with us')

if __name__ == '__main__':
    timeEnd()





