 | Defect ID | Description | Steps to Reproduce | Severity | Status | Fix Commit |
  |-----------|-------------|--------------------|----------|--------|------------|
  | D-001 | Tool crashes if a reprompt fails to open a present file | point tool to an invalid input/output input an invalid input/output on the re-prompt | High |fixed|d836b98|
  | D-002 | tool fails to pass rows with missing department entries | input a file with missing department entries | med |fixed| e2ee3a3 |
  | D-003 | tool fails to append rows with same ids even if data is difrent, causes crash | input file with id matching id in db | high |Open| ... |
  | D-004 | tool gets confused when a table matching the desired output is missing feilds, if the table in the output location has the same name as the desired table but not the required headers, it will ask to make the schema then crash | try to output to a table mathcing the name of the desierd table but missing proper coulumns | high |Open| ... | 
  | D-005 | tool crashes if it cant find the output path for log file | run the tool from a location that dosnt match the log output path | high | fixed |20545ba|
  | D-006 | tool fails to verrify rows if the sales entry has any whitespace | input a file where a sales entry has whitespace before or after the string | low | fixed | e2ee3a3 |