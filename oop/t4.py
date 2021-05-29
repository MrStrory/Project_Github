from MyProjectForGithub.addThread import message_ as m
from MyProjectForGithub.addThread import printlog as p
from MyProjectForGithub.addThread import get_list_thread as get
from MyProjectForGithub.addThread import refresh

class Books:
    def __init__(self, shelf):
        self.shelf = shelf

    def __del__(self):
        p('Shelf removed')

    def takeBook(self, book):
        for name in self.shelf:
            if name[0] == book:
                if name[-1] > 0:
                    name.append(name[-1] - 1)
                    for i in name:
                        p(str(i) + '  ', end='')
                    p()
                    return None
                else:
                    p('these books have already been taken apart')
                    return None
        p('there is no such book')

    def returnBook(self, book):
        for name in self.shelf:
            if name[0] == book:
                if name[1] == name[-1]:
                    p('The collection of these books is complete')
                    return None
                else:
                    name.append(name[-1] + 1)
                    for i in name:
                        p(str(i) + '  ', end='')
                    p()
                    return None
        p('there is no such book')

    def disShelf(self):
        for i in self.shelf:
            for j in i:
                p(str(j) + '  ', end='')
            p()


def main():
    refresh()
    p('Bookshelf')
    p('to finish forming the shelf write stop')
    shelf_ = madeDict()
    shelf = Books(shelf_)
    p('\nTo complete the operation - stop')
    while True:
        act = m('For taking - 1\nTo return - 2\n')
        if act == 'stop':
            break
        if act !='1' and act != '2':
            m('Input Error')
            continue
        if act == '1':
            title = m('Enter the title of the book you want to borrow: ')
            shelf.takeBook(title)
            continue
        if act == '2':
            title = m('Enter the title of the book you want to return: ')
            shelf.returnBook(title)
            continue
    return get()


def madeDict ():
    list = []
    ielem = 0
    back = 0
    i = 0
    while True:   # цикл создания списка
        while i < 2:   # цикл создания ячейки
            try:
                if i == 0:
                    key = m('enter title ' + str(ielem + 1) + ' of book: ')
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
                    value = m('enter quantity ' + str(ielem + 1) + ' of books: ')
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
                continue
            i += 1
        if key == 'stop' or value == 'stop':
            break
        cell = [key, value]
        list.append(cell)
        ielem += 1
        i = 0
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
            p('title must be unique')
            return True
    return False


