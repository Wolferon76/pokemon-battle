
print("")
print("                                  ,'\\")
print("    _.----.        ____         ,'  _\   ___    ___     ____")
print("_,-'       `.     |    |  /`.   \,-'    |   \  /   |   |    \  |`.")
print("\      __    \    '-.  | /   `.  ___    |    \/    |   '-.   \ |  |")
print(" \.    \ \   |  __  |  |/    ,','_  `.  |          | __  |    \|  |")
print("   \    \/   /,' _`.|      ,' / / / /   |          ,' _`.|     |  |")
print("    \     ,-'/  /   \    ,'   | \/ / ,`.|         /  /   \  |     |")
print("     \    \ |   \_/  |   `-.  \    `'  /|  |    ||   \_/  | |\    |")
print("      \    \ \      /       `-.`.___,-' |  |\  /| \      /  | |   |")
print("       \    \ `.__,'|  |`-._    `|      |__| \/ |  `.__,'|  | |   |")
print("        \_.-'       |__|    `-._ |              '-.|     '-.| |   |")
print("                                `'                            '-._|")
print("")
print("Pokemon Battle")
print("")

import json
import random

# read Pokemon file into dictionary
pokemons_file = open('pokemons.json') # opening JSON file
pokemons = json.load(pokemons_file) # returns JSON object as a dictionary
pokemons_file.close() # Closing file

print(pokemons[0])

while True:
    print("1. Show pokemon by index")
    print("2. Top 10 strongest pokemons (by total)")
    print("3. Top 10 weakest pokemons (by total)")
    print("4. Battle of 2 pokemons")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        x = int(input("Write pokemon index: "))
        x = x - 1
        print(pokemons[x])
        print(x)
        # https://www.w3schools.com/python/python_dictionaries_access.asp
        pass
    elif choice == '2':
        def sort_total(pokemon):
            return int(pokemon["total"])
        pokemons.sort(key = sort_total, reverse = True)
        print(pokemons[:11])
        # https://www.w3schools.com/python/python_lists_sort.asp
        pass
    elif choice == '3':
        def sort_total(pokemon):
            return int(pokemon["total"])
        pokemons.sort(key = sort_total, reverse = False) 
        print(pokemons[:11])
        # https://www.w3schools.com/python/python_lists_sort.asp
        pass
    elif choice == '4':
        x = int(input("Write pokemon index: "))
        x = x - 1
        My_choose = pokemons[x]
        print("Player 1(your) pokemon: ", My_choose)
        

        Computer_choose = random.choice(pokemons)
        print("Player 2 pokemon: ", Computer_choose)

        player_1_damage = My_choose["attack"] - Computer_choose["defense"] + random.randint(5, 20)
        player_2_damage = Computer_choose["attack"] - My_choose["defense"] + random.randint(5, 20)
        print("Player 1 damage player 2:", player_1_damage, "points.")
        print("Player 2 damage player 1:", player_2_damage, "points.")
        




        # Battle
        # 
        # https://www.w3schools.com/python/ref_random_choice.asp - random choice
        # Computer choosing one random Pokemon from list
        # Player choosing by entering Pokemon index
        # Damage is calculated by: (attack of Pokemon 2) - (defense of Pokemon 1) + (random from 5 to 20), and vice-versa
        # Player reaching 0 health (total) - lost
        pass

    elif choice == '5':
        print("Exiting")
        break
    else:
        print("Invalid choice, choose from 1 to 5")

    print("==========================")


