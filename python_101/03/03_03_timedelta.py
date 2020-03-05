# timedelta

from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta

# a basic timedelta
print(timedelta(days=365, hours=5, minutes=1)) # 365 days, 5:01:00

# print today's date
now = datetime.now()
print("today is: ", now)

# print today's date, one year from now
print("one year from now will be: ", now + timedelta(days=365))

# timedelta with multiple args
print("In 2 days and 3 weeks, it will be: ", now + timedelta(days=2, weeks=3))

# past calcn: date 1 week ago: formatted
t = datetime.now() - timedelta(weeks=1)
s = t.strftime("%A %B %d, %Y")
print("One week ago it was: ", s)

# How many days until April Fool's day
today = date.today()
afd = date(today.year, 4,1)

# use date comparison to see if April Fool's has already gone for this year, If it has, use the replace() fn to get the date for next year
if afd < today:
    print("April Fool day has passed: %d days ago" %((today - afd).days))
    afd = afd.replace(year = today.year + 1)

# Calculate the amount of time until April Fool's day
time_to_afd = afd - today
print("It's just ", time_to_afd.days, "days until April Fool day")