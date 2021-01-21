 #1. Write a program to check if a list is empty or not.
 
def res(L2):
    if len(L2)==0:
        return 1
    else:
        return 0

L2=[]
elements = int(input("Enter the number of elements you want in the list\n"))
print("Enter the",elements, "Elements")
for i in range(elements):
    num=int(input())
    L2=L2+[num]

print("Your Entered list is:",L2)
if res(L2):
    print("Yes, the list is empty.")
else:
    print("No, its not a empty list.")
    
    
____

# 2. Write a program to find the list of words that are longer than n from a given list of words.

list_of_words=[]

elements = int(input("Enter the number of elements you want in the list\n"))
print("Enter the",elements, "words for your List.")

for i in range(elements):
    num=input()
    list_of_words=list_of_words+[num]
print(list_of_words)

test=[]
x=int(input("The length of the words should be greater than?\n"))

for i in list_of_words:
    if len(i)>x:
        test.append(i)

print("The final list of words that are longer than",x,"From the given list is\n",test)

____
# 3. Write a program to get difference between two lists

def diffrenceBetweenLists(List1, List2):
    List3=[]
    for x in List1:
        if x not in List2:
            List3.append(x)
    for x in List2:
        if x not in List1 and x not in List3:
            List3.append(x)
    return List3

List1=[]
List2=[]

elements = int(input("Enter the number of elements you want in the first list\n"))
print("Enter the",elements, "numbers for your 1st List.")

for i in range(elements):
    num=int(input())
    List1=List1+[num]
print("Your entered 1st list is.",List1)

ele = int(input("Enter the number of elements you want in the second list\n"))
print("Enter the",ele, "numbers for your 2st List.")

for i in range(ele):
    num=int(input())
    List2=List2+[num]
print("Your entered 2nd list is.",List2)

print("The Difference between both the entered lists is.",diffrenceBetweenLists(List1,List2))

____

# 4. Program to convert a List of characters into a string.

Listx=[]

elements = int(input("Enter the number of characters you want in the list\n"))
print("Enter the",elements, "characters for your List.")

for i in range(elements):
    num=input()
    Listx=Listx+[num]
print("Your entered list of characters is.",Listx)

y=''
for x in Listx:
    y=y+x
print("The Converted String is","'",y,"'")

____
