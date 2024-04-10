import random 
str = "y"
def rollDice(str):
    if str == "y":
        num = random.randint(1,6)
        if(num == 1):
            print("""
            =========
            |       |
            |   O   |
            |       |
            =========
            """)
        elif(num == 2):
            print("""
            =========
            | O     |
            |       |
            |     O |
            =========
            """)
        elif(num == 3):
            print("""
            =========
            | O     |
            |   O   |
            |     O |
            =========
            """)
        elif(num == 4):
            print("""
            =========
            | O   O |
            |       |
            | O   O |
            =========
            """)
        elif(num == 5):
            print("""
            =========
            | O   O |
            |   O   |
            | O   O |
            =========
            """)
        elif(num == 6):
            print("""
            =========
            | O   O |
            | O   O |
            | O   O |
            =========
            """)
        str = input("To Roll again enter y to exit enter n  :")
        rollDice(str)
    elif str == "n":
        print("good Bye!!")
    else:
        print("Worng input")
        
rollDice(str)