____

#3. Write a program to print all the unique values of a Dictionary.

def findUnique(Dict):
    x = []
    c=''
    for i in Dict:
        c=Dict[i]
        if c not in x:
            x.append(c)
    return x

Dict={}
keys=''
value=''
num=int(input("Enter the number of keys you want in your Dictionary:\n"))
i=1
while(i<=num):
    keys=input("Enter the key:")
    value=input("Enter its value:")
    Dict[keys]=value
    i=i+1
print("Your Entered Dictionary is:",Dict)
y=['']
y=findUnique(Dict)
print("The Unique values are:")
for i in y:
    print(i)


____

#4. Write a program to find the highest 3 value of a dictionary
def highestThree(Dict):
    x = []
    for i in Dict:
        c=Dict[i]
        if c not in x:
            x.append(c)
    x.sort()
    return x

Dict={}
keys=''
value=''
num=int(input("Enter the number of keys you want in your Dictionary:\n"))
i=1
while(i<=num):
    keys=input("Enter the key:")
    value=int(input("Enter its value:"))
    Dict[keys]=value
    i=i+1
print("Your Entered Dictionary is:",Dict)
y=[]
y=highestThree(Dict)
print("The Highest Three values are:")
print(y[-3:])
