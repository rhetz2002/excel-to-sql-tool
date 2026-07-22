## Phase 2 Changes (Week 6)

modified the coding structure in section 3. 

The main modification in the pseudo code is the re-prompts to make sure that the program successfully opens the input and output locations. It's an error handler as well as a QoL feature for the user. I also updated the verification logic and finalized the output process. I planned to have the program quit after a single bad input but now it stores a log of the bad inputs and outputs the good data into the db and rejects the bad data while outputting a list of the bad points to the user as a log. 

section 4 folder structure 

Removed log_output as it is redundant. I also added the tool subfolder and the log folder. Tool folder is for organization reasons, and the log folder holds the operations log 

section 5 secondary libraries                                   

Removed logging as it is redundant, may add another library to use to check if a file present           

## Phase 2 changes (Week 8)

modified the coding structure in section 3. 

added the process of appending data corisponding to an exsisting ID

also moved where the db is oppend

section 4 folder structure 

added SQLcheck.py

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
> Updated — Week 8: [moved db opening proccess, added id appending proccess]

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

----------------------------------------------------(updated)----------------------------------------------------
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

                            

                else

                    prompt user to input file
-----------------------------------------------------------------------------------------------------------------

----------------------------------------------------(updated)----------------------------------------------------
    for rows and columns in file

        loop(until end of file):

            try 
                if (ID is valid)
                    if (name is valid)
                        if (email is valid)
                            if (sales is valid)
                                if (department is valid)
-----------------------------------------------------------------------------------------------------------------
----------------------------------------------------(updated)----------------------------------------------------
                                    if (ID is Duplicate)
                                        if (name matches name paird with ID in db)
                                            append data to db 
                                        else
                                            store row and index for error log and removal
-----------------------------------------------------------------------------------------------------------------
                                    else 
                                        add data to placeholder_for_data
            
            except
                
                store row and index for error log and removal
    
    for rows and columns in file

        insert row into db

    Close (SQLite file)

    print output log to terminal
    
    open (operations log) 

    append output log to operations log  

    close (operations log)    
```

## SECTION 4 File & Folder Structure              

overall folder structure              

> Updated — Week 6: [removed log output, added tool and log folders, moved program files into tool folder]

> Updated — Week 6: [added SQLcheck.py]

Excel-To-SQL-Tool             
├── tool/                  
│    ├── main.py             
│    ├── validation.py                  
│    ├── SQLoutput.py    
│    ├── SQLcheck.py                              
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