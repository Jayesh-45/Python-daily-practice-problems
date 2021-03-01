#1. Write a program to remove the nth index character from a nonempty string.

string=input("Enter the string:")
x=int(input("Enter the index number of the character you want to remove from this string:"))

print("Before removing the character:",string)

print("After removing the character from that index:",string.replace(string[x],""))


____

#2. Write a program to remove the characters which have odd index values of a given string

def removeOddIndex(str):
    y=''
    for i in range(0,len(str)):
        if i%2==0:
            y=y+str[i]
    return y

str=input("Enter the string:")

print("Before removing the odd index values:",str)

print("After removing the odd index values from that string:",removeOddIndex(str))

____
