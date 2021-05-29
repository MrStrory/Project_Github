import timeFunc
from madeLog import makeDir
from hello import hello
from operations import operations

def main():
    makeDir()
    timeFunc.timeStart()
    name = hello()
    operations(name)
    timeFunc.timeEnd()
    timeFunc.bye(name)

main()