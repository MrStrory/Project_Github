from MyProjectForGithub.addThread import message_ as m
from MyProjectForGithub.addThread import printlog as p
from MyProjectForGithub.addThread import get_list_thread as get
from MyProjectForGithub.addThread import refresh
import time

class GateValve:
    state = None
    time = 5

    def __init__(self, state, time):
        self.state = state
        self.time = time

    def openValve(self):
        p('The valve is being opened')
        time.sleep(self.time)
        if self.state == 1:
            p('error the valve is already open')
        else:
            self.state = 1
            p('Valve successfully opened ')

    def closeValve(self):
        p('The valve is being closed')
        time.sleep(self.time)
        if self.state == 0:
            p('The valve is already closed ')
        else:
            self.state = 0
            p('Valve closed successfully')

    def checkState(self):
        if self.state == 0 or self.state == 1:
            return None

def creature():
    refresh()
    p('Gate valve')
    p('To complete the operation write stop')
    valve = GateValve(1, 3)
    while True:
        state = m('Click to open - 1\nTo close press - 0\n')
        if state == 'stop':
            return get()
        if state != '0' and state != '1':
            p('wrong operation')
            continue
        state = int(state)
        if state == 1:
            valve.openValve()
        else:
            valve.closeValve()
