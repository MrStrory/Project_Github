from MyProjectForGithub.addThread import message_ as m
from MyProjectForGithub.addThread import printlog as p
from MyProjectForGithub.addThread import get_list_thread as get
from MyProjectForGithub.addThread import refresh
import MyProjectForGithub.listFunctions.madeDict as md

def main ():
    refresh()
    while True:
        announce()
        act = task7()
        if act == 'back':
            return get()
        if act == 'restart':
            continue
        break
    return get()

def announce ():
    p('\nSorting a dictionary by value\n')
    p('To complete the formation of the dictionary, write - stop\n')

def task7 ():
    data = md.madeDict()
    if data == 'back':
        return 'back'
    if data == 'restart':
        return 'restart'
    dict1 = data[0]
    sort = data[1]
    newList = []
    for i in dict1.items():
        j = 0
        while j < len(newList):
            if sort == '1':
                if i[1] < newList[j][1]: # > - Для обратного порядка
                    newList.insert(j, (i[0], i[1]))
                    break
            else:
                if i[1] > newList[j][1]: # > - Для обратного порядка
                    newList.insert(j, (i[0], i[1]))
                    break
            j += 1
        if j == len(newList):
            newList.append((i[0], i[1]))
    dict1 = dict(newList)
    p(dict1)

if __name__ == '__main__':
    main()