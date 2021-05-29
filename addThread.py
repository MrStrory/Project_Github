import threading

listThread = []

def addThread(list1):
    global listThread
    listThread.extend(list1)

def refresh():
    global listThread
    listThread = []

def message_(message = ''):
    global listThread
    mlog = ''
    for i in message:
        if i == '\n':
            i = '\n\t'
        mlog += i
    if message != '':
        th = threading.Thread(target=writeLog, args=('\t' + mlog + '\n', ''))
        listThread.append(th)
    value = input(message)
    th = threading.Thread(target=writeLog, args=('user:\n', ''))
    listThread.append(th)
    th = threading.Thread(target=writeLog, args=('\t' + value + '\n', ''))
    listThread.append(th)
    th = threading.Thread(target=writeLog, args=('program:\n', ''))
    listThread.append(th)
    return value

i = '0'

def printlog(message = '', end='\n'):
    global i
    global listThread
    mlog = ''
    message = str(message)
    for j in message:
        if j == '\n':
            j = '\n\t'
        mlog += j

    if i == '1':
        print(message, end=end)
        th = threading.Thread(target=writeLog, args=(mlog, end))
        listThread.append(th)
    else:
        print(message, end=end)
        th = threading.Thread(target=writeLog, args=('\t' + mlog, end))
        listThread.append(th)

    if end == '\n':
        i = '0'
    else:
        i = '1'

def openlog(message = ''):
    global listThread
    mlog = ''
    message = str(message)
    for j in message:
        if j == '\n':
            j = '\n\t'
        mlog += j
    th = threading.Thread(target=writeLog, args=('program:\n', '', 'w'))
    listThread.append(th)
    print(message)
    th = threading.Thread(target=writeLog, args=('\t' + mlog, '\n'))
    listThread.append(th)

def writeLog(message, end, workFile='a'):
    with open('logs/log.txt', workFile) as log:
        print(message, end=end, file=log)

def get_list_thread():
    return listThread