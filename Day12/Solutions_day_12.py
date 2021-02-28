#1. Write a program to count the number of characters(Frequency) in a string.

def count(sample[i]):
    x=sample[i]

    if sample[i]==x:
            count=count+1
    i=i+1
    return count

sample='google.com'
print(sample[0])

for i in range(0,len(sample)):
    x=count(sample[i])
    print(x)
    

____

#2. Write a python function that takes a list of words and returns the longest word and the length of that longest word.

def longestWord(List):
    z=0
    word=''
    for z in range(0,len(List)):
        if len(List[z])>len(word):
            word=List[z]
    return word

List=[]
x=int(input("Enter the no of words you want in your list:"))
i=0

while(i<x):
    word=input("Enter a word:")
    List.append(word)
    i=i+1
print("Your Entered List of words is:",List)

Word=longestWord(List)
print(Word,"is the longest word in that list and",len(Word),"is its length.")

____
