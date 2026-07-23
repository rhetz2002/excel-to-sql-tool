- **QUESTION 1**                                         

    I think the thing that the most significant thing I "learned" during this course was being able to practice my problem solving skills. I put quotes around it because I feel its not something that you can fully be taught and is something that you practice and learn along the way. You can teach problem solving practices but the bulk of it is critical thinking which is best to be practiced than taught. Another thing I'm going to take with me going forward is to be more Liberal in using try except in my decision structure because it made debugging a nightmare. 

    I think the most significant thing I built was the log output portion of main.py. At the time i was building the log output portion in v1 I didn't know how I was going to work that out. I needed to have it output to a single folder consistently regardless of terminal location. but I'm very happy about the idea of using the main.py file as a landmark of sorts and using pathlib to get main.py's location. It still doesn't quite work as expected if the terminal is outside of the tool folder but I think the idea still has merit.

    I think just allot of function usage and sending and receiving variables through them was a bit confusing from the last course I took in python. But having more hands on experience with them in a sort of real world scenario in python cleared up allot about how they work among other things. 

- **QUESTION 2**
    
    YES, definitely. I feel that this sort of design cycle is now my preferred approach for large projects. I think the main thing where the process helped was when it showed the fact that the re-prompt logic was extremely flawed when I wasn't even testing for it I was very surprised when I found that issue. I really like this approach because of its iterative design approach. Building the bare bones testing what works and building off of that.

- **QUESTION 3**
                    
    - **problem 1**

    The first major problem was the fact that it crashed if the first re-prompt failed as mentioned above, it was actually a fairly easy fix. There was a second bit of code in the excel_open file that I removed to fix the issue. It was probably a hold over from the original input functionality in v1.0 where it would prompt the user after main.py is run rather than how it runs now where you insert the files as you type out the command to run the program. it would fail and drop into a while loop after it failed, this over complicated the whole thing and changing it to try to open in the while loop fixed the issue. 

    This improvement matters as one of my goals for this project was to make the tool as user friendly as possible. Part of that goal was to walk the user through the process and the re-prompts were part of that. Having this feature failing like this goes against the entire point of that goal.

    - **problem 2**

    The second most important improvement has to be the addition of appending data of like IDs. It may of been outside of the scope of the original project but I felt it was important enough to add to the tool, plus I had time as you can see. It makes the tool better at its job rather than it being another feature, this way it can be used to not just add data but keep it up to date. I addressed it by moving the id check step to the last position in the verification chain. While its being checked it will see if its present, if it is it will check to see if the name matches to any in the database, if so it appends the entry in the database if not it skips it.

    Again I feel this was important because its important to not just add data but also keep it up to date.

    - **problem 3**

    The last problem i can think of would have to be tightening data verification. This one was tricky because what counts as "done" when you talk about something like this. I just ended up listing off all the things that come to mind when thinking about what should and shouldn't be in the fields. Then I made the program check for those requirements that was what I considered done in this case.

    I feel its important to have the program do what it reasonably can to keep the data going into the database clean and not just in terms of valid data types like ints floats and the like. If it was a general purpose program that turns all excel docs into SQL databases then maybe I'd be a little looser on the data verification.

- **QUESTION 4**

    If I had more time I'd definitely try my hand at making a modified version for more general use. One that detects headers and constructs the SQL schema based on that, but that's a more personal project kind of thing. I think it'd be a good portfolio item too. 

    But in terms of this tool in particular id say i noticed (and put in limitations as well) that it doesn't handle duplicate IDs in the same excel sheet well and hard crashes.

    I also noted that my solution for writing the log no mater where the terminal is opened doesn't quite work as expected so I'd also fix that. 

    I'd also try to loosen the dependency I currently have on try in terms of my decision structure a bit.

    I know there are other ideas I had but the aren't coming to mind as I write this.

- **QUESTION 5**

    - Followed a multi month programming project through to completion.  

    - Troubleshooted programming faults with teamwork. 

    - troubleshooted programming faults independently with critical thinking.

    - Have experience with the scrum planning process including sprint planning, minimising scope creep, and test planning.

    side note this programming project has somewhat given me the want to experiment more so I'm thinking of trying to learn C# next so i can experiment in the unity engine