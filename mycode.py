import pandas as pd 
import os

#very simple dict
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25,30,35],
    'City': ['New York', 'Log Angeles', 'Chicago']
}

#coverts dict to dataframe

df = pd.DataFrame(data)




# Adding new row to the df for data version 2 

new_row_loc = {'Name':'GF1', 'Age':20, 'City': 'Cty1'}
df.loc[len(df.index)] = new_row_loc


# Adding new row to the df for data version 3 
new_row_loc2 = {'Name':'GF1', 'Age':30, 'City': 'Cty2'}
df.loc[len(df.index)] = new_row_loc2



#ensures that the data dir exists at the root level
data_dir = 'data'
os.makedirs(data_dir, exist_ok = True) #exist_ok if the folder already exists with the same name then it will not create a new folder with the same name

#define the file path 
file_path = os.path.join(data_dir,'sample_data.csv')

#save the DataFrame to a csv file, including column names
df.to_csv(file_path, index = False)
print(f"CSV file saved to {file_path}")