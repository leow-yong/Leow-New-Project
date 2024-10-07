from list import listItem
import sys

arrList = []
arrCount = 0

def add_list_item():
    while True:
        item = input("Please enter the item or 'q' to go back: ")
        if item == 'q':
            while True:
                quitConfirm = input("Are you wish to add the item 'q' or return to previous step.\n('Y' for add item 'q' / 'N' for go back / 'C' for cancel this process): ")
                quitConfirm = str.upper(quitConfirm)
                if quitConfirm == 'N':
                    return
                elif quitConfirm == 'Y':
                    arrList.append(listItem(item))
                    print("Successfully added " + item + "\n")
                    break
                elif quitConfirm == 'C':
                    print("Cancel quit \n")
                    break
                else:
                    print("Invalid input, please enter 'Y' or 'N' or 'C'.")
        else:
            arrList.append(listItem(item))
            print("Successfully added " + item + "\n")


def show_list_item():
    if not arrList:
        print("The list is empty.")
    else:
        count = 1
        for x in arrList:
            print(str(count) + ") " + x.getItem())
            count += 1
        return

def del_list_item():
    if not arrList:
        print("The list is empty.")
    else:
        show_list_item()
        while True:
            delItem = input("\nPlease enter the index of the item to be deleted or 'q' to return to previous step: ")
            if delItem == 'q':
                return
            else:
                try:
                    delTarget = int(delItem) - 1
                    if delTarget < 0 or delTarget > len(arrList):
                        print("Invalid input, please enter again.")
                    else:
                        delItemName = arrList[delTarget].getItem()
                        arrList.pop(delTarget)
                        print("Successful deleted " + delItemName)
                except:
                    print("Invalid input, please enter again.")

def exit_program():
    print("Exiting the program now.")
    sys.exit(0)

#do while looping
while True:
    print("1) Add new item")
    print("2) Show the list")
    print("3) Delete an item")
    print("4) Quit the program")
    userInput = input("Please enter your choice: ")
    
    if userInput == "1":
        print("\n-------------------------------------------")
        add_list_item()
    elif userInput == "2":
        print("\n-------------------------------------------")
        show_list_item()
        print("All result shown")
    elif userInput == "3":
        print("\n-------------------------------------------")
        del_list_item()
    elif userInput == "4":
        print("\n-------------------------------------------")
        exit_program()
    else:
        print("Invalid input, please try again")
    
    print("\n-------------------------------------------")

        
    '''
    x = listItem("1")
    print(x.getAllInfo())
    '''

