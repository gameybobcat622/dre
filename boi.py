"""
program goals:
1. Pull the values stored at specific indexes

"""
import random
myList = []
unique_list = []

def mainProgram():
    #build our while group
    while True:
        myList = []
        print("Hello, there! Let's work with lists!")
        print("Please choose from the following options. Type number of the choice")
        choice = input("""1. Add to a list,
2. Add a bunch of numbers,
3. Get an item at an index
4. Sort list
4. Random Search
5. Linear Search
7. Recursive Binary search
8. Iterative Binary Search
9. Print List
10. Quit """)
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
            sortList(myList)
        elif choice == "7":
            binSearch = input("What number are you looking for?  ")
            recursiveBinarySearch(unique_list, 0, len(unique_list)-1, int(binSearch))
        elif choice == "8":
            binSearch = input("what number are you looking for?  ")
            recursiveBinarySearch(unique_list, int(binSearch))
            if result != -1:
                print("Your number is not at index position {}".format(result))
        else:
            print("Your number is not found in that list, bud!")

        elif choice == "9":
            printLists()
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

def sortList (myList):
    #"myList" is the ARGUEMENT this function takes.
    for x in myList:
        if x not in unique_list:
            unique_list.append(x)
    unique_list.sort()
    showMe = inout("Wanna see your new, sorted list?    Y/N")
    if showMe.lower() == "y":
        print(unique_List)

def indexValues():
    print("At what index position do you want to search?")
    indexPos = input("type an index position here:   ")
    print(myList[int(indexPos)])

def randomSearch():
    print("oH iM So randOM!!!")
    print (myList[radom.randint(0, len(myList)-1)])

def linearSearch():
    print("we're going to go through this list one item at a time")
    searchValue = input("what are you looking for?         ")
    for x in range(len(myList)):
        if myList[x] == int(searchValue):
            print("your item is at index position  {}".format(x))

def recursiveBinarySearch(unique_list, low, high, x):
    if high >=low:
        mid = (high + low) // 2
        if unique_list[mid] == x:
            print("Your number is at index position{}".format(mid))
            return mid
        elif unique_list[mid] > x:
            return recursiveBinarySearch(unique_list, low, mid-1, x)
        else:
            return recursiveBinarySearch(unique_list, mid +1, high, x)
    else:
        print("Your number isn't here!")


def itertiveBinarySearch(unique_list, x):
    low = 0
    high = len(unique_list)-1
    mid = 0

    while low <= high:
        mid = (high + low) //2

        if unique_list[mid] < x:
            low = mid + 1
        elif unique_list[mid] > x:
            high = mid -1
        else:
            return mid
    return -1
                        


def indexValues():
    print("At what index position do you want to search?")
    indexPos = input("type an index position here:   ")
    print(myList[int(indexPos)])

def printLists():
    if len(unique_list) == 0:
        print(myList)
    else:
        whichOne = input("Which list do you want to see, sorted?  ")
        if whichOne.lower() == "sorted":
            print(unique_list)
def recursiveBinarySearch(unique_list,  x):
    low = 0
    high = len(unique_list)-1
    mid = 0


    while low <= high:
        mid = (high


if __name__ == "__main__":
    mainProgram()
