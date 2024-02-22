student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    #print(value)
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    #print(row.student)
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
nano_words = pandas.read_csv('nato_phonetic_alphabet.csv')
words = []
for index,row in nano_words.iterrows():
    words.append(row)
dict_phonetic = {words[i].letter:words[i].code for i in range(len(words))}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input("Enter your name: ").upper()
user_phonetic = [dict_phonetic[letter] for letter in user_input]
print(user_phonetic)
