from message import message_ as m
from message import printlog as p


def info ():
    p('1  - Population size\n2  - Population size (complicated)\n'
          '3  - Deposit amount through while\n4  - Deposit amount through for\n5  - Multiplication table\n'
          '6  - Multiplication of two numbers\n7  - Arithmetic progression\n'
          "8  - Pascal's triangle\n9  - Triangle height h\n10 - Fibonacci numbers\n"
          '11 - Number tetration\n12 - The sum of the extreme digits of the number\n\n'
          '0  - Exit the program\nback - Take a step back')

def listInfo ():
    p('1  - List values less than 5\n2  - Common values of two lists\n3  - The first and last elements of the list\n'
          '4  - Even list values no further than 237\n5  - Elements of the first list that are not in the second'
          '\n6  - Iterating over the list through 1 element\n'
          '7  - Sorting a dictionary by value\n8  - Combining several dictionaries into one\n'
          '9  - Displaying the three largest dictionary values\n10 - If there are identical words, they are displayed in plural\n\n'
          '0  - Exit the program\nback - Take a step back')

def otherInfo ():
    p('1 - Calculator\n2 - Guess the number\n3 - Binary search\n4 - Gate valve\n5 - Bookshlef')

if __name__ == '__main__':
    info()