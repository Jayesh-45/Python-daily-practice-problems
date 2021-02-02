#1. Write a program to print a Dictionary line by line.

dict_score={}

x=int(input("Enter no of items you want in your Dictionary:\n"))
i=1
name=''
score=0

while(i<=x):
    name=input("Enter the Name of Student:")
    score=int(input("Enter the Score:"))
    dict_score[name]=score
    i=i+1

print("Your Dictionary is:")
for key,value in dict_score.items():
    print(key,":",value)

____

#2. Write a program to check if multiple keys exist in a dictionary.

checkDict={"Mon":"chest",
       "Tue":"back",
       "Wed":"B/T",
       "Thur":"Should",
       "Fri":"Legs"}

keys={"Mon","sat"}

if(checkDict.keys())>=keys:
    print("Yes.")
else:
    print("No.")


____

#3. Write a program to count number of items in a dictionary value that has a list.

checkDict={'a':[1,5,4,6,88,910],
           'b':45,
           'c':[81,66,11],
           'd':3,
           'e':[17,19]}
count=0

for key,value in checkDict.items():
    if isinstance(value,list):
        count=count+len(value)

print("The no of items in this Dictionary value that is a list is:",count)

____
