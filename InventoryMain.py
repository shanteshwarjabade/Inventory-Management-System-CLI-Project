#InventoryMain.py <---main program
from AddItem import additem
from DeleteItem import deleteitem
from DisplayAllItems import displayAllItems
from DisplayItem import displayitem
from UpdateItem import updateitem
from InventoryMenu import menu

while True:
    try:
        menu()
        ch = int(input("Enter your choice:"))
        match (ch):
            case 1:
                additem()
            case 2:
                deleteitem()
            case 3:
                updateitem()
            case 4:
                displayitem()
            case 5:
                displayAllItems()
            case 6:
                print("*"*50)
                print("\t\tTHX FOR USING THIS PROGRAM")
                print("*" * 50)
                break
            case _:
                print("\tUr Selection of Operation is wrong--try again")
    except ValueError:
        print("DON'T ENTER ALNUM/STR/SYMBOLS FOR CHOICE")