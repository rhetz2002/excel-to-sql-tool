# Excel to SQL converter

---

## requirements 

python library, pandas module 

## what does this tool do 

this tool will take an excel (xlsx) file, convert, and input  

the information into a SQL .db file. 

## instillation 

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

finally it will output a running operations log in the log folder next to the program
