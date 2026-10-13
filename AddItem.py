#AddItem.py
import pickle
def additem():
    with open("inv.pickling","ab") as fp:
        items=[] #empty list
        #getting product details from keyboard
        while True:
            try:
                print("="*50)
                pid=int(input("Enter PID:"))
                pname=input("Enter Product Name:")
                price=float(input("Enter Product Price:"))
            except ValueError:
                print("DON'T ENTER STR/ALNUM/SYMBOLS FOR PID AND PRICE")
                print("*" * 50)
            else:
                items.append(pid)
                items.append(pname)
                items.append(price)

                break
        #----------------------------------------------------------------
        #save items to file
        pickle.dump(items,fp)
        print("-"*50)
        print("PRODUCT DETAILS SAVED SUCCESSFULLY IN FILE")


