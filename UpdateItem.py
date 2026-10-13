#UpdateItem.py


import pickle

def updateitem():
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
    # locating the item for updating
    try:
        pid = int(input("Enter PID for updating PRICE:"))
    except ValueError:
        print("DON'T ENTER STR/ALNUM/SYMBOL FOR PID")
    else:
        res=False
        for i in range(len(records)):
            if (records[i][0] == pid):
                recordindex=i
                res=True
                break

        print("-" * 70)
        if (res):
            print("\tPID already exists file")
            newprice = float(input("Enter new employee sal: "))
            records[recordindex][2] = newprice
            # rewrite all record to file
            with open("inv.pickling", 'wb') as fp:
                for record in records:
                    pickle.dump(record, fp)
            print("-" * 70)
            print("\tPRODUCT DETAILS update successfully--verify")
        else:
            print("\tPID not found in file")
        print("-" * 70)
