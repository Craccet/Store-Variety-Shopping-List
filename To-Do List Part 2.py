#Ivan Hernandez and Ivan Velazquez
#1/11/24
#To-Do List


#Initialize
print("Welcome to your grocery list. Here is your current list: Milk, Eggs, Doritos, Toilet Paper, Peppers, XXXXL Underwear")
grocerylist = ["Milk", "Eggs", "Doritos", "Toilet Paper", "Peppers", "XXXXL Underwear"]


#Functions
def start():   
    print("1. Add a task to the to-do list\n2. View the current to-do list\n3. Mark a task as completed\n4. Remove a task from the to-do list\n5. Remove all tasks from the to-do list\n6. Sort the list alphabetically\n7. Print the number of Items on the To-do List\n8. Exit the program")
    question = int(input("What would you like to do (please select a number)?"))
    if question == 1:
        additem()

    if question == 2:
        viewlist()

    if question == 3:
        checkmark()

    if question == 4:
        removetask()

    if question == 5:
        removealltasks()

    if question == 6:
        sortalphabetically()

    if question == 7:
        displaynumberofitems()

    if question == 8:
        quitprogram()

def additem():
    addeditem = input("What item would you like to add?")
    global grocerylist
    grocerylist.append(addeditem)
    start()

def viewlist():
    print(grocerylist)
    start()

def checkmark():
    global grocerylist
    print(grocerylist)
    checkeditem = input("What item would you like to check off? ")
    grocerylist.remove(checkeditem)
    grocerylist.insert(0, checkeditem + " ✔")
    print(grocerylist)
    start()

def removetask():
    removedtask = input("What item would you like to remove? ")
    global grocerylist
    grocerylist.remove(removedtask)
    start()

def removealltasks():
    sure = input("Are you sure you would like to remove EVERYTHING off your list? Please say yes or no.")
    if sure == "yes" or sure == "Yes":
        grocerylist.clear()
        start()
    elif sure == "no" or sure == "No":
        start()

def sortalphabetically():
    grocerylist.sort(key=str.lower)
    start()

def displaynumberofitems():
    print("The number of items in your list is:", len(grocerylist), "items")
    start()

def quitprogram():
    quit()


#Main
start()