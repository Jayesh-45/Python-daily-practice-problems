#1. Write a program to match the key values in two dictionaries.

#dict1={'key1':1,'key2':3,'key3':4,'key4':7,'key5':9,'key6':11}
#dict2={'key1':11,'key2':3,'key3':4,'key4':1,'key5':9,'key6':2}

Dict1={}
Dict2={}

key=''
value=0
n=int(input("Enter the number of Keys you want in your Dictionaries:\n"))
i=1
while(i<=n):
    key =input("Enter the Key:")
    value=int(input("Enter its value"))
    Dict1[key] = value
    i=i+1
print("Your First Dictionary is:",Dict1)

z=1
while(z<=n):
    key =input("Enter the Key:")
    value=int(input("Enter its value"))
    Dict2[key] = value
    z=z+1
print("Your second Dictionary is:",Dict2)

for key,value in Dict1.items():
    for x,y in Dict2.items():
        if key==x and Dict1[key]==Dict2[key]:
            print(key,':',value,"Is present in both dictionaries.")


____

#2. Write a program to drop empty items from a given dictionary.

d={'a':'red','b':'pink','c':None}
print("Before dropping empty items:",d)
dict={}
for key,value in d.items():
    if value is None:
        continue
    else:
        dict[key]=value
print("After dropping empty items:",dict)


____

#3. Write a program to create a dictionary of keys x,y,z
# where each key has a value as a list from 11-20, 21-30,31-40
# access the fifth value of each key from the dictionary.

def frame(min):
    value=list(range(min,min+9))
    return value

dict={}
key=''
value=[]
n=int(input("Enter the number of Keys you want in your Dictionary:\n"))

i=1
min=11
while(i<=n):
    key =input("Enter the Key:")
    value=frame(min)
    dict[key] = value
    i=i+1
    min=min+10

print("Your Dictionary is:",dict)
for x,y in dict.items():
    print("The fifth item of", x, "is:", dict[x][4])

for x,y in dict.items():
    print(x,'has values:',y)

    
____
