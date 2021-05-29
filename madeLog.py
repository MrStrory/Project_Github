import os

def makeDir():
    if os.path.exists('logs'):
        return True
    else:
        os.mkdir('logs')
        return True
