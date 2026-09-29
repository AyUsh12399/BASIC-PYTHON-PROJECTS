str=input("Enter the string")
count_vowel=0
count_consonant=0
count_space=0
count_digit=0
list=[0,1,2,3,4,5,6,7,8.9]
for ch in str:
    if ch in "AEIOUaeiou":
        count_vowel+=1
    if ch not in "AEIOUaaeiou":
        count_consonant+=1
    if ch.isdigit():
                count_digit+=1
    if ch==" ":
        count_space+=1
print(count_space,"Number of spaces")
print(count_digit,"Number of digit")
print(count_consonant,"Number of consonants")
print(count_vowel,"Number of vowels")