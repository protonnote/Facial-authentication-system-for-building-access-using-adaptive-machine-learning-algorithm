import os

def clean(fname):
    dir = "pic/"
    for i in fname:
        file = dir + i
        if os.path.exists(file):
            os.remove(file)
            print("The {} remove complete.".format(file))
        else:
            print("The file does not exist")