#DeleteItem.py
import pickle


def deleteitem():
    records=[]
    with open("inv.pickling",'rb') as fp:
        while True:
            try:
                record=pickle.load(fp)
                records.append(record)
            except EOFError:
                break
    #----------------------------
    #locating the item for delete
    try:
        pid=int(input("Enter PID for deleting an item:"))
    except ValueError:
        print("DON'T ENTER STR/ALNUM/SYMBOL FOR PID")
    else:
        res=False
        for i in range(len(records)):
            if(records[i][0]==pid):
                recordindex=i
                res=True
                break
        #delete the item
        if(res):
            records.pop(recordindex)
            print("Item Deleted successfully from File")

            #rewritting to the file
            with (open("inv.pickling",'wb')) as fp:
                for record in records:
                    pickle.dump(record,fp)
        else:
            print("="*50)
            print("\tPID NOT FOUND IN FILE FOR DELETING ITEM")