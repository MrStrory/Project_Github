from MyProjectForGithub.addThread import message_ as m
from MyProjectForGithub.addThread import printlog as p
from MyProjectForGithub.addThread import get_list_thread as get
from MyProjectForGithub.addThread import refresh


def main():
    refresh()
    while True:
        announce()
        act = inpNum()
        if act == 'back':
            return get()
        if act == 'restart':
            continue
        break
    return get()

def announce():
    p('\nBinary search\n')

def inpNum():
    try:
        numb = m('Please enter a number between 1 and 100: ')
        if numb == 'back':
            return 'back'
        numb = int(numb)
        if numb < 1:
            p('the number must be greater than 1')
        if numb > 100:
            p('The number must be less than 100')
    except ValueError:
        p('Please enter an integer')
    except:
        p('Program error')

    res = BinarySearch(numb)
    p(res)

def BinarySearch(val, lys=range(1, 100)):
    first = 0
    last = len(lys) - 1
    index = -1
    while (first <= last) and (index == -1):
        mid = (first + last) // 2
        if lys[mid] == val:
            index = mid
        else:
            if val < lys[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return index


if __name__ == '__main__':
    main()