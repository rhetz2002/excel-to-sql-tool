# BRD

---

## SECTION 1 Project Overview  
**What problem dose this tool solve**    
this tool is designed to make the job of transfering an   
excel file into a SQL database easy. it will be near automatic    
with only requiring the user to provide an excel file instead of    
manualy typing the data into the SQL database   

**Who will use this software and how often**   
the emplyies of the company will use this software to transfer the data    
into the SQL database. it will asumably be used quite frequent with many    
in the company

**What will success look like for the client**    
sucsess will be the transfer of infromation from the excel file into the SQL   
database. sucsess will also entale absolutly no errors from valid data or     
modification to valid data upon transfer of the data into the SQL database.    
if invalid data is input or a unforseen error ocures it should output an error log.  

## SECTION 2 Stakeholders  
**Who is the client / end user**    
the client is the hiring companie with   
the end user bing the employies at the companie

**Who is the developer**    
i Myles Tollefson am the developer    

<!-- really hope this is good....-->

## SECTION 3 Functional Requirements: User Stories 

-as a manager i was to be able to pull up an up to     
 date summery of the SQL database and see if there has      
 been any errors and how many     

-as an IT professional i want to be able to be called       
 in if there is an error and have the ability to look                
 at an output log of the error to put me on the right          
 track to solving the issue

-as an acountant i want the system to be able to detect      
 invalid or corupt data that way i dont have to worry about        
 bad ballences geting to my desk

-as a database analyst i want to be able to load a excell      
 file on damand so i can view the data in an easily       
 readable format

-as bookeeper i want to be able to insert a simple file         
 to be input into an sql database in order to       
be stored in our SQL datbase

-as an operations manager i want to be able       
 to input a single file and run a single command        
 to convert the excell file to SQL so my staff         
 dosnt have to do it by hand       

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
it being writen in python as long as python is installed on the system




## SECTION 5 Out of Scope

## SECTION 6 Open Questions