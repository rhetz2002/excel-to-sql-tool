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
  command to convert the Excell file to SQL, so my staff doesn't have to do it by hand.                          

## SECTION 4 Non-Functional Requirements                       
                                              
**Reliability: what happens when the Excel file is missing or malformed**                
It should prompt an error to the user and output a small error log with more details              
if needed. It should also prevent the input data from being processed further. Could               
possibly be configured too automatically remove older error logs.                    
                                                                       
**Usability: does someone need to be a Python expert to run this tool**                                           
No, it should in best case scenario only require the excel file be put in a specific folder,                   
could have an option to be pointed into a folder, possibly could be achieved by the cd command                         
or prompt for name of file after being redirected by cd, at most may require minimal bash knowledge.                         

**Portability: what OS and Python version should it run on**                                    
It should be able to run on many operating systems with it being written in python as long as python                          
is installed on the system. It will be using the most recent version of python being version 3.14.5.                         

**Constraints: free tools only, Python only, SQLite only (no external database server required)**                     
It will be using python, a free library and programming language                        
and will only be using the companies internal SQL database.                                
                           
## SECTION 5 Out of Scope                     
- This tool will not be used to view SQL, excel data.                           
                                                           
- This tool will not have a graphical UI and is strictly command line based.                           
                                        
- This tool will only output data to a chosen location. It will not be able to manage output data.                   

- This tool will check for a certain amount of user input error but isn't perfect. Error verification                     
  can only go so far, and human error can still be a factor. I'm sure there are ways to check that input                
  data checks out with already existing data in the SQL database, but that is beyond the scope of this tool.                 

## SECTION 6 Open Questions              

- Will it be required to convert the SQL back into an Excell format?                          
<!--out of ideas lol-->                                                 
- Would you like to control where the output data is dropped or just a                       
  prechosen location? (likely a folder next to the program)                     
<!--really out of ideas-->                                                              
- Is there anything in this BDR that I forgot to mention, that is needed in the tool?            