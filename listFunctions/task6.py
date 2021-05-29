from MyProjectForGithub.addThread import message_ as m
from MyProjectForGithub.addThread import printlog as p
from MyProjectForGithub.addThread import get_list_thread as get
from MyProjectForGithub.addThread import refresh

def main ():
    refresh()
    while True:
        announce()
        task6()
        if back == 'back':
            return get()
        if back == 'restart':
            continue
        break
    return get()

def announce ():
    p('List items one by one\n')
    p('To finish forming the list, write - stop\n')

def task6 ():
    list = []
    global back
    back = 0
    i = 1
    while True:
        try:
            elem = m('Enter ' + str(i) + ' list item: ')
            if elem == 'stop':
                break
            if elem == 'back':
                if len(list) > 0:
                    back += 1
                    if back == 3:
                        back = m('\nClick to continue - 1\n'
                                 'Press to restart the operation - 2\n'
                                 'Press any key to enter the Menu: ')
                        if back == '1':
                            back = 0
                            del list[-1]
                            i -= 1
                            continue
                        if back == '2':
                            back = 'restart'
                            return None
                        back = 'back'
                        return None
                    else:
                        del list[-1]
                        i -= 1
                        continue
                else:
                    back = 'back'
                    return None
            back = 0
            list.append(elem)
            i += 1
        except Exception:
            p('Program error')

    for i in range(0, len(list), 2):
        print(list[i], ' ')

if __name__ == '__main__':
    main()