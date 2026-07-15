| Test ID | Category | Description | Input | Expected Output | Actual Output | Pass/Fail |
|---------|----------|-------------|-------|-----------------|---------------|-----------|
| TC-001  | Normal   | mixed batch of valid and invalid data | sample(1).xlsx (5 valid 5 invalid) | 5 rows inserted, 5 rows rejected | ... | ... |
| TC-002  | Normal   | valid data with zero as input in id and sale value | sample(2).xlsx | all rows passed | ... | ... |
| TC-003  | Normal   | invalid input in form of various field types | sample(3).xlsx | bad data should be rejected gracefully  | ... | ... |
| TC-004  | Normal   | input with data missing from optional data fields | sample(4).xlsx | optional fields should be passed as null | ... | ... |
| TC-005  | Edge     | output file has some fields but not all | sample(5).xlsx | should prompt user to create fields or gracefully stop | ... | ... | 
| TC-006  | Edge     | input file headers but no data | sample(6).xlsx | should run cleanly with 0 files processed | ... | ... | 
| TC-007  | Edge     | input has text fields with abnormal characters | sample(7).xlsx | depending on characters will reject fields | ... | ... | 
| TC-008  | Edge     | Input file has extra columns | sample(8).xlsx | should use the valid columns | ... |sample(9) ... |
| TC-008  | Edge     | input file has duplicate id but has updated data | sample(10).xlsx | should append to file | ... | ... |
| TC-009  | Error    | invalid input file type | sample(11).xlsx | should gracefully reject input or re-prompt for user input | ... | ... |
| TC-010  | Error    | invalid output file type | sample(12).xlsx | should gracefully reject output or re-prompt for user input | this one had me facinated, for a bit i was starting to think that it didnt cade about extension which is partly right, it only cares about the data in a file. if the data in the file is improperly formatted it will ask to create the schema, the failes if you slecet yes, it will reprompt the user to input a new file location, if the user tries to input the same file it crashes. otherwise an empty .jpg file is as valid as anything else to the program | ... |
| TC-011  | Error    | Nonexistent file path for log file | sample(13).xlsx | should create path | processess files but crashes on the creation of log file | fail |
| TC-012  | Error    | Headers non existent in input file | sample(14).xlsx| should gracefully stop with user error | procsesses data with 0 input | pass |
  