# Feedback Response                                
                         
- **tighter verification**             
                   
    will partly address            
          
    I will attempt to tighten the verification but verifying strings have been giving me issues. I          
    have ideas such as minimum lengths and invalid characters for names. My goal is to have the valid                       
    input options be broad enough that there shouldn't be any issues but limiting enough that                      
    invalid data doesn't slip through the cracks.                                  
                                               
- **duplicate IDs**                          
                           
    will address                       
                                     
    My thought is to have a section specifically check the IDs from the Excel sheet with the list of                        
    known IDs in the database but when and how is up in the air. I’d like to do it in the verification                       
    step, so it's a clean list of steps as well from a log construction standpoint. But it would                    
    make more sense logically to do it in the insertion step since it will already have the database                       
    open at that point. I'm going to have to think on this one                     
                                
- **informal typing**                           
                                      
    will address                            
                                            
    Will go through and fix grammar and spelling. Most of it was meant to be temporary                            
    text anyways, but I still need to get better at typing it correctly the first time.                         
                            
- **db_open redundancy**                                     
                                        
    will partly address                              
                                         
    I'm pretty sure at least one of the functions it's in may work just fine without it                                   
    but I think it's still useful in its original use case. I will have to do some testing                                  
    to see if it can be removed or not. If one works without it and the other doesn't, I                         
    may rewrite the one that depends on it so it works without it if at all possible.                           
                                   
- **validation.py typo**                                                     
                                                   
    will address                                          
                                          
    I take full responsibility for that. I meant to do more thorough testing but                                   
    didn't get around to it. While I'm fixing the typos, I'll also do more through                          
    testing on the branching validation structure of validation.py.                      
                                  
- **SQL_output.py references input rather than file_path**                                  
                               
    will address                                        
                                                    
    Will change input to file_path where applicable.                                  
                                               
- **process() doesn't return log data**                                        
                                                         
    will address                                 
                                                   
    Will make sure it is able to return data. will check to see if it's                       
    that it doesn't have a return argument or a variable to accept the data.               
                       
- **main.py operations.close has no parentheses**                                    
                            
    already addressed                            
                                                    
    Shortly after got feedback fixed this issue by putting parentheses after                           
    close, I will check to see if there's any other cases like this.                    
                                    
- **validation.py treats rows with sales of 0 as null**                                   
                                   
    will address                              
                                                  
    Will change the validation method for sales and ID to check for not                      
    null and will use other methods for type validation.                       
                                              
- **command line argument**                    
                                   
    will address                               
                                       
    Was already planning on it. I mentioned in the commenting above the two main                       
    input arguments that I meant this to be a temporary solution. My main goal for                  
    this go round was to get this tool up and running like a prototype. will adjust the 
    code as needed i didnt realize the exact nature of the comand line argument portion though.                 
                             
- **code duplication**                        
                          
    will address                        
                             
    Will make the code insertion portion into a sperate function from the table                               
    creation function and will pass the data through code insertion function.                         
    The table creation function will be called depending on whether a table is present.                                                      