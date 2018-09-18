sentence = input('Enter a sentence: ')
upper = 0
lower = 0
digits = 0
punctuation = 0

for i in range(0,len(sentence)):
    if sentence[i].isupper() == True:
        upper += 1
    elif sentence[i].islower() == True:
        lower += 1
    elif sentence[i].isdigit() == True:
        digits += 1
    elif sentence[i].isalnum() == False and sentence[i] != " ":
        punctuation += 1

print("{:>15s}{:>5d}".format("Upper case",upper))
print("{:>15s}{:>5d}".format("Lower case",lower))
print("{:>15s}{:>5d}".format("Digits",digits))
print("{:>15s}{:>5d}".format("Punctuation",punctuation))

