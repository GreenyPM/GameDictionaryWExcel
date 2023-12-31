from gameDict import GameDict


class Interface:
# This handles the initial instantiation of the class
    def __init__(self):
        gameCollection = {}
        collectionHandler = GameDict(gameCollection)

        print()
        print("Welcome to the GAME COLLECTOR!\nA fine application to track your games\n")
        keepGoing = True

        # This is the while loop continuously running the choices as long as "keepGoing" = True.
        while keepGoing:
            print("Please input one of the selections below.\n-add game\n-view collection\n-clear\n-export\n-exit")
            print()
            userChoice = input()

            if "add game" in userChoice:
                platformEntry = input("Enter Name of Platform:")
                gameEntry = input("Enter Name of Game:")
                print(collectionHandler.addGame(platformEntry,gameEntry))
                print()
    
            elif "view collection" in userChoice:
                collectionHandler.showDict()
                print()
            elif "clear" in userChoice:
                print(collectionHandler.clearDict())
                print()

            elif "export" in userChoice:
                print(collectionHandler.exportDict())

            #This function ends the loop, thus ending the runtime of the program.
            elif "exit" in userChoice:
                keepGoing = False

            else:
                print("Invalid Selection Please Try Again")
                print()


