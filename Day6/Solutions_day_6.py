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

#2. Write a program to check if a given key exists in a Dictionary

Dict2={}
key=''
value=''
n=int(input("Enter the number of Keys you want in your Dictionary:"))
i=1

while(i<=n):
    key =input()
    value=input()
    Dict2[key] = value
    i=i+1

print("Your final dictionary is:",Dict2)

check=input("Enter the key you want to check in your dictionary:")
if check in Dict2:
    print("Yes,",check,"is present in",Dict2)
else:
    print("No,",check,"is not present in",Dict2)

____

#3. Write a program to generate and print a dictionary that contains a no. between 1 and n
# In the form of (x,x*x)
# Sample n=5
# Output: 1:1,2:4,3:9,4:16,5:25

dict={}
n=int(input("Enter the value of N:"))
data=0
score=0
i=1

while(i<=n):
    data =i
    score =i*i
    dict[data] = score
    i=i+1
print("The Final Dictionary is:",dict)
