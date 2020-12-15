#Animal population game
#V0.7
#Credits: Atkin, Sir.burton, Leo

import time, random, sys
option = 0

#Item stuff
items = {'bunnyPopulation':10,
         'foxPopulation':3,
         'plants':20,
         'thirst':40,
         'hunger':40,
         'sleep':0,
         'day':0
         }


#Creating a function to make sure any inputs are numbers.
#I take a lot of number inputs, so this will be helpful
def numberInput(text=""):
    cow = input(text)
    while not cow.isdigit():
        print("Please enter a number:")
        cow = input(text)
    return int(cow)

#function for plants
def plantPopulation():
    plantChance = random.randint(0,100)
    if plantChance <= 30:
        items ['plants'] -= (bunnyPopulation/2) 
        
                
#player
def hunger():
    items ['hunger'] += 10


def thirst():
    items ['thirst'] += 10
        
#main menu
def menu():
    print(' 1) be a bunny')
    print(' 2) be a fox')
    print(' 0) do something else')
    option = numberInput()
    print()
    if option == 1:
        menuBunny()
    if option == 2:
        menuFox()
    if option == 0:
        print("you cant")
        items ['sleep'] += 1
        time.sleep(items ['sleep'])
    else:
        items ['sleep'] += 1
        time.sleep(items ['sleep'])
        print()
        menu()

 
def randomEvents():
    global plants, hunger, thirst, bunnyPopulation, foxPopulation
    event = random.randint(0,600)
    #boom of foxes
    if event <= 30:
        print ("A boom of the fox population went up")
        items ['bunnyPopulation']+=4
    #boom of bunnies
    elif event <= 60:
        print("A boom of the bunny population went up")
        items ['bunnyPopulation']+=4
    #drought
    elif event <= 75:
        print("a drought acoured!")
        items ['thirst'] += 17
    #scarcity of plants
    elif event <=105:
        print("the population of plants have gone down")
        items ['plants'] -= 6

#death functions
def death():
    if option == 1:
        if items ['bunnyPopulation'] == 0:
            print('your species failed')
            print()
            time.sleep(1)
            print('you lose')
            sys.exit()
    if option == 2:
        if items ['foxPopulation'] == 0:
            print('your species failed')
            print()
            time.sleep(1)
            print('you lose')
            sys.exit()
    return option

if items ['thirst'] == 100:
    print('you died of thirst')
    sys.exit()

if items ['hunger'] == 100:
    print('you starved to death')
    sys.exit()

#bunny menu
def menuBunny():
    global hunger, thirst, bunnyPopulation
    hunger()
    thirst()
    print('Day = ',items ['day'])
    print('Hunger = ',items ['hunger'])
    print('Thirst = ',items ['thirst'])
    print('amount of plants =',items ['plants'])
    print('Fox population = ', items ['foxPopulation'])
    print('Bunny population = ', items ['bunnyPopulation'])
    randomEvents() #Initiate possible random events
    print(' 1) eat')
    print(' 2) drink')
    print(' 3) add population')
    option = numberInput()
    print()
    if option == 1:
        if items ['plants'] == 0:
            print('there are no more plants so you can not eat')
        else:
            items ['hunger'] -= 15
            items ['plants'] -= 1
    elif option == 2:
        items ['thirst'] -= 15
    elif option == 3:
        items ['bunnyPopulation'] += 0.35
    if random.randint(0,40) < items ["foxPopulation"]:
        bunnySeeFox()
    items ['day'] += 1
    death()
    menuBunny()
    return option

 #fox menu
def menuFox():
    global hunger, thirst, foxPopulation
    print('Day = ',items ['day'])
    print('Hunger = ',items ['hunger'])
    print('Thirst = ',items ['thirst'])
    print('amount of plants =',items ['thirst'])
    print('Fox population = ', items ['foxPopulation'])
    print('Bunny population = ', items ['bunnyPopulation'])
    randomEvents() #Initiate possible random events
    print(' 1) hunt')
    print(' 2) drink')
    print(' 3) add population')
    option = numberInput()
    print()
    if option == 1:
        if items ['bunnyPopulation'] <= 0:
            print('there are no more bunnies so you can not eat')
        else:
            foxSeeBunny()
    elif option == 2:
        items ['thirst'] -= 15
    elif option == 3:
        items ['foxPopulation'] += 0.35
    elif option == 0:
        print("no u")
    else:
        print("You wasted a day.")
    items ['day'] += 1
    death()
    menuFox()
    return option



#animals seeing each other
def bunnySeeFox():
    print("You see a fox.")
    print(" 1) Follow it")
    print(" 2) run away")
    choice = numberInput()
    if choice == 1:
        print('You follow the fox and you die')
        sys.quit()
    elif choice == 2:
        print("You run away")
        if random.randint(0,100) < 20:
            print("the fox caught up to you and ate you")
            sys.exit()

 
def foxSeeBunny():
    print("You see a bunny.")
    print(" 1) Ignore")
    print(" 2) Hunt it")
    choice = numberInput()
    if choice == 1:
        print('You ignore the bunny')
    if choice == 2:
        print("you follow the bunny")
        items ['hunger'] -= 18
        event = random.randint(0,100)
    if event <= 40:
        print("the bunny ran away")
        
    elif event <= 100:
        print("you caught the bunny and you eat it")


#ending of the game stuff
for i in range(250):
    menu()


while day <= 250:
    print()
    print('CONGRATS! you survived till hibernation time!')
    time.sleep(1)
    print('you go into your bunny hole and hibernate')
    time.sleep(2)
    print('Thanks for playing!')
