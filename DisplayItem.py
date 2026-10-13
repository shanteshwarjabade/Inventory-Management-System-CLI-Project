#DisplayItem.py
import pickle

def displayitem():
    #geetting all record in list in list
    records = []
    with open("inv.pickling", 'rb') as fp:
        while True:
            try:
                record = pickle.load(fp)
                records.append(record)
            except EOFError:
                break
    # ----------------------------
    # locating the item for display
    try:
        pid = int(input("Enter PID for display an item:"))
    except ValueError:
        print("DON'T ENTER STR/ALNUM/SYMBOL FOR PID")
    else:
        res=False
        for i in range(len(records)):
            if (records[i][0] == pid):
                recordindex=i
                res=True
                break

        if(res):
            print("=" * 50)
            print("\tItem details found successfully")
            print("=" * 50)
            print("\tPID\t\tPNAME\t\tPRICE")
            print("=" * 50)
            for val in records[recordindex]:
                print("\t{}".format(val),end="\t")
            print()
            print("=" * 50)
        else:
            print("=" * 50)
            print("\tPID NOT FOUND---TRY-AGAIN")
            print("=" * 50)

