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