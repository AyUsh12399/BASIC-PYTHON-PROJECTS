struct={

}
choice=1
sum=0
while(choice):
    names=input("Enter the player name :")
    score=int(input("Ennter the score :"))
    struct[names]=score
    choice=int(input("Do u want to add more 1/0 : "))
print(struct)
higestplayer=" "
lowestplayer=" "
higestscore=0
lowestscore=500
for i in struct:
    if struct[i]>higestscore:
        higestplayer=i
        higestscore=struct[i]
    if struct[i]<lowestscore:
            lowestplayer=i
            lowestscore=struct[i]
for values in struct.values():
     sum+=values
avg=sum/len(struct)
print("The avg score is :",avg)
print("THE HIGEST PLAYER IS :",higestplayer)
print("THE LOWEST PLAYER IS :",lowestplayer)