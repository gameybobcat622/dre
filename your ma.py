"""
program goals:
1. Pull the values stored at specific indexes

"""
def mainProgram():
    #build our while group
    while True:
        myList = []
        print("Hello, there! Let's work with lists!")
        print("Please choose from the following options. Type number of the choice")
        choice = input("1. Add to a list, 2. Return a value at a list, or 3.  ")
        if choice == "1":
            addToList()
        elif choice == "2":
            indexValues(
        elif choice == "3":
            break

def addToList():
    print("Adding to a list! Great choice!")
    newItem = input("Type an integer here!   ")
    mylist.append(int(newItem))
    #we  need to think about errors!


def indexValues():
    print("At what index position do you want to search?")
    indexPos = input("type an index position here:   ")
    print(myList[int(indexPos)])


if__name__== "__main__":
