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

print("{:>15}Upper case {:>5}".format("",upper))
print("{:>15}Lower case {:>5}".format("",lower)
print("{:>15}Digits {:>5}".format("",digits))
print("{:>15}Punctuation {:>5}".format("",punctuation))

