list=[]
choice=1

while choice :
    names=input("Enter the name u want to add : ")
    
    list.append(names)
    choice=int(input("Do you want to add more names : 1/0 :"))
list2=[]
count=0
for name in list:
    if name not in list2:
        list2.append(name)
   
print(list2)