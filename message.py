import threading

def message_(message = ''):
    mlog = ''
    for i in message:
        if i == '\n':
            i = '\n\t'
        mlog += i
    if message != '':
        th = threading.Thread(target=writeLog, args=('\t' + mlog + '\n', ''))
        threadList.append(th)
    value = input(message)
    th = threading.Thread(target=writeLog, args=('user:\n', ''))
    threadList.append(th)
    th = threading.Thread(target=writeLog, args=('\t' + value + '\n', ''))
    threadList.append(th)
    th = threading.Thread(target=writeLog, args=('program:\n', ''))
    threadList.append(th)
    return value

threadList = []
i = '0'

def printlog(message = '', end='\n'):
    global i
    global threadList
    mlog = ''
    message = str(message)
    for j in message:
        if j == '\n':
            j = '\n\t'
        mlog += j

    if i == '1':
        print(message, end=end)
        th = threading.Thread(target=writeLog, args=(mlog, end))
        threadList.append(th)
    else:
        print(message, end=end)
        th = threading.Thread(target=writeLog, args=('\t' + mlog, end))
        threadList.append(th)

    if end == '\n':
        i = '0'
    else:
        i = '1'

def openlog(message = ''):
    mlog = ''
    message = str(message)
    for j in message:
        if j == '\n':
            j = '\n\t'
        mlog += j
    th = threading.Thread(target=writeLog, args=('program:\n', '', 'w'))
    threadList.append(th)
    print(message)
    th = threading.Thread(target=writeLog, args=('\t' + mlog, '\n'))
    threadList.append(th)

def writeLog(message, end, workFile='a'):
    with open('logs/log.txt', workFile) as log:
        print(message, end=end, file=log)

def append_thredList(list1):
    global threadList
    threadList.extend(list1)

def startThread():
    global threadList
    for j in threadList:
        j.start()
        j.join()
