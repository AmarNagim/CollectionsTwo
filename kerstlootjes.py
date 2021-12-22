import random

print('Welkom bij kerstlootjes.\n')


def nameLoop():
    count = 1
    usersValidation = True
    userList = []
    while usersValidation:
        users = input(f'Vul hier de naam in van deelnemer {count}: ')
        userList.append(users)
        count+=1
        yesNo = input('Wil je nog een naam toevoegen? Y/N: ').lower()
        if yesNo == 'n':
            usersValidation = False
        elif yesNo == 'y':
            pass    
        else: 
            print('Ik heb u Helaas niet begrepen')
    return count, usersValidation, userList, yesNo, users

count, userValidation, userList, yesNo, users = nameLoop()
print(userList)
count2 = 1
listPosition = 0
amountUsers = count-2
print(amountUsers)
while len(userList) > 0:
    randomPick = random.randint(count2, amountUsers)
    print(randomPick)
    pull = print(f'\n{userList[count2]} trekt een lootje..\n')
    count2+=1
    listPosition+=1
    print(f'Op het lootje staat.. {userList[randomPick]}')
    userList.pop(randomPick-1)
    continueOrNot = input('Druk ENTER om door te gaan naar de volgende deelnemer..')
        