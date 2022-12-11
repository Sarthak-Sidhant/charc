import json
import re


#start-validation >>
def start_game():
    print("""
    Welcome To The Game Called 'Charc'
    You Are Charc. You're Living in the Modern Day World Of Science, Every Metric
    Should Be Wisely Chosen, A Digit Overflow Can Corrupt The System.
    Your Objective is to defeat the 3 bosses and come back alive.
    There are glitches in the matrix, And You're Here To Abuse them!
    Good Luck Soldier!

    We Will Start With Personalizing Your Character, Choose the metrics wisely
    """)

    valid_name = False
    
    while valid_name == False:
         
        name=input("Enter Your Username Here (a-z & 8 characters): ")
        
        if not re.match("^[a-z]*$", name):
            print ("Error! Only letters a-z allowed!")
        elif len(name) > 8:
            print ("Error! Only 8 characters allowed!")
        else:
            valid_name=True


    valid_height = False

    while valid_height == False:

        height = int(input("Input Your Height (in centimeters): "))

        if height < 54.6:
            print("too less of a height, go register some guinness or smth")
        elif height > 272:
            print("bro taller than wadlow, bro have a life")
        else:
            valid_height = True

    valid_weight = False

    while valid_weight == False:
        weight= int(input("Input Your Weight (in Kilograms): "))

        if weight < 20:
            print("what are you? a baby?")
            print("invalid below 20, enter it again.")
        elif weight > 369:
            print("Sorry, This Game Is For Humans, Not Elephants.")
        else:
            valid_weight = True


    bmi = weight/((height/100)**2)
    print ("Your BMI is: ", round(bmi,1))

    health = 100

    if bmi > 25:
        print("bro ur overweight, atleast for ur height")
        print("im sorry but you lose 0.5 from your health-points because of your health condition")
        print("bro thats the way science works, you fat, you lose.")
        health=health-0.50
    elif bmi > 21 and bmi < 22:
        print("that's like the perfect bmi")
        health=health+1.50
    elif bmi < 19: 
        print("sadly, ur underweight haha stick")
        print("im sorry but you lose 0.5 from your health-points because of your health condition")
        print("that's the way science works bro, you cant fight bosses when u bad lean and thin")
        health=health-0.50
    else:
        print("sadly/happily, your bmi is alright- but you dont get any extra health points. bad metrics ig?")
    #that's how you get a headstart in society (smirks)
    print("Your Current Health Point is: ", health)

    print("you'll now be guided through the commands")
    print("If You want to check the amount of money/balance you have, you can type 'Money'")
    print("if you want to check the health-points of your character, you can type 'health'")
    print("If You Want to check the progress you made, or the experience you have, you can type 'Exp' or 'Experience'")


    # send the health, height and weight back to the main function so it can be saved to the player class
    return health, height, weight, name

#info-stat area >>
def weapon():
    print("""
    
    health - weapon*(-3/4) 

    if health = 64, and weapon = 16, It Will Take 5.33 Average No-Luck Hits To KEAL

    would be bought from in game store (shop), would display perks and can be upgraded
    
    """ "Your Current Weapon Point is: ", character.weaponx)
def armor():
    print("""
    armor^1.25+health=health
    
    if armor = 16 and health = 64, 16^1.25+64=96 (hehe advanced maths)
    
    you can buy armor in the in-game-store (shop)
    
    """"Your Current Armor Point is: ", character.armorx)
def stats():
    print("Your Player's Stats Are:")
    print("Name: ",character.get_name())
    print("Height: ",character.get_height())
    print("Weight: ",character.get_weight())
    print("Health: ",character.get_health())
    print("Money: ",character.get_money())
    print("Armor: ",character.get_armorx())
    print("Weapon: ",character.get_weaponx())
    print("Experience: ", character.get_exp())
    print("-----------x-----------")
def help():
    print("""
    There Are A Handful Of Commands
     For Money, Type 'Money' (Aliases: bal)
     For Health, Type 'Health'
     For Experience, Type 'Exp' (Aliases: Experience)
     To Check Your Weapon And Armor Points, Type: 'Weapon' or 'Armor'
    """)
def exp():
    print("Your Experience Level is: ", exp,"\n You Can Earn Experience By Killing Minibosses And/Or Bosses\n You Need Experience To deal with bosses and get good weapon/armor.\nThere's also a hidden way to earn experience. I wonder what? (hint: it's literally a cli game bro)")
def bal():
    print("Welcome To The World Of Finance\nCurrently You Have:",character.money,"\nYou Can Earn Money by Working, Yes, Just Like Real Life![1450 (Min. Wage + 20 Minute Cooldown)]\n You Can Also Earn Money By Searching in Places, However, You Have a 11% chance to actually lose money lul\nMoney is Important, You Can Purchase Weapons And Armors To Defeat Bosses with Money\n Things Get Sold in 'Shop' Check 'em out! ")

#shop area >>
def shop():
    print(""" 
    ⁘⁘⟬-SHOP-⟭⁘⁘
    Welcome To The In Game Shop!
    Here You Can Buy Weapon Points And Armor Points! And Healthy Food!
    
    Weapon Point(s) - 1450 $ (buy weapon/buy w/buy Weapon) 
    Armor Point(s) - 1450 $ (buy armor/buy a/buy Armor)
    Health Point(s) - 2900 $ (buy health/buy h/buy Health)
                        --x--
    """)
def buyweapon():
    if character.money >= 1450:
       character.money = character.money - 1450
       character.weaponx = character.weaponx + 1
       print("Weapon Point Has Been Used""\nCurrent Weapon Point(s): ", character.weaponx)
       character.exp+1
    elif character.money < 1450:
        print("Insufficient money, you need ", 1450-character.money, "$ more to buy this item")
    elif character.money == 0:
        "you literal piece of garbage lying over the bin, what do you even think you can buy with 0$, this is not walmarts 80%` sale,  even they dont give shit for free, and you here are trying to destroy the economy, go to hell man"
    else:
        print("Error in buying things. This Shouldn't even occur")
def buyarmor():
    if character.money >= 1450:
        character.money = character.money - 1450
        character.armorx = character.armorx + 1
        print("Armor Point Has Been Used""\nCurrent Armor Point(s): ", character.armorx)
        character.exp+1
    elif character.money < 1450:
        print("Insufficient money, you need ", 1450-character.money, "$ more to buy this item")
    elif character.money == 0:
        "you literal piece of garbage lying over the bin, what do you even think you can buy with 0$, this is not walmarts 80%` sale,  even they dont give shit for free, and you here are trying to destroy the economy, go to hell man"
    else:
        print("Error in buying things. This Shouldn't even occur")
def buyhealth():
    if character.money >= 2900:
        character.money = character.money - 2900
        character.health = character.health + 1
        print("Health Has Been Used""\nCurrent Health Point(s): ", character.health)
        character.exp+2
    elif character.money < 2900:
        print("Insufficient money, you need ", 2900-character.money, "$ more to buy this item")
    elif character.money == 0:
        "you literal piece of garbage lying over the bin, what do you even think you can buy with 0$, this is not walmarts 80%` sale,  even they dont give shit for free, and you here are trying to destroy the economy, go to hell man"
    else:
        print("Error in buying things. This Shouldn't even occur")

# use a class to store a players data and/or settings (It Works, Please Don't Touch)
#class area (120 lines omg) >>
class Player:
    def __init__(self, name, height, weight, health, exp, money, weaponx, armorx):
        self.name = name
        self.height = height
        self.weight = weight
        self.health = health
        self.exp = exp
        self.money = money
        self.weaponx= weaponx
        self.armorx= armorx
        
    # using setters and getters to access the data, by calling Player.get_height() for example, we can get the players height at any point
    # another advantage of using a class is that you can have as many instances of the class as you want, so you can have multiple players / NPCs
    def get_name(self):
        return self.name

    def get_height(self):
        return self.height

    def get_weight(self):
        return self.weight

    def get_health(self):
        return self.health

    def get_exp(self):
        return self.exp
    
    def get_money(self):
        return self.money

    def get_armorx(self):
        return self.armorx
    
    def get_weaponx(self):
        return self.weaponx
    
    def set_money(self, money):
        self.money = money

    def set_name(self, name):
        self.name = name

    def set_height(self, height):
        self.height = height

    def set_weight(self, weight):
        self.weight = weight

    def set_health(self, health):
        self.health = health

    def set_exp(self, exp):
        self.exp = exp

    def set_armorx(self):
        self.armorx = armorx
    
    def set_weaponx(self):
        self.weaponx = weaponx

    def save(self):

        # checking if the file exists, if it doesn't, creating it
        try:
            with open("players.json", "r") as f:
                pass
        except FileNotFoundError:
            with open("players.json", "w") as f:
                # creating a blank .json file
                f.write("{\n    \"Players\":[\n  ]\n}")

        # adding the players data into the players section of the json file
        with open("players.json", "r") as f:

            # loading the entire json file into a variable
            data = json.load(f)

            # adding the new player into the players section of the json file
            data["Players"].append({
                "Name": self.name,
                "Height": self.height,
                "Weight": self.weight,
                "Health": self.health,
                "Exp": self.exp,
                "Money": self.money,
                "Armor Points": self.armorx,
                "Weapon Points": self.weaponx
            })

        # writing the new data to the json file
        with open("players.json", "w") as f:
            json.dump(data, f)
    
    # loading a player based on their name
    @classmethod
    def load(cls, name):
        # getting the data from the json file
        with open("players.json", "r") as f:
            data = json.load(f)

        # getting the player date from the json file
        try:
            # loading all the players section into the users variable
            users = data["Players"]

            # looping through all the users
            for user in users:

                # checking if the name of a user matches the name of the player we are trying to load
                if user["Name"] == name:

                    # if it does, create a new player object with the data from the json file and return it
                    player = cls(user["Name"], user["Height"], user["Weight"], user["Health"], user["Exp"], user["Money"], user["Armor Points"], user["Weapon Points"])
                    return player
        except Exception as e:
            # if there is an error return None
            print("There has been an error loading the player: ", e)
            return None
        
        # if the player isn't found, return None
        return None

#command-input function
def takeCommand():
    query=input()
    return query

#command area >>
if __name__ == "__main__":

    # calling a method to ask the user if they have played the game before
    # if they have, load the game based on a username they input
    # if they haven't, start the game, ask them for a username and run the start_game() method
    
    if input("Have you played the game before? (y/n): ").lower() == "y":
        valid = False

        while valid == False:

            username = input("Enter your username: ")

            if not re.match("^[a-z]*$", username) or len(username) > 8:
                print ("Error! That username is invalid, please try again.")
            else:
                valid = True
                character = Player.load(username)
    else:

        # if user hasn't played the game before, we run the start_game() method
        health,height,weight,name = start_game()
        exp = 0
        money = 25000
        weaponx = 1
        armorx = 0
        character = Player(name, height, weight, health, exp, money, armorx, weaponx)

    # if the user has played the game before, load the game based on the username they input
    # if the username doesn't exist, ask them to re-enter it

    print("Name: ",character.get_name())
    print("Height: ",character.get_height())
    print("Weight: ",character.get_weight())
    print("Health: ",character.get_health())
    print("Money: ",character.get_money())
    print("Armor: ",character.get_armorx())
    print("Weapon: ",character.get_weaponx())
    # start taking commands from the user
    while True:
        query = takeCommand()
        if 'help' in query or 'Help' in query:
            
            character.exp+0.1
        elif 'health' in query or 'Health' in query:
            help()
            character.exp+0.1
        elif 'exp' in query or 'Exp' in query or 'Experience' in query or 'experience' in query:
            exp()
            character.exp+0.1
        elif 'money' in query or 'bal' in query or 'Money' in query or 'Bal' in query:
            bal()
            character.exp+0.1
        elif 'shop' in query or 'Shop' in query:
            shop()
        elif 'weapon' in query or 'Weapon' in query:
            weapon()
        elif 'armor' in query or 'Armor' in query:
            armor()
        elif 'buy' in query or 'Buy' in query:
            def buy():
                item=input("whatchu wanna buy: ")
                if item == "armor":
                    print("you've requested to buy armor")
                    buyarmor()
                elif item == "weapon":
                    print("you've requested to buy weapon")
                    buyweapon()
                elif item == "health":
                    print("you've requested to buy health")
                    buyhealth()
                else:
                    buy()
            buy()
        elif 'exit' in query or 'Exit' in query or 'quit' in query or 'Quit' in query:
            print("Saving Current Progress...")
            character.save()
            print("Exiting...")
            exit()
        else:
            print("Invalid Command")
            character.exp+0.05
# left to add: 
#   1. a way to earn money
#   2. Bosses and Fights
#pfft? only 403 lines of code? 
