from MyProjectForGithub.addThread import message_ as m
from MyProjectForGithub.addThread import printlog as p
from MyProjectForGithub.addThread import get_list_thread as get
from MyProjectForGithub.addThread import refresh

def main ():
    refresh()
    while True:
        announce()
        act = task8()
        if act == 'back':
            return None
        if act == 'restart':
            continue
        break
    return get()

def announce ():
    p('\nCombining several dictionaries into one\n')
    p('To complete the formation of the dictionary, write - stop')
    p('To complete the formation of all dictionaries, write - stop1\n')

def task8 ():
    data = md.madeDicts()
    if data == 'back':
        return 'back'
    if data == 'restart':
        return 'restart'
    newDict = {}
    for i in data:
        newDict.update(i)
    p(newDict)

if __name__ == '__main__':
    main()