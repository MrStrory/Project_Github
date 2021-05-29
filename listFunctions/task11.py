from MyProjectForGithub.addThread import message_ as m
from MyProjectForGithub.addThread import printlog as p
from MyProjectForGithub.addThread import get_list_thread as get
from MyProjectForGithub.addThread import refresh
import MyProjectForGithub.listFunctions.madeDict as md

def main():
    refresh()
    while True:
        announce()
        act = task11()
        if act == 'back':
            return None
        if act == 'restart':
            continue
        break
    return get()

def announce ():
    p('\nWandering in the hotel\n')
    p('To complete the formation of the route  - stop\n')

def task11():
    data = md.madeListFor11()
    if data == 'back':
        return 'back'
    if data == 'restart':
        return 'restart'
    if len(data) == 0:
        p('no route')
        return None

    for step in range(len(data) - 1):
        if data[step] == 'h':
            if data[step + 1] == '1' or data[step + 1] == '2' or data[step + 1] == '3' or data[step + 1] == '4':
                continue
            p('Your route is not possible')
            p(data)
            return None
        if data[step] == '1' or data[step] == '2' or data[step] == '3' or data[step] == '4':
            if data[step + 1] == 'h':
                continue
            p('Your route is not possible')
            p(data)
            return None

    p('Your route is built')
    p(data)
    return None

if __name__ == '__main__':
    main()