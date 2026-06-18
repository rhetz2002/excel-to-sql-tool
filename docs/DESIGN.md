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
  [iterate over and validate Excell file]           
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
            |    [stops processing and]               
            |    [validation, outputs]              
            |    [error log to terminal]                  
            |                               
            v                       
[continues to convert,]                                      
[goes back two steps too]                         
["iterate.. ..Excell file"]                                 
[repeat this process until]                       
[it reaches end of the file]                                   
            |             
            |                    
            |               
            v                 
[reaches the end of the data]                    
[one last validation read]                             
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
                                           
rundown of the process of the tool                       
                                                 
this will run under the assumption that it's meant to                                   
export data fitting the upper schema and only that data                                        
                                         
```text

main():

    read_Excell(input/filename.xlsx)

    placeholder_for_data = []
    
    read row (filename.xlsx)

    loop(until end of file or invalid data is read):

        validate_row()

        if (data is valid)
            
            add data to placeholder_for_data

            load next row                

        else 

            end proccess

            print error log to terminal
    
     read data list to verify data

    load first section in placeholder_for_data
 
    loop (for number of rows)
        
        if (required) check (if not null)
            
            if null, fail validation

            end proccess

            print error log    

        if (should be text) check (if text)
            
            if not text, fail validation

            end proccess

            print error log

        if (should be int) check if (int)
            
            if not int fail validaton

            end proccess

            print error log

        if (should be real) check if (real)
            
            if not real fail validation

            end proccess

            print error log
        
        load next section in placeholder_for_data

    
    load SQLite file

        for (elements in placeholder for data)

            insert_row(R,C)

    Close (filename.xlsx) 

    Close (SQLite file)

    print output log to terminal
    
    open (operations log) 

    append output log to operations log  

    close (operations log)    
```

## SECTION 4 File & Folder Structure              
              
overall folder structure              
           
Excel-To-SQL-Tool             
├── main.py                  
├── validation.py                
├── log_output.py               
├── excell2SQL.py                     
├── excell_read.py              
├── input/                 
│     └── input.xlsx                 
├── sql_out.py                     
├──docs/             
└──README.md              
                                    
## SECTION 5                                   

secondary python libraries to be used                         
                                        
pandas (for reading Excell files)                             
sqlite3 (for SQL database)                                       
argparse (for accepting filepath as commandline argument)                          
logging (for writing errors to logs)                                  