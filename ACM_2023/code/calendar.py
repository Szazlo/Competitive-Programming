def main():
    daysInWeekCount, monthCount, X, Y, Z = map(int, input().split())
    monthsInYear = list(map(int, input().split()))
    startYear = 1
    yearDayStrt = 0

    # Query count
    for i in range(int(input())):
        year, month, dayStart = map(int, input().split())
        yrdayStart = yearDayStart(year, monthsInYear, monthCount, daysInWeekCount, X, Y, Z)
        dayCount = 0
        for i in range(1, month):
            dayCount += nrOfDays(i, monthsInYear, year, X, Y, Z)
        
        monthDayStart = (yrdayStart + dayCount + dayStart) % daysInWeekCount
        if monthDayStart == 0:
            print(monthDayStart + daysInWeekCount)
        else:
            print(monthDayStart)
        

        
def yearDayStart(year, monthsInYear, monthCount, daysInWeekCount, X, Y, Z):
    dayCount = 0

    for currYear in range(1, year):
        for month in range(monthCount):
            dayCount += nrOfDays(month, monthsInYear, currYear, X, Y, Z)

    return dayCount % daysInWeekCount


def nrOfDays(month, monthsInYear, year, X, Y, Z):
    if month == 2:
        return monthsInYear[1] + isLeap(year, X, Y, Z)
    
    else:
        return monthsInYear[month-1]

def isLeap(year, X, Y, Z):
    if year % X == 0:
        return 1
    if year % Z == 0:
        return 0
    if year % Y == 0:
        return 1

    return 0



if __name__ == "__main__":
    main()


