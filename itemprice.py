struct={}
higest=0
name1=""
name2=""
lowest=999999
for i in range(5):
    name=input("enter the item name :")
    price=int(input("enter the price :panne"))
    struct[name]=price
lis1=[]
list2=[]
for i in struct:
    lis1.append(i)
for i in struct:
    list2.append(struct[i])
for i in struct:
    if struct[i]>higest:
        name1=i
        higest=struct[i]
    elif struct[i]<lowest:
        name2=i
        lowest=struct[i]

print("highest priced",name1)
print("lowest priced",name2)
print(sum(list2))

