# Dates
from datetime import date
from datetime import time
from datetime import datetime

def main():
    # Date Objects
    
    # Get Today's date from the today() method from date class
    today = date.today()
    print("Today's date is ", today) # yyyy-mm-dd

    # Date's individual component
    print("Date components are: ", today.day, today.month, today.year)

    # Get today's weekday (0=Monday, 6=Sunday)
    print("Today's week day is: ", today.weekday())
    days=["mon","tue","wed","thu","fri","sat","sun"]
    print("which is a: ", days[today.weekday()])

    # DateTime Class

    # Get current time and date
    now = datetime.now()
    print("Current Time and Date is: ", now)

    # Get current time only
    print("Time now is: ", datetime.time(datetime.now()))

if __name__ == "__main__":
    main()