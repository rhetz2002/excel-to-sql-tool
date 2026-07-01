# Phase 2 Plan

**sprint goal**
By the end of week seven, the tool will have tighter verification logic and error handling, the latter will prevent a hard crash from bad input. It will also have full compatibility with the command line, making it easier to input correct file paths, lessening the possibility for miss-inputs. I will keep the re prompts as I feel it's good for error handling and good from a UX perspective. it will also have cleaner code and comments with better grammar and punctuation and finally most if not all syntax errors that slipped through with v1.0 should be corrected, hopefully preventing further crashes from unexpected inputs. 

**blocking table**

| # |     Item     |     Description     | Priority | Est. Hours | Source |
|---|------|----------------|----------|-------------|----------|
| 1 | validation | detect duplicate ID |   med   |    3 - 4    |  self  |
| 2 | validation | validation incorrectly marking as null | high | 3 - 4 | instructor feedback |
| 3 | validation | verification could be tighter | high | 4 - 5 | self |
| 4 | user input | user input uses input function and not command line argument | med | 2 | instructor feedback |
| 5 | sql insertion | major amount of duplicate code | med | 1 | instructor feedback|
| 6 | logging | log functionality doesn't work in SQL_output  | med | 1 | instructor feedback |

**Definition of Done**

item 1 (duplicate id): done when I can input an excel sheet with a duplicate ID                  
and the row it is in will be rejected rather than cause a hard crash.                
                           
item 2 (incorrectly marking as null): Done when ID and sales with a zero value isn't                      
marked as null and skipped but rather is kept as zero and used.                       
                               
item 3 (tighter verification): Done when I've done all I can to make it functionally tight. I won't                        
be able to make it perfect, but I'll add min character limit and valid character restrictions on the strings.                      
                                                           
item 4 (using command line argument): Done when I have the user using command                 
line arguments instead of having to type it out all by hand.                    
                                                                             
item 5 (code duplication): Done when I have the code in SQL_out lessened and                
the input portion uses a function rather than it being all typed out.                      
                                                                          
item 6 (log output): Done when the logs of SQL_output are correctly output                            
into main and therefore appended to the operations logs.                   

