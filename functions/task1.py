from MyProjectForGithub.addThread import message_ as m
from MyProjectForGithub.addThread import printlog as p
from MyProjectForGithub.addThread import get_list_thread as get
from MyProjectForGithub.addThread import refresh
import MyProjectForGithub.functions.generateData as generateData

coeff = 1000

parametrs = [
    {
        'message' : 'Enter country name: ',
        'functions' : []
    },
    {
        'message' : 'Enter population: ',
        'functions' : [generateData.toInteger, generateData.value_more_or_equal_zero]
    },
    {
        'message' : 'Enter fertility per ' + str(coeff) + ' people: ',  # дописать с помощью функции формат и lambda
        'functions' : [generateData.toInteger, generateData.value_more_zero]
    },
    {
        'message' : 'Enter mortality on ' + str(coeff) + ' people: ',
        'functions' : [generateData.toInteger, generateData.value_more_zero]
    },
    {
        'message' : 'Enter the number of years: ',
        'functions' : [generateData.toInteger, generateData.value_more_zero]
    },
]

def main():
    refresh()
    announce()
    while True:
        parametrList = generateData.generateConstant(parametrs)
        if parametrList == 'back':
            return get()
        if parametrList == 'restart':
            continue
        break
    task1(parametrList[0], parametrList[1], parametrList[2], parametrList[3], parametrList[4])
    return get()

def announce():
    p('\nPopulation size\n')

def task1(country, population, fertility, mortality, years):
    i = 1
    while i <= years:
        i += 1
        mFactor = population // coeff
        wasBorn = fertility * mFactor
        died = mortality * mFactor
        population += wasBorn
        population -= died
    p('Population of the country ' + country + ' through ' + str(years) + ' years will be ' + str(population) + ' people')

if __name__ == '__main__':
    main()

