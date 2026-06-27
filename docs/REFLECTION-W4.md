# WEEK 4 PROGRAMMING REFLECTION                            
**what does your v1 do well**                                
                                         
I think I did a verry good job on a user experience front. As someone who used to hate command                                                                        
line utilities a while back I tried my best to make this tool verry approachable, giving                                   
ample instruction to the user and prompting the user that a no database was                                                      
found before asking if they want to create one.                                                                 
                                                                                                           
I also tried to give ample feedback in the log file. And unless I forgot that I removed it,                            
I left in a bit of debug print text as I found it useful from a user standpoint which                                
shows from 1st to last which rows of the excel file passed and failed as the program runs.                                            
                                                      
eg                                           
row 0 sucsess                                   
row 1 sucsess                                       
row 2 sucsess                                
row 4 sucsess                                   
row 7 sucsess                               
                                                                                                                
looking at it i could make it more useful by showing which ones                                                 
failed as well like I said this was originally debugging text hap                                                 
hazardly thrown together so i could test the pass-fail function                                            
                                                           
**PEP 8 rules I broke**                                                         
                                                                           
1 Indentation                                                                     
                                                                                                   
Right on the landing page I saw one that surprised me. I'm used to tabbing once but I'll have                                                                  
to get used to tabbing twice as apparently that's better practice in python when you do an indent                             
                                                            
2 limit try: except: to minimum amount of code possible                                                           
                           
I used allot of code in try: clauses which I was originally proud of for being able to use it to test                      
if a file was present, but apparently its better practice to not use allot of code in try statements.                       
                                          
**what was the three weakest point**                                 
                                                 
1 Data verification,                                         
                                               
This is the one that bugs me the most as I know there are some ways I could make it more watertight,                                  
but either I can't articulate it or I’m just not seeing it. The main one is checking to see if an employee                           
ID already exists. As the tool sits, if a field exists it will cause a full crash on the data insertion step.                           
                                              
On the other hand, I could just be being too hard on myself because allot of it could be me seeing that it will accept                     
"reiwujbfn" as a valid name input, And it kinda bugs me. And I don't know if it should accept numbers in the name field                 
                             
2 optimization                                             
                                   
I know there are optimizations that can be made. one that really bugs me is yet again, the data verification step. As it is,                                  
I have the check to see if its valid and the check to see which step it failed sperate. Right now, it's done this way for ease                         
of programming as adding an else statement would cause the try statement to never fail. I don't have anything solid on working                          
around that, but I have ideas and I will probably be changing that later, but I know there were more things I could have done better                      
                                         
3 spelling and grammar                                                  
                                                           
Weird one for a college student I feel but spelling and grammar was never my strong suit. It is mostly on display in my                                       
comments but in a professional setting the comments should still be kept neat I feel. I think this should still be something                             
I try to work on. weirder still my informal typing style slipped in a couple times like the use of 'u' instead of 'you'.                            
                                       
**what dose code quality mean to me**                                           
                                 
I feel there are three things I focus on when making good quality code                         
                               
1 stability                            
                                   
I feel the ability of the code to operate well and operate as intended under most conditions is the number one priority when making              
quality code. For example, if it looks like it runs but outputs an invalid output, its running fine but it's not fulfilling its purpose.              
                                 
2 neatness/readability                            
                                   
My second priority is writing code that can be read and understood at a glance. This is good for maintenance and long-term programming projects. I               
vividly remember when I was first learning JavaScript a long time ago thinking “I'll remember how this works” and lo and behold I didn't remember.                
Readability is one of the main influences of my programing style with ample spacing between lines and nearly every line of code commented.            
                                          
3 runs well on target hardware                                             
                                                            
This runs parallel with number 2 in my mind as yes optimization is a priority, but I feel like it shouldn't overtake readability if                   
it doesn't affect performance. For example, I currently have the verification step and insertion step separate in my program. I know it                    
would be better optimization wise to do it all in one step and not send the data to main.py and then to SQL_out.py, but I feel                     
it's easier to manage and understand this way and it runs fine as is.             
                                               
I do ask you to let me know if I’m off base with number 3 as this is an "epiphany?" that set in not too long ago.                          
                                                                                                
I feel like balancing all three of these things are my personal priority when writing code.                                           