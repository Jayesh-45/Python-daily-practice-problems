#1. Write a program to concatenate following 3 dictionaries to create a new one.

Dict1={}
Dict2={}
Dict3={}
finalDict={}

key=0
value=0
n=int(input("Enter the number of Keys and values you want in your 3 Dictionaries:"))

i=1
while(i<=n):
    key =int(input("Enter the key for 1st Dict:"))
    value=int(input("Enter its value:"))
    Dict1[key] = value
    i=i+1

i=1
while(i<=n):
    key =int(input("Enter the key for the 2nd Dict:"))
    value=int(input("Enter its:"))
    Dict2[key] = value
    i=i+1

i=1
while(i<=n):
    key =int(input("Enter the key for the 3rd Dict:"))
    value=int(input("Enter its value:"))
    Dict3[key] = value
    i=i+1

print("The First Dictionary:",Dict1)
print("The Second Dictionary:",Dict2)
print("The Third Dictionary:",Dict3)

for a in (Dict1,Dict2,Dict3):
    finalDict.update(a)
print("The Final Dictionary after concatinating the above three dictionaries is:\n",finalDict)

____

