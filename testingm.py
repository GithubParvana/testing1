import sys

args = sys.argv

if len(args) != 3:
        print("The script should be called with two arguments")

else:
    a = int(args[1])
    b = int(args[2])

    def addition():
        c = a + b
        return c


    print(addition())