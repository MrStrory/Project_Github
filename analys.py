import message

def ending():
    print('data processing')
    message.startThread()
    print('All your actions have been recorded')
    print('\nWould you like to analyze the recorded actions?')
    while True:
        print('\n1 - Counting a character\n2 - Output of all words and their number\n3 - Output of all unique words \n\n0 - To complete')
        act = input()
        if act == '1':
            numbCharactersMain()
        elif act == '2':
            get_words_main()
        elif act == '3':
            uniqueWordsMain()
        elif act == '0' or act == 'back':
            return None
        else:
            print('Invalid value')
        print('Do you want to continue analyzing the actions?')



def numbCharactersMain():
    symbol = input('Enter a character to find out how many times it appears: ')
    quonty = numbCharacters(symbol)
    def ending():
        if quonty == 1:
            return 'time'
        else:
            return 'times'
    print('\nCharacter ' + symbol + ' occurs ' + str(quonty) + ' ' + ending() + '\n')


def numbCharacters(symbol):
    symbol = symbol.lower()
    with open('logs/log.txt', 'r') as l:
        quonty = 0
        while True:
            line = l.readline()
            if not(line):
                break
            if line == 'Program:\n' or line == 'User:\n':
                continue
            for i in line:
                if i == symbol:
                    quonty += 1
    return quonty


def listWords():
    with open('logs/log.txt', 'r') as l:
        data = []
        while True:
            line = l.readline()
            if not (line):
                break
            if line == 'Program:\n' or line == 'User:\n':
                continue
            word = ''
            for i in line:
                if checkAlpha(i):
                    word += i
                else:
                    if word == '':
                        continue
                    word = word.lower()
                    data.append(word)
                    data.sort()
                    word = ''
    return data

def uniqueWordsMain():
    print('\nBelow are all unique words:\n')
    uniqueWords(listWords())

def uniqueWords(list1):
    set1 = set()
    for i in list1:
        if i in set1:
            set1.remove(i)
            elem = ' ' + i
            set1.add(elem)
        elif (' ' + i) in set1:
            continue
        else:
            set1.add(i)
    set2 = set()

    for i in set1:
        if i[0] != ' ':
            set2.add(i)
    words = list(set2)
    words.sort()
    for i in words:
        print(i)

import os

def get_words_main():
    print("\nAll words used:")
    wordsList = listWords()
    words_dict = get_words_dict(wordsList)
    for word in words_dict:
        print(word.ljust(20), words_dict[word])

def get_words_dict(words):
    words_dict = dict()

    for word in words:
        if word in words_dict:
            words_dict[word] = words_dict[word] + 1
        else:
            words_dict[word] = 1
    return words_dict


alphabet = [
    'а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л',
    'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш',
    'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я', 'А', 'Б', 'В', 'Г', 'Д', 'Е',
    'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С',
    'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю',
    'Я', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
    'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
    'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
    'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
    'Z'
]

def checkAlpha(symbol):
    for i in alphabet:
        if symbol == i:
            return True
    return False
