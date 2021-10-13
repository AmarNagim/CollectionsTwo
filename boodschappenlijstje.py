# Amar Nagim
# F1.6.02.O2 - Boodschappenlijstje


print("""
=================================================
Typ hier de artikelen voor uw boodschappenlijstje
=================================================
""")

groceryList = []

again = 'j'
while again != 'n':
        item = input('Typ hier een product in: ')
        groceryList.append(item)
        again = input('Wil je nog een product toevoegen? J/N: ').lower()
        while again != 'j' and again != 'n':
                print('Sorry, dit begreep ik niet..')
                again = input('Wil je nog een product toevoegen? J/N: ').lower()
                        


    

result = dict((i, groceryList.count(i)) for i in groceryList)


if again == 'n':
    print('\n================================')
    print('    Uw boodschappenlijstje')
    print('================================')
    print("\n".join(f"{key} x{value}" for key, value in result.items()))
    print('================================')
    