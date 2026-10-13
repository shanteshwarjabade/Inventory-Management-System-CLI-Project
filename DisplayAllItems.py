#DisplayAllItems.py


import pickle
def displayAllItems():
    with open("inv.pickling","rb") as fp:
        print("="*50)
        print("\tPID\t\tPNAME\t\tPRICE")
        print("=" * 50)
        while True:
            try:
                items = pickle.load(fp)
                for item in items:
                    print("\t{}".format(item),end="\t")
                print()
            except EOFError:
                print("=" * 50)
                break
