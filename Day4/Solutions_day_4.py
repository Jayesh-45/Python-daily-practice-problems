#1. To check if two lists are circularly identical

def circ(List1,List2):
    List3=List1*2#121121
    for x in range(0,len(List1)):#x=0
        z=0
        for y in range(x,x+len(List1)):
            if List2[z]==List3[y]:
                z=z+1
            else:
                break
        if z==len(List1):
            return True
    return False

List1=[]
List2=[]

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

if(circ(List1,List2)):
    print("Yes,they are circular..")
else:
    print("No,they are not")

____

#2. To find the second smallest number in the list.

List1=[]
elements = int(input("Enter the number of elements you want in the your list:\n"))

print("Enter the",elements, "numbers(KEYS) for your List:")
for i in range(elements):
    num=int(input())
    List1=List1+[num]
print("Your entered list is:",List1)

List1.sort()
print('The second smallest number in this list is',List1[1])

____

#3. To find unique values from a list.

def findUnique(listx):
    x=[]
    for i in listx:
        if i not in x:
            x.append(i)
    return x

Listx=[]
elements = int(input("Enter the number of elements you want in the your lists:\n"))

print("Enter the",elements, "numbers(KEYS) for your List:")
for i in range(elements):
    num=int(input())
    Listx=Listx+[num]
print("Your entered list is:",Listx)

print("The unique values are",findUnique(listx))

____
