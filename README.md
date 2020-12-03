# codeExec
Executing code *without bugs.*

## Installation
You can install `codeExec` two ways.
***
1a. Using the `zip` file (Ubuntu Terminal):
- Step 1: Run the command `wget https://repl.it/@NoNameByProgram/codeExec.zip`. This will download the zip in the current directory.
- Step 2: Unzip the downloaded file by running `unzip -o codeExec.zip "main.py"`.
- Step 3: Remove the `zip` file by running `rm codeExec.zip`.
- Step 4: Rename the file `codeExec.py` by running `mv main.py codeExec.py`.
- Step 5: Use the API!

1b. Using the `zip` file (MacOS X Terminal):
- Step 1: Repeat Step 1 in `1a`, but replace `wget` with `curl`. 
- Step 2: Follow the steps of `1a` from Steps 2-5. 

***
2\. Use `pip` (Any OS):
- Step 1: Open your local console.
- Step 2: Install `codeExec` with `pip install codeexec`.
- Step 3: Use the API!

# API
To import the API, simply use:
```py
import codeExec
```

## Functions
Functions in `codeExec` are simple – we put beginners first.

### `retConsole`
The `retConsole` function is when the code provided (argument 1) is executed and it returns the logged data.
An example:
```py
output = retConsole('''
print("it's the end of the line, buddy.")
''')
print(output) # returns: it's the end of the line, buddy.
```
***
### `runScript`
The `runScript` function is when the file provided (argument 1) is executed.
An example:

`main.py`
```py
runScript('secondary.py') # returns: uno reverse
```

`secondary.py`
```py
print("uno reverse")
```