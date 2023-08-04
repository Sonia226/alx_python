from sys import argv

if __name__ == "__main__":
    pass

args = argv[1:]
n = len(args)

if  n == 1:
    print("{} argument:".format(n))
elif n == 0:
    print("{} arguments.".format(n)) 
elif n > 1:
    print("{} arguments:".format(n))
else:
    print("No argument.")

for i in range(n):
 print("{}: {}".format(i+1, args[i]))