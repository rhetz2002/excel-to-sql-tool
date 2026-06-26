import pandas as pd

#defines vaildate function
def validate (data):

    
    
    # iterates through the data taken from excell file
    # loops for the index and row
    bad_rows = []
    print ("rows processed")
    for index, row in data.iterrows():

        # sees if is int or int adjacent
        
        try: 
            
            # thuroughly checks to see if its missing any important data or formated incorectly

            if pd.notna(row['ID']):
                if pd.notna(row['name']):       
                        if pd.notna(row['email']):
                            if int(row['ID']):
                                if str(row['name']):
                                    if float(row['sales']):
                                        if '@' in str(row['email']):
                                            if str(row['department']) in ['sales', 'customer service']:
                                                print(f"row {index} sucsess") 
        
        # if fails check, stores index in list to be removed at end
        # also prints which row pass and fail                                
        
        except ValueError:
            bad_rows.append(index)
            print(f"row {index} fail") 

    # stores passing data in clean        
    
    clean = data.drop(bad_rows, axis=0)
    
    # returns clean
    return clean, log

            