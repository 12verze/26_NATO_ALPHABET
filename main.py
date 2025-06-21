import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
nato = {value.letter:value.code for (key,value) in data.iterrows()}

#print(nato)
def magic():
    word = input("Enter a word\n").upper()
    try:
        list = [nato[letter] for letter in word]
    except KeyError:
        print("Please enter only Alphabets")
        magic()
    else:
        print(list)

magic()














