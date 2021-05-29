from MyProjectForGithub.addThread import message_ as m
from MyProjectForGithub.addThread import printlog as p
from MyProjectForGithub.addThread import get_list_thread as get
from MyProjectForGithub.addThread import refresh
import MyProjectForGithub.listFunctions.madeDict as md

def main ():
    refresh()
    while True:
        announce()
        act = task9()
        if act == 'back':
            return get()
        if act == 'restart':
            continue
        break
    return get()

def announce ():
    p('\Displaying the three largest dictionary values\n')
    p('To complete the formation of the dictionary, write - stop\n')

def task9 ():
    data = md.madeDictfor9()
    if data == 'back':
        return 'back'
    if data == 'restart':
        return 'restart'
    newList = []
    for i in data.items():
        j = 0
        while j < len(newList):
            if i[1] > newList[j][1]:
                if len(newList) == 3:
                    newList.insert(j, (i[0], i[1]))
                    newList.pop(3)
                else:
                    newList.insert(j, (i[0], i[1]))
                break
            j += 1
        if len(newList) == 0:
            newList.append((i[0], i[1]))
    p(newList)

if __name__ == '__main__':
    main()