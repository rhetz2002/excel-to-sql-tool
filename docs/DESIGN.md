## SECTION 1, Architecture Overview
Overall overview of the tool prossesses
---
this tool will acept an excell file as an input, proccess             
it into SQL, and input the output SQL into a chosen SQL database.                 

It will acept an Excell document as input and start to read             
through it (posibly using a while loop) validate the data                        
and if its valid it will convert and output valid SQL into an                         
exsisting sql database. if it is read as invalid it will stop                        
reading at the point of error and output an overview                 
of the error in inot the command line                       
                                                                 
after the tool is done running it will output a log of all the                              
lines read, proccesed, and added to the sql database                                      

---
## SECTION 1 prossess diagram      
      
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
            |    [stops prosessing and]               
            |    [validation, outputs]              
            |    [error log to terminal]                  
            |                               
            v                       
[continues to convert]                        
[goes back two steps too]             
["iterate.. ..Excell file"]                 
[untill reache end of file]                        
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

table name                   
employee sales                    
                     
coloumn names                      
employee_ID : (intiger, primary key, required)                     
employee_name : (text, required)                       
employee_email : (text, required)                      
department : (text)                   
sales : (real)                    
                    
sql table creation                      
                               
CREATE TABLE employee_sales (

    employee_ID int PRIMARY KEY, NOT NULL
    employee_name text NOT NULL
    employee_email text NOT NULL
    department text
    sales : real
);
                        
---
## SECTION 3 psudo code 

rundown of the proccess of the tool

this will run under the assumption that its ment to export data 
fitting the upper infromation and only that data


```text

main():

    read_excel(input/filename.xlsx)

    placeholder_for_data = []
    
    load section in (filename.xlsx)

    loop(untill end of file or invalid data is read):

        read row (filename.xlsx)

        validate_row()

            end process
                
                print error log to terminal

        if (data is valid)
            
            add data to placeholder_for_data

            load next row                

        else 

            end proccess

            print error log to terminal
    
    read data list to veriffy data

    load first section in placeholder_for_data
 
    loop(for number of rows)
        
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

    print output log 

    apend output log to opertation log

    end 
        
```

## SECTION 4 File & Folder Structure              
              
overall folder structre             
           
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
argparse(for accepting filepath as commandline argument)                          
logging (for writing errors to logs)                                  

hope this is good





