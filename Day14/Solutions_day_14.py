'''Problem .
- Write a program to Convert an IP Address from Decimal to Binary Form, without using the Decimal to binary in-built function [bin(n)]
- Input format:- '140.65.215.159'
- Output format:- '10001100.1000001.11010111.10011111'
'''

def conver(num):
    if num>0:
        conver(num//2)
        print(num%2,end='')

number=input("Enter the Address")
y=number.split('.')

for i in y:
    c=int(i)
    conver(c)
    print('.',end='')
    
____
