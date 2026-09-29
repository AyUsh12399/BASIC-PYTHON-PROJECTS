list=[]
for i in range(1,6):
        marks=int(input("Enter the marks of student :"))
        list.append(marks)
avg=sum(list)/len(list)
print("The Average mark is ",avg)
higest_marks=max(list)
lowest_marks=min(list)
print("The Highest marks is ",higest_marks)
print("The Lowest marks is ",lowest_marks)

if avg>=90:
        print("GRADE A")
elif avg>=75 and avg<=89:
        print("GRADE B")
elif avg>=60 and avg<=74:
        print("GRADE C")
else:
        print("GRRADE D")