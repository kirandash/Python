# working with os path module

import os
from os import path
import datetime
from datetime import date, time, timedelta
import time

def main():
    # print name of OS
    print(os.name)

    # check if item exists
    print("Item exists: " + str(path.exists("python_101/04/textfile.txt")))
    print("Item is a file: " + str(path.isfile("python_101/04/textfile.txt")))
    print("Item is a directory: " + str(path.isdir("python_101/04/textfile.txt")))

    # work with file paths
    print("Item path: " + str(path.realpath("python_101/04/textfile.txt")))
    print("Item path and name: " + str(path.split(path.realpath("python_101/04/textfile.txt"))))

    # Get the modification time
    t = time.ctime(path.getmtime("python_101/04/textfile.txt"))
    print(t)
    print(datetime.datetime.fromtimestamp(path.getmtime("python_101/04/textfile.txt"))) # does the same as time.ctime

    # Calculate how long ago the file was modified
    td = datetime.datetime.now() - datetime.datetime.fromtimestamp(
        path.getmtime("python_101/04/textfile.txt")
    ) # creates a timedelta object which is a diff b/w current time and mtime of txt file
    print("It has been " + str(td) + " since the file was modified")
    print("Or, " + str(td.total_seconds())+ " seconds")

if __name__ == "__main__":
    main()