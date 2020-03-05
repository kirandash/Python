# Calendars

# import calendar module
import calendar

# create plain text calendar
c = calendar.TextCalendar(calendar.SUNDAY) # starting day of week is Sunday
st = c.formatmonth(2020,3,0,0)
print(st) # March 2020 calendar starting sunday

c = calendar.TextCalendar(calendar.MONDAY) # starting day of week is Sunday
st = c.formatmonth(2021,4,0,0)
print(st) # April 2021 starting MONDAY

# HTML formatted calendar
h = calendar.HTMLCalendar(calendar.MONDAY)
hst = h.formatmonth(2021,4)
print(hst) # April 2021 starting MONDAY - table based calendar - with classes for styling

# loop over days of a month
# zeroes mean that the day of that week belongs to another month
for i in c.itermonthdays(2020,8): # loop through Aug 2020 days
    print(i)

# calendar module provides useful utilities for the given locale Ex: days and months in full and abbreviated forms
for name in calendar.month_name:
    print(name)

for name in calendar.day_name:
    print(name)

# If team meeting on first Friday of every month. What day would it be for each month
print("Team meetings will be on: ")
for m in range(1,13): # 13 is not included
    cal = calendar.monthcalendar(2020, m)
    weekone = cal[0]
    weektwo = cal[1] # First Friday must be within week 1 or two

    if weekone[calendar.FRIDAY] != 0: # if calendar's Friday is in weekone then weekone has the meetday else week two
        meetday = weekone[calendar.FRIDAY]
    else:
        meetday = weektwo[calendar.FRIDAY]

    print("%10s %2d" %(calendar.month_name[m], meetday))
