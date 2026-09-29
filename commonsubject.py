set1=set()
set2=set()
choice=1
choice2=1
while(choice):
    subject=input("ENTER THE SUJECTS OF  FIRST STIDET  : ")
    set1.add(subject)
    choice=int(input("Do u want to continue 1/0 :"))
 
while(choice2):
    subject2=input("ENTER THE SUJECTS OF  SECOND STUDENT : ")
    set2.add(subject2)
    choice2=int(input("Do u want to continue 1/0 :"))
print("common subjets",set1 & set2)
print("subject only in  first student",set1-set2)
print("subject only in  second student",set2-set1)