import calendar

year = int(input("Enter the Year: "))
#month = int(input("Enter the Month: "))

calendar.setfirstweekday(calendar.SUNDAY)

#mycalender = calendar.month(year,month)
mycalendar = calendar.calendar(year)

print(mycalendar)