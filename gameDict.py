import pandas as pd

#This class holds the main functions of the GameDictionary
class GameDict:
    def __init__(self, dictionary = {}, pk = 0):
        self.dictionary = dictionary
        self.pk = pk

    #this takes the values for the Videogame Console/Platform and the name of the Videogame as arguments and then places them into the dictionary 
    def addGame(self,platform,game):
        self.dictionary[self.pk] = [platform,game]
        self.pk += 1
        print()
        return f"Added {game} on {platform} to Dictionary"
    
    #This checks if there are any games in the dictionary and returns the data if it exists.
    def showDict(self):
        if len(self.dictionary) == 0:
            print("There are currently no games in this collection")
        for i, x in self.dictionary.values():
            print(f"I have the game {x} on {i}")
        return "Information Transfer Complete"
    
    # Note columns is for the columns and the index is for the rows
    # This exports the data currently inside the dictionary to a Excel document named "output.xlsx"
    def exportDict(self):
        df1 = pd.DataFrame(self.dictionary.values(), columns=['Platform','Videogames'])
        with pd.ExcelWriter("output.xlsx") as writter:
            df1.to_excel(writter)
        print()  
        return "Export Complete"
    
    # This clears all of the data from the current dictionary.
    def clearDict(self):
        self.dictionary.clear()
        return "Dictionary Cleared"
    





