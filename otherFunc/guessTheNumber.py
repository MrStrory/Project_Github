from MyProjectForGithub.addThread import message_ as m
from MyProjectForGithub.addThread import printlog as p
from MyProjectForGithub.addThread import get_list_thread as get
from MyProjectForGithub.addThread import refresh
import random

def main():
    refresh()
    while True:
        announce()
        act = guessNumb()
        if act == 'back':
            return get()
        if act == 'restart':
            continue
        break
    return get()

def announce ():
    p('\nGuess a number from 1 to 10 in 3 tries\n')

def guessNumb():
    x = random.randint(1, 10)

    for i in range(3):
        try:
            y = input('Enter the number: ')
            if y == 'back':
                return 'back'
            y = int(y)
            if y == x:
                p('You guessed it, this is the number ' + str(x))
                break
            elif x > y:
                p('More')
            else:
                p('Less')
        except ValueError:
            p('Please enter an integer')

    if y != x:
        p("You didn't guess")




if __name__ == '__main__':
    main()