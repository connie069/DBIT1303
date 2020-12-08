import datetime
from allFunctions import *

prepareDB()

currentDT=datetime.datetime.now().strftime("%d-%m-%Y")
print ("Today: %s\nYou should select a date in the next 10 days." % str(currentDT))

while 1:
    choosing=whishChoosing()
    processChoosing(choosing)
