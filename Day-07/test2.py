import sys

type = sys.argv[1]

if type == "t2.micro":
    print("it will charge you 2 dollers per day")

elif type == "t2.medium":
    print("it will charge you 4 dollers per day")

elif type == "t2.xlarge":
    print("it will charge you 8 dollers per day")

else:
    print("Please provide correct instance type")
    
