## Phase 2 Changes (Week 6)

modified the coding structure in section 3. 

main modification in the sudo code is the repromts to make sure that the program sucsessfully opens the input and output locations. its an error handeler as well as a QoL feature for the user. also updated a verification logic and finalised output prossess. planned to have the program quit after a single bad input but now it stores a log of the bad inputs and outputs the good data into the db and rejects the bad data with a list of the bad points to the user as a log.

section 4 folder structre

removed log_output as it is reduntant also added the tool subfolder and the log folder, tool folder is for orginisation reasons and the log folder holds the operaitons log

section 5 secondary libraries
removed logging as is redundant
may add another library to use in order to check for a file present

## SECTION 1, Program Overview                   
Overview of the tool’s processes                       
---                  
This tool will accept an Excell file as an input, proccess                            
it into SQL, and insert the output SQL into a chosen SQL database.                                   
                                                                    
It will accept an Excell document as input and start to read                        
through it (possibly using a while loop,) validate the processed data.                           
And if it's valid, it will convert and output valid SQL into an                                   
existing SQL database. if it is read as invalid, it will stop                                
reading at the point of error and output an overview                                      
of the error into the command line and an error log.                           
                                                                        
After the tool is done running, it will output a log of all the                                    
lines read, processed, and added to the SQL database.                                           
                                                                 
---
## SECTION 1 process diagram       
      
```text        

          [input Excell file]       
                  |      
                  |      
                  v       
  [iterate over and validate row in Excell file]           
                  |           
                  v               
[if data is valid]|[if data is invalid]              
                 / \         
                /   \               
               /     \            
              /       \              
             /         \               
            |           |
            |           v        
            |    [skip row, output error]               
            |    [into terminal, go to next]              
            |    [row, go back two steps]
            |    [unles at end of data]                  
            |    [then go to next step]     
            v                |       
[continues to convert]       |                              
[goes back two steps too]    |                     
["iterate.. ..Excell file"]  |                               
[repeat this process until]  |                     
[it reaches end of the file] |                                  
             |               |
             |               |
              \             /
               \           /
                \         /
                 \       /
                  \     /
                   \   / 
                    \ /
                     |             
                     |                    
                     |               
                     v                  
        [reaches the end of the data]                                                 
        [exports the converted SQL]                 
        [into the database]                          
```               
          
---      
## SECTION 2 Database Schema                    
                                  
breakdown of database schema                        
                                 
table name: employee sales                                                   
                     
column names                      
employee_ID: (integer, primary key, required)                                                 
employee_name: (text, required)                                        
employee_email: (text, required)                                                
department: (text)                                                          
sales: (real)                              
                    
SQL table creation                                                   
                                            
CREATE TABLE employee_sales (                                           
                                         
employee_ID int PRIMARY KEY, NOT NULL                           
employee_name text NOT NULL                                       
employee_email text NOT NULL                                             
department text                                      
sales real                                                          
); 
                        
---                        
## SECTION 3 psudo code                             
                                
SECTION 3 pseudo code                                 

> Updated — Week 6: [restructred validation logic and repormpting user process, no longer quits after a single bad row]

rundown of the process of the tool                       
                                                 
this will run under the assumption that it's meant to                                   
export data fitting the upper schema and only that data                                        
                                         
```text

ask user for file path

try
    
    read_Excell(input/filename.xlsx)

except 

    while file unopened

        ask user for file

        read_Excell(input/filename.xlsx)
    
    placeholder_for_data = []

    for rows and columns in file

        loop(until end of file):

            try 
                if (ID is valid)
                    if (name is valid)
                        if (email is valid)
                            if (sales is valid)
                                if (department is valid)
                                    add data to placeholder_for_data
            
            except
                
                store row and index for error log

    while db is unoppened

        try 
            
            open db

            for rows and columns in file

                insert row into db
        
        except

            while unoppened 

                if

                    prompt user if they want to create a new db
                    
                        create db

                            for rows and columns in file

                                insert row into db

                else

                    prompt user to input file

    Close (SQLite file)

    print output log to terminal
    
    open (operations log) 

    append output log to operations log  

    close (operations log)    
```

## SECTION 4 File & Folder Structure              

overall folder structure              

> Updated — Week 6: [removed log output, added tool and log folders, moved program files into tool folder]

Excel-To-SQL-Tool             
├── tool/
│    ├── main.py
│    ├── validation.py                  
│    ├── SQL_output.py                                  
│    ├── excell_open.py              
│    ├── output/
│    │    └── output.db
│    ├── input/                 
│    │    └── input.xlsx                                     
│    └── log/
│         └── operations.log
├──docs/             
└──README.md              
                                    
## SECTION 5                                   

secondary python libraries to be used                         

> Updated — Week 6: [removed logging added pathlib]

pandas (for reading Excell files)                             
sqlite3 (for SQL database)                                       
argparse (for accepting filepath as commandline argument)                          
pathlib (checking if file is present)