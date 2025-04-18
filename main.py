"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Michal Matějíček
email: matejicekmichal@seznam.cz
"""
TEXTS = [
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',
    '''At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.''',
    '''The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.'''
]
users = {"bob": "123", "ann": "pass123", "mike": "password123", "liz": "pass123"}
name = input("Please enter your username\n")
password = input("Please enter your password\n")
separator = "-" * 40

if users.get(name) == password:
    message = (f"username: {name}\npassword: {password}")
    print(f"{message}")
else:
    message = (f"username: {name}\npassword: {password}")
    print(f"{message}\nunregistered user, terminating the program.")
    quit()

print(separator)
print(f"Welcome in the app, {name}.")
print(f"We have {len(TEXTS)} texts to be analyzed.")
print(separator)

selection = input(f"Enter a number btw. 1 and {len(TEXTS)} to select: ")
print(separator)

if not selection.isdigit() or not (1 <= int(selection) <= len(TEXTS)):
    print(f"There is no text for this number: {selection}, terminating the program.")
    quit()
else:
    count = (len(TEXTS[int(selection) - 1].split())) 
    index = int(selection) - 1   
    print(f"There are {count} words in the selected text.")

    words = (TEXTS[int(selection) - 1].split())
    capital_letter = 0
    all_capital_letter = 0
    small_letter = 0
    number = 0
    sum_number = 0

    for word in words:
        if word and word[0].isupper() and not word.isupper():
            capital_letter = capital_letter + 1
    
        if word.isupper():
            all_capital_letter = all_capital_letter + 1
    
        if word.islower():
            small_letter = small_letter + 1
    
        if word.isnumeric():
            number = number + 1
    
        if word.isnumeric():
            sum_number = sum_number + int(word)

    print(f"There are {capital_letter} titlecase words.")
    print(f"There are {all_capital_letter} uppercase words.")
    print(f"There are {small_letter} lowercase words.")
    print(f"There are {number} numeric string.")
    print(f"The sum of all the numbers {sum_number}.")

    clear_words = []
    for word in words:
        cleaned_words = word.strip(",.:;'!?")
        clear_words.append(cleaned_words)
        length_word = [len(word) for word in clear_words]
        length_count = {}
        for length in length_word:
            if length in length_count:
                length_count[length] = length_count[length] + 1
            else:
                length_count[length] = 1
    print(f"{separator}\n{"LEN".center(3)} | {"OCCURENCES".center(18)} | {"NR.".center(3)}\n{separator}")
    for length, count in sorted(length_count.items()):
        stars = "*" * count
        print(f"{str(length).center(3)} | {stars:<18} | {str(count).center(3)}")
        