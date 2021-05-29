from MyProjectForGithub.addThread import message_ as m
from MyProjectForGithub.addThread import printlog as p
from MyProjectForGithub.addThread import get_list_thread as get
from MyProjectForGithub.addThread import refresh

def main():
    refresh()
    while True:
        announce()
        task2()
        if back == 'back':
            return get()
        if back == 'restart':
            continue
        break
    return get()

def announce ():
    p('\nDisplaying the same list items\n')
    p('To finish forming the list, write - stop\n')


def task2 ():
    global back
    back = 0
    iForList = 0
    list1 = []
    list2 = []
    lists = [list1, list2]
    while iForList < 2:
        iForElem = len(lists[iForList])
        while True:
            try:
                elem = m('Enter '+str(iForElem + 1)+' list item '+str(iForList + 1)+': ')
                if elem == 'stop':
                    iForList += 1
                    break
                if elem == 'back':
                    if len(lists[iForList]) > 0:
                        back += 1
                        if back == 3:
                            back = m('\nClick to continue - 1\n'
                                     'Press to restart the operation - 2\n'
                                     'Press any key to enter the Menu: ')
                            if back == '1':
                                back = 0
                                del lists[iForList][-1]
                                iForElem -= 1
                                continue
                            if back == '2':
                                back = 'restart'
                                return None
                            back = 'back'
                            return None
                        else:
                            del lists[iForList][-1]
                            iForElem -= 1
                            continue
                    else:
                        if iForList > 0:
                            back += 1
                            if back == 3:
                                back = m('\nClick to continue - 1\n'
                                         'Press to restart the operation - 2\n'
                                         'Press any key to enter the Menu: ')
                                if back == '1':
                                    back = 0
                                    iForList -= 1
                                    break
                                if back == '2':
                                    back = 'restart'
                                    return None
                                back = 'back'
                                return None
                            iForList -= 1
                            break
                        else:
                            back = 'back'
                            return None
                back = 0
                lists[iForList].append(elem)
                iForElem += 1
            except Exception:
                p('Program error')

    res = []
    for i in list1:
        for j in list2:
            if i == j:
                if res.count(i) < 1:
                    res.append(i)
    p(res)

if __name__ == '__main__':
    main()