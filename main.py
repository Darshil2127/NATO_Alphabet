import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
# data.iterrows() means access of rows in csv as letter and code
new_dict = {row.letter:row.code for (index,row) in data.iterrows()}

word = input("Enter a word = ").upper()

nato = [new_dict[letter] for letter in word]
print(nato)