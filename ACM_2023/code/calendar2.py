def main():
    daysInWeekCount, monthCount, X, Y, Z = map(int, input().split())
    monthsInYear = list(map(int, input().split()))
    startYear = 1
    yearDayStart = 0

    # Query count
    for i in range(int(input())):
        year, qmonth, dayStart = map(int, input().split())
        dayCount = 0

        # From start year to current year
        for currYear in range(startYear, year):
            for month in range(monthCount):
                if month == 2:
                    if currYear % X == 0:
                        dayCount += monthsInYear[1] + 1
                        continue
                    if currYear % Z == 0:
                        dayCount += monthsInYear[1]
                        continue
                    if currYear % Y == 0:
                        dayCount += monthsInYear[1] + 1
                        continue
                    dayCount += monthsInYear[1]
                else:
                    dayCount += monthsInYear[month - 1]

            for i in range(1, qmonth):
                if i == 2:
                    if year % X == 0:
                        dayCount += monthsInYear[1] + 1
                        continue
                    if year % Z == 0:
                        dayCount += monthsInYear[1]
                        continue
                    if year % Y == 0:
                        dayCount += monthsInYear[1] + 1
                        continue
                    dayCount += monthsInYear[1]
                else:
                    dayCount += monthsInYear[month - 1]


        yrStart = (yearDayStart + dayCount) % daysInWeekCount

        startYear = year
        yearDayStart = yrStart
        
        monthDayStart = (yrStart + dayCount + dayStart) % daysInWeekCount
        if monthDayStart == 0:
            print(monthDayStart + daysInWeekCount)
        else:
            print(monthDayStart)
    

if __name__ == "__main__":
    main()


