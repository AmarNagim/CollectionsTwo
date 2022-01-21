import random

print('Welkom bij kerstlootjes.\n')

def nameLoop():
    count = 1
    usersValidation = True
    userList = []
    while usersValidation:
        users = input(f'Vul hier de naam in van deelnemer {count}: ')
        while users in userList:
            users = input(f'Er bestaat al een lootje met deze naam, vul alstublieft een andere naam in voor deelnemer {count}: ')
            
        userList.append(users)
        count+=1
        if (count % 2):
            yesNo = input('Wil je nog een naam toevoegen? Y/N: ').lower()
            if yesNo == 'n':
                usersValidation = False
            elif yesNo == 'y':
                pass    
            while yesNo != 'y' and yesNo != 'n':
                        print('Ik heb u Helaas niet begrepen')
                        yesNo = input('Wil je nog een naam toevoegen? Y/N: ').lower()
                        if yesNo == 'n':
                            usersValidation = False
                        elif yesNo == 'y':
                            pass    
    return count, usersValidation, userList, users

count, userValidation, userList, users = nameLoop()
random.shuffle(userList)

def randInt():
    amountNames = len(userList)-1
    randomInt = random.randint(0, amountNames)
    return randomInt

while len(userList) >= 2:
    # print(userList)
    number = randInt()
    numberName = userList[number]
    userList.pop(number)
    number2 = randInt()
    number2Name = userList[number2]
    userList.pop(number2)
    print(f'\n{numberName} heeft {number2Name} getrokken\n')
    input('Druk ENTER om door te gaan\n')
    
    
