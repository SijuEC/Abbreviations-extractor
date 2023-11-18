# Importing the required libraries
import re
import pandas as pd

file = open("file.txt") # Opening a .txt file where the text to be analysed resides

word_list = []
content = file.readlines()
for line in content:
    words = line.split()
    for word in words:
        if re.match(".+[A-Z]+[A-Z]", word): # This will select all th words that have consecutive capital letters
            word_list.append(word)

# Removing opening and closing brackets
for i in range(len(word_list)):
    word = word_list[i]
    word = word.replace("(", "")
    word = word.replace(")", "")
    word_list[i] = word

# Writing all the abbreviations into an excel file
list_of_abrv = list(dict.fromkeys(word_list))
df = pd.DataFrame(list_of_abrv)
df.to_excel("abr_list.xlsx", index=False)

