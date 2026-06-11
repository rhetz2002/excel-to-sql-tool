# BRD

---

## SECTION 1 Project Overview                   

**What problem dose this tool solve**         
This tool is designed to make the job of transferring an        
excel file into a SQL database easy. it will be near       
automatic, only requiring the user to provide an excel file           
instead of manually typing the data into the SQL database.         

**Who will use this software and how often**                          
The employees of the company will use this software to               
transfer the data into the SQL database. It will assumably               
be used quite frequent with many people in the company.               

**What will success look like for the client**             
Success will be the transfer of information from the            
excel file into the SQL database. Success will also entail             
absolutely no errors from valid data or modification to valid            
data upon transfer of the data into the SQL database. If invalid            
data is input or an unforeseen error occurs, it should prompt               
an error and output an error log instead of transferring the data.                

## SECTION 2 Stakeholders                    

**Who is the client / end user**            
the client is the hiring company with              
the end user being the employees and company                

**Who is the developer**                 
I Myles Tollefson am the developer                   

<!-- really hope this is good....-->

## SECTION 3 Functional Requirements: User Stories              
            
- As a manager, I was to be able to pull up an up to date summary           
  of the SQL database and see if there have been any errors and how many.              
           
- As an IT professional, I want to be able to be called in if there is an                     
  error and have the ability to look at an output log of the error                  
  to put me on the right track to solving the issue.                    
                         
- As an accountant, I want the system to be able to detect bad data                       
  that way I don't have to worry about bad balances getting to my desk.                    
                       
- As a database analyst, I want to be able to load an Excell file on demand so                      
  I can view the data in an easily readable format.                           

- As bookkeeper, I want to be able to insert a simple file to be input into                     
  the SQL database to be stored in our SQL database without any additional hassle.                 

- As an operations manager, I want to be able to input a single file and run a single                       
  command to convert the Excell file to SQL, so my staff doesn't have to do it by hand                          

## SECTION 4 Non-Functional Requirements                       

**Reliability: what happens when the Excel file is missing or malformed**               
it should promt an error to the user and output        
a small error file with more details if needed       
could posilbe be configured to automaticly        
remove older error logs

**Usability: does someone need to be a Python expert to run this tool**              
no it should in best case senrio only require the             
excel file be put in a specific folder, could                     
have an option to be pointed into a folder or               
prompt for name of file after being redirected by bash       

**Portability: what OS and Python version should it run on**             
it should be able to be run on many operating systems with            
it being writen in python as long as python is installed on the system.
it will ising the most recent version of python being version 3.14.5

**Constraints: free tools only, Python only, SQLite only (no external database server required)**
it will using python a free library and programming language          
and will only be using the comapnies internal SQL database

## SECTION 5 Out of Scope                     

- this tool will not be used to view sql, excel data

- this tool will not have a grafical ui and is striclty command line based

- this tool will not it will only output data to a              
  chosen location it will not be abel to manage output data             

- this tool will check for certan amount of user input error but isnt perfect,         
  error verification can only go so far and human error can still be a factor.          
  im sure there are ways to check that input data checks out with alredy existing         
  data in the sql database but that is byond the scope of this tool      

## SECTION 6 Open Questions              

- will it be rquired to convert the sql back into an excel format?          
<!--out of ideas lol-->           
- would you like to controll where the output data is droped or a        
  preechosen location? (likely a folder next to the python program)         
<!--really out of ideas-->          
- is there anything in this BDR that i forgot to mention that is needed in the tool