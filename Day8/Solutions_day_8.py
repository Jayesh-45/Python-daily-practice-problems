# 1. Write a program to create a dictionary and access all elements using key and value.
#Dictionary is unordered changeable and duplicates are not allowed

puppy = {"Mutable":"It can be changed",
         "Immutable":"It cannot be changed",
         "Wise":"The person who is morally correct",
         "Manmade":"The objects that were not readily available in nature."}
print("Search for the meanings of the following words:\n",
      "1. Immutable\n","2. Mutable\n","3. Wise\n","4. Manmade\n")

word = input()
print(puppy[word])
print("The dictionary is")

count=1
for i in puppy:
    print(count,i,puppy[i])
    count=count+1

____

#2. Write a program to add a key to a dictionary.


s={1:"Yes",2:"This",3:"Is a"}
print("Current dictionary is",s)
key = int(input("Enter the key"))
value = input("Enter the value")
s[key] = value
print("The final dict is",s)

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
