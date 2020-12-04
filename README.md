# codeExec
Executing code *without bugs.* 

## Installation
You can install `codeExec` two ways.
***
1a. Using the `zip` file (Ubuntu Terminal):
- Step 1: Run the command `wget https://repl.it/@NoNameByProgram/codeExec.zip`. This will download the zip in the current directory.
- Step 2: Unzip the downloaded file by running `unzip -o codeExec.zip "codeExec/"`.
- Step 3: Remove the `zip` file by running `rm codeExec.zip`.
- Step 4: Use the API!

1b. Using the `zip` file (MacOS X Terminal):
- Step 1: Repeat Step 1 in `1a`, but replace `wget` with `curl`. 
- Step 2: Follow the steps of `1a` from Steps 2-4. 

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
Functions in `codeExec` are simple – we put simplicity first.

### `retConsole`
The `retConsole` function is when the code provided (argument 1) is executed and it returns the logged data.
An example:
```py
variable = 3
output = retConsole('''
variable += 3
print(variable)
''')
print(output) # returns: 6
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
However, a con about this is that the code after a `runScript` function is called, the following code will not be executed.
An example:

`main.py`
```py
runScript('secondary.py')
print('done!') # only returns: uno reverse
```

`secondary.py`
```py
print("uno reverse")
```