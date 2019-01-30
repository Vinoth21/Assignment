content=""
vowels = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]
consonants="bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
count_V=0
count_C=0
count_S=0
f= open("abc.txt", "r")

con = f.read()
print (con)
for x in con:
    if x is not None: 
        if x in vowels:
            count_V+=1
        elif x in consonants:
            count_C+=1   
        elif x=="\n":
            count_S+=1         
print ("Total Vowels in File : %d" %count_V)
print ("Total Consonants in File : %d" %count_C)
print ("Total Sentences in File : %d" %count_S)

f.close()
