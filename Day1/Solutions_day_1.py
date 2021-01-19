# 1. Write a python program to create a list without append(), and display list items.
# Access individual items through indexes getting user input

A=[] # Empty list created
elem=int(input("Enter the number of elements you want in the list\n"))#No of elements in list
print("Enter the",elem, "Elements")
for i in range(elem):
    num=int(input())
    A=A+[num]
print("Your entered list is",A)

X=int(input("Enter any index number you want."))
print("The element on",X,"Position is",A[X])


# 2. Write a program to get the number of occurrences of a specified element in a list

L1=[]
elements = int(input("Enter the number of elements you want in the list\n"))
print("Enter the",elements, "Elements")
for i in range(elements):
    num=int(input())
    L1=L1+[num]
print("Your entered list is",L1)
def Func(L1,X):
    countVar=0
    for i in L1:
        if (i==X):
            countVar=countVar+1
    return countVar
X=int(input("Enter the number you want to find the no of occurances in the given list\n"))
noOfTimes=Func(L1,X)
print(X,"Has appeared",noOfTimes,"Times in List")



# 3. Write a program to remove the first occurrence of a specified element from a list.

L2=[]
elements = int(input("Enter the number of elements you want in the list\n"))
print("Enter the",elements, "Elements")
for i in range(elements):
    num=int(input())
    L2=L2+[num]
print("Your entered list is",L2)
X=int(input("Enter the number you want to remove from the list\n"))
L2.remove(X)
print("The remaining list is",L2)
