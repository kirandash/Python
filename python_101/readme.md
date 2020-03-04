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