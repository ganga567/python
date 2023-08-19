#2. From a string,concatinate a vowel for each characte in string and store it in a list

string1 = "string"
vowels = ["a","e","i","o","u"]
for i in string1:
    for j in vowels:
        print(i + j,end=" ")
