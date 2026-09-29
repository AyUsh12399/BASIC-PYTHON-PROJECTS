string=input("Enter a  string")
string2={}
words=string.split()
for word in words:
    for ch in word:
        if  ch not in string2:
            string2[ch]=1
        else:
            string2[ch]+=1
print(string2)
highest=0
frequentcharcter=""
for i in string2:
    if  string2[i]>highest:
        frequentcharcter=i
        highest=string2[i]
print(frequentcharcter)