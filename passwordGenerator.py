# Amar Nagim
# F1.6.02.O4 - Password GeneratorFuncties

import random
import time

lettersList = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
specialCharactersList = ['@','#','$','%','&','_','?','.']
numbersList = ['1','2','3','4','5','6','7','8','9']

capitalLettersList = []
specialCharactersChoiceList = []
numbersChoiceList = []
smallLetterChoiceList = []

capitalLetters = random.choice(range(2,6))
for letters in range(capitalLetters):
    letterChoice = random.choice(lettersList)
    capital = letterChoice.upper()
    capitalLettersList.append(capital)


for randomSpecialCharacters in range(3):
    specialCharacters = random.choice(specialCharactersList)
    specialCharactersChoiceList.append(specialCharacters)
    

times = random.choice(range(4,7))
for numbers in range(times):
    digitsChoice = random.choice(numbersList)
    numbersChoiceList.append(digitsChoice)



total = capitalLettersList+specialCharactersChoiceList+numbersChoiceList
count = len(total)
smallLetters = 24-int(count)

for smallLetters in range(smallLetters):
    smallLetterChoice = random.choice(lettersList)
    smallLetterChoiceList.append(smallLetterChoice)



# print(capitalLettersList)
# print(specialCharactersChoiceList)
# print(numbersChoiceList)
# print(smallLetterChoiceList)

totalsum = total + smallLetterChoiceList

random.shuffle(totalsum)

while totalsum[0] in specialCharactersList or totalsum[-1] in specialCharactersList or totalsum[0] in numbersList or totalsum[1] in numbersList or totalsum[2] in numbersList:
    print(totalsum)
    random.shuffle(totalsum)
    print('special characters on first or last spot')


print('This is your 24 character password=', "".join(totalsum))

