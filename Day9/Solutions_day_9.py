#1. Write a program to sort a list alphabetically in a dictionary.
#Dict={"L1":[1,8,5,7],"L2":[5,9,11,4],"L3":[11,81,65,52]}

Dict={}
print("Enter the Dictionary who's value for a key is a list:")
Key=""
value=[]
noOfItems=int(input("Enter the no of items you want in your Dictionary:\n"))
i=0

while(i<noOfItems):
    Key = input("Enter the key no:")
    elements = int(input("Enter the number of elements you want in the your list:\n"))
    print("Enter the", elements, "numbers for your List:")

    for z in range(elements):
        num = int(input())
        value = value + [num]
    Dict[Key] = value
    i = i + 1
    value=[]

print("YOUR DICTIONARY BEFORE SORTING ALPHABETICALLY IS:\n",Dict)

Dict2={}

print("After sorting:")
for i,j in Dict.items():
    Dict2[i]=sorted(j)

print(Dict2)


____

#2. Write a program to remove spaces from dictionary keys.
#using replace()

Dict={}
keys=''
value=''
num=int(input("Enter the number of keys you want in your Dictionary:\n"))
i=1

while(i<=num):
    keys=input("Enter the key with space:")
    value=int(input("Enter its value:"))
    Dict[keys]=value
    i=i+1
print("Your Entered Dictionary is:",Dict)

dict_without_space={}

for Key,z in Dict.items():
    dict_without_space[Key.replace(" ","")]=z
print(dict_without_space)


____

#3. Write a program to get the key value and item in a dictionary.
#dict={1:10,2:30,3:55,4:65,5:91}

Dict={}
key=0
value=0
num=int(input("Enter the number of keys you want in your Dictionary:\n"))
i=1

while(i<=num):
    key=int(input("Enter the key:"))
    value=int(input("Enter its value:"))
    Dict[key]=value
    i=i+1
print("Your Entered Dictionary is:",Dict)

print("Key Value Count")
Count=1

for Key,Value in Dict.items():
    print(Key," ",Value," ",Count)
    Count=Count+1
    
____
