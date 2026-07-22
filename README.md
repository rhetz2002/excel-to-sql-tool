# Excel to SQL converter

tool to convert and insert excel into sql databases

this tool solves the issue of having to manually type out excel data into an SQL format. all that is needed is to type in a single terminal command with a cuple arguments.

## instillation 

**requirements** 

python3, pandas module  


**windows** 

install python interpreter from official python website  

[https://www.python.org/downloads/](https://www.python.org/downloads/) 

**Linux (Arch and Arch base systems)** 

install python interpreter through pacman  

install pandas through pacman 

eg. sudo pacman -S python, sudo pacman -S python-pandas 

**linux (other systems)

install python interpreter through your package manager

install pandas through your package manager

eg. 

debian: sudo apt install python, sudo apt install python-pandas

fedora: sudo dnf install python, sudo dnf install python-pandas

lastly download the zip from the repo or git clone the repo

```text
https://github.com/rhetz2002/excel-to-sql-tool/tree/main
```


## how to use  

input the file path to main.py in line with the python3 command or windows equivalent 

eg. python3 tool/main.py 

the tool requires two arguments the input path and the output path, it uses the relative path from the directory open in the terminal

for example if I input in a fresh terminal on my system

```text  
    python3 main.py input.xlsx output.db     
```
it would look for the paths 

```text  
    /home/{name}/input.xlsx /home/{name}/output.db    
```
if it cant find an input or output file it will prompt for an input or output file 

these will also be relative to the open directory 

it has the ability to append like IDs if names match in the corresponding output file

if the data in a row is invalid it will omit the corresponding row

if it executes successfully, you will see a breakdown of lines successfully added  

and the lines that failed with the line "success" all printed in the terminal 

a sucsessfull run will output the following to the terminal

```text 
rows processed
--------------------------------------------
row 0 sucsess
row 1 sucsess
row 2 fail
row 3 fail
row 4 fail
row 5 fail
row 6 fail
row 7 sucsess
row 8 fail
row 9 sucsess
row 10 sucsess
row 11 sucsess
row 12 fail
row 13 fail
row 14 sucsess
row 15 sucsess
row 16 sucsess
row 17 sucsess
row 18 sucsess
row 19 sucsess
row 20 sucsess
row 21 sucsess
row 22 sucsess
row 23 sucsess
16 rows processed successfully
8 rows failed,
check operations log for more detail
--------------------------------------------
success
```
finally it will output a running operations log in the log folder next to the program

## expected data format 

the data expected in the input is the following

| ID | name  | email | department | sales|
|----|-------|-------|------------|------|
|employee ID (unuiqe whole number)| employee name (first and last name, plain text)| employee email (include .com and @)| department (including either salse or customer service) | sales made (number with two decimal places)|