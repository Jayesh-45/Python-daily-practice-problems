#1. Write a program to count and display the vowels of a given text.

#vowels=a,e,i,o,u

vowels=['a','e','i','o','u','A','E','I','O','U']
str=input("Enter a string in which you want to count the no. of Vowels present:")
c=0

for i in range(len(str)):
    for z in vowels:
        if str[i] == z:
            c=c+1

print(str,"Contains:",c,"Vowels.")


____

#2. Write a program to count occurrences of a substring in a given string.


str=input("Enter the string:")
substr=input("Enter the substring:")
count=str.count(substr)

print(substr,"is present in",str,":",count,"times.")

____
