class Month:
    January   = 0
    February  = 1
    March     = 2
    April     = 3
    May       = 4
    June      = 5
    July      = 6
    August    = 7
    September = 8
    October   = 9
    November  = 10
    December  = 11

class Day:
    Sunday    = 0
    Monday    = 1
    Tuesday   = 2
    Wednesday = 3
    Thursday  = 4
    Friday    = 5
    Saturday  = 6

def LeapYear(year):
    if year % 400 == 0 or (year % 4 == 0 and year % 100 <> 0):
        return True

    return False

def DaysInMonth(month,year):
    if month == Month.April or month == Month.June or month == Month.September or month == Month.November:
        return 30
    elif month == Month.February:
        if LeapYear(year):
            return 29
        else:
            return 28
    else:
        return 31

day=Day.Tuesday
startMonth=Month.January
startYear=1901

totalSundays=0

for year in range(startYear,2001,1):
    for month in range(Month.January,(Month.December+1),1):
        if day == Day.Sunday:
            totalSundays+=1
        day+=(DaysInMonth(month,year) % 7)
        day%=7

print "Result: ",totalSundays
