str=input("Enter a sentense")
freq={}
words=str.split(" ")
for word in words:
    if word not in freq:
        freq[word]=1
    else:
        freq[word]+=1
print(freq)
