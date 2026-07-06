## Code Review                 
                                   
### PART 1 — PEP 8 Compliance Check                       
                                    
had allot about white space and line length,                           
tried to get as many 'interesting' ones as possible                           
                                  
- 1 excell_open.py line 41                             
                       
  comparison to False should be 'if cond is False:' or 'if not cond:                           
                                  
  original: while opened == false                       
                                       
  corrected: while opened is false                          
                      
  fixed in (removed whitespace in main.py and excell_open.py as well as changing "==" to "is" on line 41 of excell_open)                          
                                      
- 2 excell_open.py line 47                           
                                     
  tool/excell_open.py:47:80: E501 line too long (113 > 79 characters)                            
                                                         
  original: log = log + f'{time.strftime("%I:%M:%S %p")}: failed to open file in {file} reprompting user input\n'                        
                                           
  corrected: log = log + f'{time.strftime("%I:%M:%S %p")}: failed to ' \                                 
                        f'open file in {file} reprompting user input\n'                            
                                                 
  fixed in (shortened lines added FileError to except statements and removed unessasary whitespace)                      
                                
- 3 SQL_output.py line 71                          
                                                      
  tool/SQL_output.py:71:17: E128 continuation line under-indented for visual indent                         
                                     
  original:                        
                db.execute("""                    
                        INSERT INTO employee_sales                   
                        (employee_ID, employee_name, employee_email, department, sales)                   
                        VALUES (?, ?, ?, ?, ?)""" ,                 
                (data_store[0], data_store[1], data_store[2], data_store[3], data_store[4]))                          
                              
  corrected:                                      
                db.execute("""                      
                           INSERT INTO employee_sales                         
                           (employee_ID, employee_name, employee_email, department, sales)                        
                           VALUES (?, ?, ?, ?, ?)""",                           
                           (data_store[0], data_store[1], data_store[2], data_store[3], data_store[4]))                          
                                                
  fixed in (removed exsess white spaces, shorttened lines, added FileError to except statement)                             
                                    
- 4 validation.py line 90                                   
                                                   
  tool/validation.py:90:80: E501 line too long (151 > 79 characters)                                           
                                   
  original: log = log + f'{time.strftime("%I:%M:%S %p")}: row {index} fail on department check, pleas check that feild contains vaild department\n'                   
                                
  corrected:                                  
            log = log + f'{time.strftime("%I:%M:%S %p")}: row {index} ' \                              
                            f'fail on department check, pleas check that ' \                       
                            f'feild contains vaild department\n'                             

  fixed in (shorttened lines and removed unnessasary whitespace in validation.py)                   
                 
### PART 2 — Function-by-Function Review                           
                      
- 1 read           

    lLooking at it through the lens of “is it doing too much” does show me I could have split it into two parts, but I'm unsure of how practical that would be. I do see its doing two jobs, one is checking to see if there is a file and the other is actually opening the file. 

    As I am writing this, I did just have an idea that I'm going to try out in v2. I could try to make a function for checking if a file exists and use it across both the opening of the input and output file. That would cut down on code re-use significantly if I could get it to work. 
    

    I do think the name could be more explicit as I'm now really seeing that all my function names just lightly reflect their usage. 


    I think the main thing I'd be embarrassed by is the heavy use of try and except to check if a file is present. It came to my attention that putting that much code in try is bad practice. Plus, I think there must be a more “graceful” way to verify the presence of a file. 

- 2 validate

    It’s doing one job split into two parts that I feel would be impractical to split. It's checking for good data and logging the bad.

    as mentioned above i think all my functions could be more explicit.

    I have a number of things here that I'm a bit embarrassed by. I've already talked ad nauseam about the less than tight validation logic, but I'm also a bit iffy on the giant if chain. Even though I designed it that way on purpose to trigger an exception in the event of just one part of the row is bad. It just looks like there's a cleaner way. There’s also the extreme reliance on try except again. I can't help but feel like I could have used better options here all around. 

- 3 prossess

    This one I'm unsure on. I mean all its doing is taking the data that was output from validate and inserting it into the output file but it's also checking for the presence of the file therefore I should yet again be able to split it up a bit more. 

    This one could be clearer as well as right now I think a more apt name would be insert_sql or something along those lines. 

    The main thing I'm somewhat embarrassed by here would have to be the codes repetitive nature. not just in itself but between itself and read. If I could somehow split it up into several parts, I think that would be a good thing to try and do as it would cut down on code repetition. that and the try, except again. 

### PART 3 — Error Handling Audit

- 1 User inputs invalid input file in excell_open.py

    Is handled by prompting user to re input file path 

- 2 Couldn't open a db / no db found in user input output directory 

    Is handled by prompting the user, asking if they want to create one

    If user selects no they will be asked again to input output directory

    Could add a quit option here as well this way if it's not a user error and some computer issue. the user can close the tool fix it and come back later 

- 3 Missing/mismatched column headers in input file

    Currently no error handling outside of it automatically failing the row the moment it reaches the column in question in the validation step. 

    Pretty sure there is a better way to handle it, but it doesn't cause a hard crash and does instruct the user to check the sheet. 

    Is not in my sprint plan and as of right now and it doesn't pose any risks to the tools function. An error handler for another process covers it. It could just be handled more gracefully. 

- 4 miss matched headers in target output file

    Currently there is partial error handling here as the part of the code that attempts to append information to a preexisting db will fall back on creating a new db if it fails to run properly. 

    Currently not in my sprint plan. 

    The partial error handling should be able to keep it running stable with no bad data getting through to the database. still should add some sort of quit option like in the previous item, to give the user a chance to investigate the issue before coming back. At this point it is probably best to keep it as is. 

- 5 unable to access user input output directory on SQL_output step line 91 

    Currently no error handling here whatsoever.  

    It is not in my sprint plan. 

    Is not important to data integrity but I feel it is also important to try to make it run as smooth as possible. But for underlying functionality I think it's best to leave it off my sprint plan for now. 

- 6 unable to write into operations log 

    Currently no error handling here. 

    Not in my sprint plan. 

    Will add to it as I feel it's important for the user to have the operations log on hand. 
