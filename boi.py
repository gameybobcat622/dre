"""
program goals:
1. Pull the values stored at specific indexes

"""
import random
myList = []

def mainProgram():
    #build our while group
    while True:
        myList = []
        print("Hello, there! Let's work with lists!")
        print("Please choose from the following options. Type number of the choice")
        choice = input("""1. Add to a list,
2. Return a value at a list,
3. Add a bunch of numbers!
4. Random Search
5. Linear Search 
6. Print List
7. Quit """)
        if choice == "1":
            addToList()
        elif choice == "2":
            indexValues()
        elif choice == "3":
            addABunch()
        elif choice == "4":
            randomSearch()
        elif choice == "5":
            linearSearch()
        elif choice == "6":
            print (myList)
        else:
            break

def addToList():
    print("Adding to a list! Great choice!")
    newItem = input("Type an integer here!   ")
    mylist.append(int(newItem))
    #we  need to think about errors!

def addABunch():
    print("were gonna add a bunch of numbers to your list!")
    numToAdd = input("How many new integers would you like to add? ")
    numRange = input("and how high would you like these numbers to go ? ")
    for x in range(0, int(numToAdd)):
        myList.append(random .randint(0, int(numRange)))
    print("your list is complete")


def randomSearch():
    print("oH iM So randOM!!!")
    print (myList[radom.randint(0, len(myList)-1)])

def linearSearch():
    print("we're going to go through this list one item at a time")
    searchValue = input("what are you looking for?         ")
    for x in range(len(myList)):
        if myList[x] == int(searchValue):
            print("your item is at index position  {}".format(x))
                        
def indexValues():
    print("At what index position do you want to search?")
    indexPos = input("type an index position here:   ")
    print(myList[int(indexPos)])


if __name__ == "__main__":
    mainProgram()
