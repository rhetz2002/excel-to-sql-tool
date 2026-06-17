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
      
        little rusty in python

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
            |           |             
            |           |                
            |           |                
            |           |                  
            |           |                   
            |    [stops prosessing and]               
            |    [validation, outputs]              
            |    [error log to terminal]                  
            |                 
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
[exports the converted SQL]                 
[into the database]
```               
          
                   
---      

