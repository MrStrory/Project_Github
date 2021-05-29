from MyProjectForGithub.addThread import message_ as m
from MyProjectForGithub.addThread import printlog as p
from MyProjectForGithub.addThread import get_list_thread as get
from MyProjectForGithub.addThread import refresh
import MyProjectForGithub.listFunctions.madeDict as md

def main ():
    refresh()
    while True:
        announce()
        act = task10()
        if act == 'back':
            return get()
        if act == 'restart':
            continue
        break
    return get()

def announce ():
    p('\nIf there are identical words, they are displayed in plural\n')
    p('To finish writing words, write - stop\n')

def task10 ():
    data = md.madeListfor10()
    if data == 'back':
        return 'back'
    if data == 'restart':
        return 'restart'
    if len(data) == 0:
        p('no words')
        return None
    set1 = set()
    for i in data:
        if i in set1:
            set1.remove(i)
            elem = i + 's'
            set1.add(elem)
        elif (i + 's') in set1:
            continue
        else:
            set1.add(i)

    p(set1)

if __name__ == '__main__':
    main()
