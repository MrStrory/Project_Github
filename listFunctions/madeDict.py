from MyProjectForGithub.addThread import message_ as m
from MyProjectForGithub.addThread import printlog as p
from MyProjectForGithub.addThread import get_list_thread as get
from MyProjectForGithub.addThread import refresh
import copy

def madeDict ():
    list = []
    ielem = 0
    back = 0
    i = 0
    while True:   # цикл создания списка
        while i < 2:   # цикл создания ячейки
            try:
                if i == 0:
                    key = m('enter key ' + str(ielem + 1) + ' of element: ')
                    if key == 'back':
                        back += 1
                        if len(list) == 0:
                            back = 'back'
                            return back
                        if back == 3:
                            back = backStep3x()
                            if back == 'restart':
                                return back  # перезапуск
                            if back == 'back':
                                return back  # выход в меню
                            back = 0
                        ielem -= 1
                        key = list[-1][0]
                        del list[-1]
                        i = 1
                        continue
                    back = 0
                    if key == 'stop':
                        break
                    if uniqCheck(key, list):
                        continue
                if i == 1:
                    value = m('enter value ' + str(ielem + 1) + ' of element: ')
                    if value == 'back':
                        back += 1
                        if back == 3:
                            back = backStep3x()
                            if back == 'restart':
                                return back # перезапуск
                            if back == 'back':
                                return back # выход в меню
                            back = 0
                        i = 0
                        continue
                    if value == 'stop':
                        break
                    value = int(value)
                    back = 0
            except ValueError:
                p('\nValues must be integers\n')
                continue
            except Exception:
                p('\nProgram error\n')
            i += 1
        if key == 'stop' or value == 'stop':
            while True:
                sort = m('\nTo sort in ascending order, click - 1\n'
                             'To sort in descending order, click - 2\n')
                if sort == 'back':
                    if len(list) == 0:
                        i = 0
                        break
                    key = list[-1][0]
                    del list[-1]
                    i = 1
                    back += 1
                    ielem -= 1
                    break
                if sort != '1' and sort != '2':
                    p('you entered an invalid value')
                    continue
                break
            if sort == 'back':
                continue
            break
        cell = [key, value]
        list.append(cell)
        ielem += 1
        i = 0

    dict1 = dict(list)
    return [dict1, sort]

def madeDicts ():
    lists = []
    list = []
    ielem = 0
    ilist = 0
    back = 0
    i = 0
    while True:  # цикл создания списка списков
        while True:  # цикл создания списка
            while i < 2:  # цикл создания ячейки
                try:
                    if i == 0:
                        key = m('enter key ' + str(ielem + 1) + ' of element ' + str(ilist + 1) + ' of dictionary: ')
                        if key == 'back':
                            back += 1
                            if len(list) == 0:
                                if len(lists) == 0:
                                    back = 'back'
                                    return back
                                key = lists[-1][-1][0]
                                list = lists[-1]
                                del lists[-1]
                                del list[-1]
                                ilist = len(lists)
                                ielem = len(list)
                                i = 1
                                continue
                            if back == 3:
                                back = backStep3x()
                                if back == 'restart':
                                    return back  # перезапуск
                                if back == 'back':
                                    return back  # выход в меню
                                back = 0
                            ielem -= 1
                            key = list[-1][0]
                            del list[-1]
                            i = 1
                            continue
                        back = 0
                        if key == 'stop' or key == 'stop1':
                            break
                        if uniqCheck(key, list):
                            continue
                    if i == 1:
                        value = m('enter value ' + str(ielem + 1) + ' of element ' + str(ilist + 1) + ' of dictionary: ')
                        if value == 'back':
                            back += 1
                            if back == 3:
                                back = backStep3x()
                                if back == 'restart':
                                    return back  # перезапуск
                                if back == 'back':
                                    return back  # выход в меню
                                back = 0
                            i = 0
                            continue
                        if value == 'stop' or 'stop1':
                            break
                        back = 0
                except Exception:
                    p('\nProgram error\n')
                i += 1
            if key == 'stop' or value == 'stop' or key == 'stop1' or value == 'stop1':
                dict1 = copy.deepcopy(list)
                list = []
                lists.append(dict1)
                ielem = 0
                ilist += 1
                i = 0
                break
            cell = [key, value]
            list.append(cell)
            ielem += 1
            i = 0
        if key == 'stop1' or value == 'stop1':
            break
    dictlist = []
    for i in lists:
        dict1 = dict(i)
        dictlist.append(dict1)
    p(dictlist[0])
    p(dictlist[1])
    p(dictlist[2])

    return dictlist

def madeDictfor9 ():
    list = []
    ielem = 0
    back = 0
    i = 0
    while True:   # цикл создания списка
        while i < 2:   # цикл создания ячейки
            try:
                if i == 0:
                    key = m('enter key ' + str(ielem + 1) + ' of element: ')
                    if key == 'back':
                        back += 1
                        if len(list) == 0:
                            back = 'back'
                            return back
                        if back == 3:
                            back = backStep3x()
                            if back == 'restart':
                                return back  # перезапуск
                            if back == 'back':
                                return back  # выход в меню
                            back = 0
                        ielem -= 1
                        key = list[-1][0]
                        del list[-1]
                        i = 1
                        continue
                    back = 0
                    if key == 'stop':
                        break
                    if uniqCheck(key, list):
                        continue
                if i == 1:
                    value = m('enter value ' + str(ielem + 1) + ' of element: ')
                    if value == 'back':
                        back += 1
                        if back == 3:
                            back = backStep3x()
                            if back == 'restart':
                                return back # перезапуск
                            if back == 'back':
                                return back # выход в меню
                            back = 0
                        i = 0
                        continue
                    if value == 'stop':
                        break
                    value = int(value)
                    back = 0
            except ValueError:
                p('\nValues must be integers\n')
                continue
            except Exception:
                p('\nProgram error \n')
            i += 1
        if key == 'stop' or value == 'stop':
            break
        cell = [key, value]
        list.append(cell)
        ielem += 1
        i = 0
    dict1 = dict(list)
    return dict1

def madeListfor10 ():
    list = []
    back = 0
    i = 1
    while True:
        try:
            elem = m('Enter ' + str(i) + '  word: ')
            if elem == 'stop':
                break
            if elem == 'back':
                if len(list) > 0:
                    back += 1
                    if back == 3:
                        if back == 3:
                            back = backStep3x()
                            if back == 'restart':
                                return back # перезапуск
                            if back == 'back':
                                return back # выход в меню
                            back = 0
                    del list[-1]
                    i -= 1
                    continue
                else:
                    back = 'back'
                    return back
            back = 0
            try:
                elem = int(elem)
                elem = float(elem)
                p('Input data cannot be numbers')
                continue
            except ValueError:
                list.append(elem)
                i += 1
            finally:
                continue
        except Exception:
            p('Program error')
    return list

def madeListFor11():
    list = []
    value = ['1', '2', '3', '4', 'h']
    back = 0
    i = 1
    while True:
        try:
            elem = m('Enter '+str(i)+' route element: ')
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
                            return back
                        back = 'back'
                        return back
                    else:
                        del list[-1]
                        i -= 1
                        continue
                else:
                    back = 'back'
                    return back
            elem = elem.lower()
            def check(elem):
                for j in value:
                    if elem == j:
                        return True
                return False

            if not check(elem):
                p('You entered an invalid value')
                continue

            back = 0
            list.append(elem)
            i += 1
        except Exception:
            p('Program error')

    return list

def backStep3x ():
    back = m('\nClick to continue - 1\n'
             'Press to restart the operation - 2\n'
             'Press any key to enter the Menu: ')
    if back == '2':
        back = 'restart'
        return back  # перезапуск
    if back != '1':
        back = 'back'
        return back  # выход в меню

def uniqCheck (key, list):
    for i in list:
        if key == i[0]:
            p('keys must be unique')
            return True
    return False