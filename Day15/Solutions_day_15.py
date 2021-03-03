#1. Write a program that accepts a comma separated sequence of words as input
# and prints the unique words in sorted form(Alphanumerically).

str=input("Enter comma separated string of words:")

final_str=str.split(",")
final_str.sort()
y=(',').join(final_str)

print("The sorted form is:",y)


____

#2. Write a program to insert a string in the middle of a string.

str=input("Enter the string.")#';;{[]};;'
word=input("Enter the word you want to insert between the string")

#p=str[0:len(str)//2]
str=str[0:len(str)//2]+word+str[len(str)//2:]
print("The final string after inserting the word is:",str)


____

#3. Write a program to reverse words in a string.

str=input("Enter a string containing words:")#'This is a String that we want to reverse.'String of words.

word=str.split() #Splits the string in a list.

x=list(reversed(word))#Reverses the list.
str=" ".join(x)

print("The reversed string is:",str)

____
