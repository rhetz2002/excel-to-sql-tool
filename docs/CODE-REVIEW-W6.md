## Code Review                 

### PART 1 — PEP 8 Compliance Check                       
                                    
had allot about white space and line length,                           
tried to get as many 'interesting' ones as posible                             
                                  
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
  corected:                                  
            log = log + f'{time.strftime("%I:%M:%S %p")}: row {index} ' \                              
                            f'fail on department check, pleas check that ' \                       
                            f'feild contains vaild department\n'                             
  fixed in (shorttened lines and removed unnessasary whitespace in validation.py)                   
                 
### PART 2 — Function-by-Function Review                           
                      
- 1 read()           

    looking at it through the lense of is it doing to much does show me i could of split it into two parts but im unsure of how paractical that would be.
    I do see its doing two jobs one is opening seeing if there is a file and the other is opening the file.

    as im writing this i did just have an idea on this that im going to try out in v2 i could try to make a function for checking if a file exsists and use it across both the opening of the input and output file

    that would cutdown on code used significantly if i can get it to work 
    


    im not sure about name alone but i think the developer would be able to tell from its usage plus the name but i could rename it to be more explsiit



    i think the main think id be embarised by the HEAVY use of try and except to check if a file is present as it came to my atention that puting that much code in try is bad practice

- 2 validate()

    i think its safe to say that its doing one job split into two parts. its checking if its good data and loging the bad

    i think this ones name could be more explisit. now that i think of it both this and read could be more explicit as they reflect there usage but dont tell what they're "reading" or "validating"

    i have a number of things here that im a bit embarised by. iv alredy talked ad nauseam about the less than tight validation but im also a bit iffy on the giant if chain
    
    even though i designed it that way on purpose to trigger an exception it just dosnt look nice also the extreem relience on try except again. i cant help but feel like i could of used another better option here 

- 3 prossess()

    this one im unsure i mean all its doing is takeing the data that was output from validate and inserting it into the output file but its also checking for the presence of the file so i could yet again split it up a bit more 

    this one could be clearer as well as rn i think a more apt name would be insert_sql or something allong those lines

    the main thing im somewhat emberrised by here would have to be the codes repetitive nature not just in itself but between itself and read() if i could somehow split it up into several parts i think that would be a good thing to try and do that and the try, except again

### PART 3 — Error Handling Audit

- 1 user inputs invalid input file in excell_open.py

    is handeled by prompting user to re input file path

- 2 couldnt open a db / no db found in user inputed output directory

    is handled by prompting the user, asking if they want to create one

    if user selects no they will be asked again to input output directory

    could add a quit option here as well as a way to close the tool in the event
    that its an issue with acsess so they can fix it and come back to it

- 3 missing/missmatched coloumn headers in input file

    curently no error handelling outside of it automatically failling the row the moment it reaches the couloumn in question

    prety sure there is a better way to handle it but it dosnt cause a hard crash and does instruct the user to check the sheet

    is not in my sprint plan and as of right now it dosnt pose any risks to the tools function, as an error handeller for another process covers it it could just be handelled more gracefully

- 4 miss matched headers in target output file

    curently there is partal error handelling here as the part of the code that atempts to append infromation to a pre exsisting db will fall back on creating a new db if it fails to run properlly

    curently not in my sprint plan

    the partal error handelling should be able to keep it running satable with no bad data geting through to the database. still should add some sort of quit option like in the previous item, to give user chance to investigat the issue before comeing back at this point probably best to keep it as is

- 5 unable to acsess user input output direcotry

    curently no error handelling here whatsoever 

    is not in my sprint plan 

    is not important to data integrity but i feel it is also important to try to make it run as smooth as posible but for underlying funcunaltiy i think its best to leave it off my sprint plan for now

- 6 unable to write into operations log 

    curently no error handelling here

    not in my sprint plan

    will ad as i feel its important for the user to have the operations log on hand
