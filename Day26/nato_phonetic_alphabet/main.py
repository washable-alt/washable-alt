student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

import pandas as pd
import csv

student_data_frame = pd.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    print(index, row)
    print(row.student)
    print(row.score)

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. :
#Create a dictionary in this format:
#{"A": "Alfa", "B": "Bravo"}

dictionary = {}

## CSV method
with open(".\\Day26\\nato_phonetic_alphabet\\nato_phonetic_alphabet.csv", 'r') as f:
    
    reader = csv.reader(f)
    # Skips the header row
    next(reader)
    for row in reader:
        letter, code = row
        dictionary[letter] = code
print(dictionary)


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

#try:
#    data = pd.Series(dictionary).to_frame()
#    print(data)
#except Exception as e:
#    print(e)

word = input("Enter a word: ").upper()
output_list = [dictionary[letter] for letter in word]
print(output_list)