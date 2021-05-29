from MyProjectForGithub.addThread import message_ as m
from MyProjectForGithub.addThread import printlog as p
from MyProjectForGithub.addThread import get_list_thread as get
from MyProjectForGithub.addThread import refresh

def main():
    refresh()
    while True:
        announce()
        task1()
        if back == 'back':
            return get()
        if back == 'restart':
            continue
        break
    return get()

def announce ():
    p('\nList values less than 5\n')
    p('To finish forming the list, write - stop\n')

def task1():
    list = []
    global back
    back = 0
    i = 1
    while True:
        try:
            elem = m('Enter '+str(i)+' list item: ')
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
            elem = int(elem)
            list.append(elem)
            i += 1
        except ValueError:
            p('Input data must be integers only')
        except Exception:
            p('Program error')

    for i in list:
        if i < 5:
            p(i, ' ')

if __name__ == '__main__':
    main()