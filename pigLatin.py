word = input("Enter a word: ")
while word != ".":
    
    vowels = "aeiou"
    isvowel = False
    first_vowel_pos = 0
    first_consonants = ""
    leave = False

    #Test to see if the first letter in the word matches any letter in the vowels string
    for i in range(0,len(vowels)):
        if word[0] == vowels[i]:
            isvowel = True


    if isvowel == True:
        word = word + 'yay'
    else:
                
        for j in range(0,len(word)):                 
                for k in range(0,len(vowels)):
                    if leave == False: 
                        if word[j] == vowels[k]:
                            first_vowel_pos = j
                            first_consonants = word[0:j]
                            word = word[j:len(word)] + first_consonants + "ay"
                            leave = True
    print(word)
    word = input("Enter a word: ")
print("")