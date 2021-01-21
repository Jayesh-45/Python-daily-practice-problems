# 1. Write a program to count the number of strings
# where the length is two or more and
# the first and last character is same from the given list of strings.

List=[]
elements = int(input("Enter the number of elements you want in the your list:\n"))

print("Enter the",elements, "numbers(KEYS) for your List:")
for i in range(elements):
    num=input("Enter the List element:")
    List=List+[num]
print("Your entered list is:",List)

def Sample(List):
    count=0
    for la in List:
        if len(la) >= 2 and (la[0] == la[-1]):
            count=count+1
    return count

x=Sample(List)
print("The number of strings where the string length is two or more and the first and last char are same is:",x)

____

# 2. Write a program to remove duplicates from a list

List=[]
elements = int(input("Enter the number of elements you want in the your list:\n"))

print("Enter the",elements, "numbers for your List:")
for i in range(elements):
    num=int(input())
    List=List+[num]
print("Your entered list is:",List)

newList=[]
for x in List:
    if x not in newList:
        newList.append(x)

print("After removing duplicate elements:",newList)

____

#3. Write a program to print the numbers of a specified list after removing even numbers from the list.

sampleList=[]
elements = int(input("Enter the number of elements you want in the list\n"))
print("Enter the",elements, "numbers(E/O) for your List.")
for i in range(elements):
    num=int(input())
    sampleList=sampleList+[num]
print("Your entered list is.",sampleList)

for i in sampleList:
        if (i%2==0):
            sampleList.remove(i)

print("After removing even numbers, the remaining list is..",sampleList)
