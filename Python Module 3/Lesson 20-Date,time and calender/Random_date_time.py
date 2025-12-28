import random
import time
def getRandomDate(startDate, endDate):
    print ("Printing a random date between", startDate, "and", endDate)
    randomGen=random.random()
    dateFormat='%m/%d/%Y'
    startTime=time.mktime(time.strptime(startDate, dateFormat))
    endTime=time.mktime(time.strptime(endDate, dateFormat))
    randomTime=startTime+randomGen*(endTime-startTime)
    randomDate=time.strftime(dateFormat,time.localtime(randomTime))
    return randomDate
print("Random date is", getRandomDate("1/1/2026", "12/12/2026"))