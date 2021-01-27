#1. Write a program to remove a key from a dictionary.

Dict={}
key=''
value=''
n=int(input("Enter the number of Keys you want in your Dictionary:\n"))
i=1

while(i<=n):
    key =input("Enter the Key:")
    value=input("Enter its value")
    Dict[key] = value
    i=i+1
print("Your Dictionary is:",Dict)

value=input("Enter the key you want to remove:\n")
del Dict[value]

print("Remaining dictionary is:\n",Dict)


____

#2. Write a program to multiply all the items in a dictionary.

def mul(Dict):
    result=1
    for x in Dict:
        result = result * Dict[x]
    return result

Dict={}
key=''
value=''
n=int(input("Enter the number of Keys you want in your Dictionary:\n"))
i=1
while(i<=n):
    key =input("Enter the Key:")
    value=int(input("Enter its value:"))
    Dict[key] = value
    i=i+1

print("Your Dictionary is:",Dict)
print("Multiplication of all items in this dictionary is:",mul(Dict))


____

#3. Write a program to map two lists into a dictionary.

def combineTwoLists(List1,List2,DICT):
    for i in List1:
        for z in List2:
            DICT[i]=z
            List2.remove(z)
    return DICT

List1=[]
List2=[]
DICT={}

elements = int(input("Enter the number of elements you want in the your lists:\n"))

print("Enter the",elements, "numbers(KEYS) for your 1st List:")
for i in range(elements):
    num=int(input())
    List1=List1+[num]
print("Your entered 1st list is:",List1)

print("Enter the",elements, "numbers(VALUES) for your 2st List:")
for i in range(elements):
    num=int(input())
    List2=List2+[num]
print("Your entered 2nd list is:",List2)

print("The Combined List is:\n",combineTwoLists(List1,List2,DICT))

____
