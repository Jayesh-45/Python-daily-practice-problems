#1 Write a python program to get the frequency of elements in a list.

def form(i):
    x = list.count(i)
    return x

list=[]
x=int(input("Enter the no of elements you want in your list:"))
i=0

while(i<x):
    num=int(input("Enter a num:"))
    list.append(num)
    i=i+1
print("Your Entered List is:",list)

y=[]
for x in list:
    if x not in y:
        y.append(x)
for i in y:
    print(i, "has appeared", form(i), "Times in the list")
    

____

#2. Write a program to count the number of elements in a list within a specific range

#list=[1,2,3,4,5,6,77,88,9]
List=[]
x=int(input("Enter the no of elements you want in your list:"))
i=0

while(i<x):
    num=int(input("Enter a num:"))
    List.append(num)
    i=i+1
print("Your Entered List is:",List)

x=int(input("Enter the min range"))
y=int(input("Enter the max range"))
z=0
for i in List:
    if i in range(x,y):
        z=z+1

print("There are",z,"Elements in",List,"between range",x,"and",y,"and they are:")

for i in List:
    if i in range(x,y):
        print(i)

____
