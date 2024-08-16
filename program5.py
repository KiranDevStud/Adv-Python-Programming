import calendar

def findDay(date):
        day, month, year = (int(i) for i in date.split(' ')) 
        dayNumber = calendar.weekday(year, month, day)
        days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        return days[dayNumber+1]

date = input("Enter a date in the format DD MM YYYY")
print(findDay(date))
