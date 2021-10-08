# Amar Nagim
# F1.6.02.O3 - Set met kaartenFuncties
def cards():
    import random
    count = 0
    colors = ['harten', 'klaveren', 'schoppen', 'ruiten']
    cardKind = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'boer', 'vrouw', 'heer', 'aas']
    cardList = ['joker', 'joker']
    for cards in range (52):
        randomColors = random.choice(colors)
        randomKind = random.choice(cardKind)
        joined = (f'{randomColors} {randomKind}')
        cardList.append(joined)
    print('\nDeck(54):', ", ".join(cardList) + "\n")
    print('Shuffling deck of cards...\n')
    random.shuffle(cardList)
    print('Deck shuffled(54):', ", ".join(cardList) + "\n")
    for randomPick in range (7):
        randomPickResult = [cardList[count]]  
        count+=1
        print(f'Kaart {count}: {(",".join(randomPickResult))}')
    cardListSeven = cardList[7:]
    print('\nRemaining deck of cards(47):', ", ".join(cardListSeven))

cards()    