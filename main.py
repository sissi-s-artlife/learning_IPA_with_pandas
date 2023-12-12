import pandas as pd
#import dataframe
from dataframe import df

# Step 3: Write the DataFrame to a CSV file.
csv_path = 'df.csv'
df.to_csv(csv_path, index=False)


df = pd.read_csv(csv_path)
loop_is_on=True
while loop_is_on:
    type_check=input("If you want to check an IPA symbol type 'IPA' if you want to check a sound type 'SOUND': ").upper()
    if type_check=="IPA":
        print(df[df['IPA Symbol'] == input("Input the IPA symbol you want to check: ").lower()])
    elif type_check == "SOUND":
        print(df[df['Sound'] == input("Input the sound you want to check: ").lower()])
    else:
        print("You typed an invalid value.")
    end_cont=input("Do you want to end the checking or continue. If you want to continue type 'continue' if you want to end it type 'end': ").lower()
    if end_cont=='end':
        loop_is_on=False
    else:
        loop_is_on=True












