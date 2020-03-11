# Python
Python, popular OO language used in client and cloud side apps.

## 1. Intro
### 1.1 Installing Python
1. Python is mostly pre installed on mac and linux.
2. Run on mac: `python3 --version` (Python 3.8.2). Pythong 2.7 is original version of Python, dev is already stopped and support is only till 2020. Whereas Python 3.7 is the updated new version of Python.
3. If not installed, go to https://www.python.org/ and proceed with downloads.
4. Download ---> Launch the Installer and complete installation
5. Additional step for mac: Go to Applications ---> Run Shell: "Install certificates command" (This will install necessary certificates reqd for working with internet data)
6. `python -v` is used to check python version on windows

### 1.2 Tools
1. VSCode
2. Extensions: Python by MS
3. Open Working directory on VS, Click on Debug icon. Click on gear icon. Chose Python environment. It will open launch.json settings file. Change `cwd` to empty string. This will make sure that the debugger points to the same directory where python file is present.

## 2. Basics
### 2.1 Hello World
1. To launch python interpreter from command terminal: run `python3`
2. Python is an interpreted language. Much like JS/PHP unlike Java or C++. It doesn't need to be build as an executable before running it.
3. print('hello world')
4. exit()
5. Python uses `:` to understand that scope block has started and indentation is used to know if a block of code belongs to a function.
6. Run VS debugger icon to execute the active py file.

### 2.2 Variables and Expressions, global, del
1. Install a Python code formatter eg autopep8. After writing code, press option + Shift + F
2. Python is a strongly typed language. And does not allow mixing types of vars
3. Function has a local scope for variable
4. `global name` creates a global variable
5. `del name` deletes a previously created variable

### 2.3 Functions
1. `def func1():` colon is the start of scope block in Python unline braces.
2. `print(power(x=3, num = 2))` python supports name and value declaration. Thus order can be ignored
3. `def multi_add(*args): # multiple args can be sent as *args`
4. Variable args can be combined with a set of formal args but var args in that case should always come at end `def multi_add_offset(num1, num2, *extranums):`

### 2.4 Conditional structures
1. `if elif else`
2. python does not have switch case block. Keeps it simple with elif
3. Ternary equivalent: `st = "x is lt y" if(x<y) else "x is gt or eq y"`

### 2.5 Loops
1. `while` and `for`. simple no other loops `while(x < 5):` and `for y in range(5, 10)`, `for d in days:`
2. `break` is used to stop the current and all next iterations and exit out the loop
3. `continue` is used to only stop the current iteration and continue loop for next one
4. `for` loop in python does not use an index var like JS. To get index we can use `enumerate()` fn

### 2.6 Classes
Classes helps in procedural or OO programming
1. Helps building modules that can be passed to even other projects
2. `class myClass():`
3. `def method1(self):` self refers to the object itself (equivalent of this in js)
4. all fns in class has first arg as self
5. Inheritance: `class anotherClass(myClass): def method1(self): myClass.method1(self)`

## 3. Date and Time
### 3.1 date, time and datetime classes
datetime library

### 3.2 Formatting Date and Time outputs
strftime

### 3.3 Using timedeltas objects
1. Helps us to to mathematical operation on date and time
2. Timedelta is a time span. and not a specific date/time

### 3.4 Calendars
1. Python provides libraries to work with calendars in text and html format
2. TextCalendar

## 4. Working with Files
### 4.1 Reading and writing Files, appending data, closing file
1. No imports reqd
2. `open("textfile.text", "w+")`
3. a for append mode
4. `f.close` to close file
5. `f.write`
6. `f.read` and `f.readlines` to read entire file content or line by line in array

### 4.2 Working with OS path utilities
1. `import os from os import path`
2. `path.exists("textfile.txt")`, `path.isfile()`, `path.isdir()`
3. Item path: `path.realpath("abc.txt")`. Item path and name: `path.split(path.realpath("abc.txt"))`
4. Get modification time: `path.getmtime("abc.txt")`

### 4.3 File system shell methods
1. `import shutil`
2. copy file content: `shutil.copy(src, dst)` : copies only file content and not meta info eg modification time etc
3. copy with meta: `shutil.copystat(src, dst)`
4. rename: `os.rename("python_101/04/rename.txt", "python_101/04/textfile_renamed.txt")`
5. zip: `shutil.make_archive("archive", "zip", root_dir)`: This includes all the files from root dir
6. To control, which file to add in zip, use the `ZipFile` module. `with ZipFile("testzip.zip", "w") as newzip:`

### 4.4 Quiz
1. Get os name for python and cwd: `import os print(os.name) print(os.getcwd())`
2. Read a file content and print it to console: 
    `with open('breeders_for_cats.txt', 'r') as reader: print(reader.read())`

## 5. Working with web data
### 5.1 Fetching internet data
1. `import urllib.request`

### 5.2 Working with JSON
1. JSON feed from: https://earthquake.usgs.gov/earthquakes/feed/, ---> GeoJSON summary Feed ---> All Earthquakes ---> https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_hour.geojson
2. `import json`
3. `json.loads(data)`
4. `print(theJSON["metadata"]["title"])`

### 5.3 Parsing and Processing HTML
1. `from html.parser import HTMLParser`
2. `parser = MyHTMLParser()`, a subclass MyHTMLParser is created to overwrite default parser fns
3. `parser.feed(htmlcontent)`

### 5.4 Manipulating XML
1. While manipulating XML/HTML, we do not want to parse the file line by line. But rather have the entire content in memory viz DOM for easier modification.
2. `doc = xml.dom.minidom.parse("python_101/05/samplexml.xml")`
3. `doc.nodeName`
4. `doc.firstChild.tagName`
