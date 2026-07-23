- **QUESTION 1**                                         

    I think the thing that the most significant thing I "learned" during this course was being able to practice my problem solving skills. I put quotes around it because I feel its not something that you can fully be taught and is something that you practice and learn along the way. You can teach problem solving practices but the bulk of it is critical thinking which is best to be practiced than taught. Another thing I'm going to take with me going forward is to be more Liberal in using try except in my decision structure because it made debugging a nightmare. 

    I think the most significant thing I built was the log output portion of main.py. At the time i was building the log output portion in v1 I didn't know how I was going to work that out. I needed to have it output to a single folder consistently regardless of terminal location. but I'm very happy about the idea of using the main.py file as a landmark of sorts and using pathlib to get main.py's location. It still doesn't quite work as expected if the terminal is outside of the tool folder but I think the idea still has merit.

    I think just allot of function usage and sending and receiving variables through them was a bit confusing from the last course I took in python. But having more hands on experience with them in a sort of real world scenario in python cleared up allot about how they work among other things. 

- **QUESTION 2**
YES, definetly. i feel that this sort of design cycle is now my preferd aproch for large projects. i think the main thing where the proccess helped whas when it showed the fact that the reprompt logic was severilly flawed when i wasnt even testing for it i was verry supprised when i found that issue.

- **QUESTION 3**

    - **problem 1**
    the first major problem was the fact that it crashed if the first reprompt failed as mentioned above. it was actually a fairlly easy fix. there was a second bit of code in the excel_open file which was probably a hold over from the originall input funcitonality in v1.0. it would fail and drop into a while loop when it failed, this overcomplicated the whole thing and changing it to try to open in the while loop fixed the issue. 

    this improvment matters as one of my goals for this project was to make the tool as user friendly as posible and part of that goal was to walk the user through the proccess and the re-prompts were part of that. and having this feature failling like this goes against the entire point of that goal

    - **problem 2**

    the second most inportant improvment has to be the addition of apending data of like IDs, it may of been outside of the scope of the original project but i felt it was important enough to add to the tool, because it makes the tool better at its job rather than it being another feature, this way it can be used to not just add data but keep it up to date, i adressed it by changing the id check step to be last and while its being checked it will see if its present if it is it will check to see if the name matches to any in the database, if so it appends the entry in the databse if not it skips it.

    again i feel this was important because its important to not just add data but also keep it up to date.

    - **problem 3**

    the last problem i can think of would have to be tightening data varification and this one was tricky because what counts as "done" when you talk about somehting like this, and i just ended up saying list off all the things that come to mind when thinking aobut what shouldnt be in the feilds so i ended up checking for thos things and when i implemented those checks that was done.

    i feel its important to have the program do what it reasonably can to keep the data going into the database clean and not just in terms of valid data types like ints floats and the like. if it was a genral puropse program that turns all excel sheats into SQL databases then maby id be a little looser on the data varification

- **QUESTION 4**

if i had more time id defenitly try my hand at making a modified verson for more genrall use one that detects headers and cunstructs the SQL schema based on that but thats a more personall project kind of thing, good for a resume too 

but in terms of this tool in particular id say i noticed (and put in limitations as well) that it dosnt handle duplicate IDs in the same excel sheet well and hard crashes

i also noted that my solution for wiritng the log no mater where the terminal is oppend disnt quite work as expected so id also fix that 

id also try to loosen the dependency i curently have on try in terms of my desicion structer a bit

i know there are other ideas i had but the arent coming to mind as i write this

- **QUESTION 5**

    - followed a multi month programming project through to completion 

    - trouble shooted programming faults with teamwork

    - trouble shooted programming faults with criticall thinking

    - have experience with the scrum planning process including sprint planning, minimising scope creap, and test planning