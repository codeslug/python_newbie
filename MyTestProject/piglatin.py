'''
Created on Dec 19, 2013

@author: codeslug

This document converts a single word to "pig latin."

Rules of pig latin:

1. The first letter of a word is taken, added to the end of the word, followed by "ay." dog == ogday
2. If the first letter of the word is a vowel, it is not removed, but "ay" is still added to the end of the word.
3. If rule # 2 applies, and the last letter of the word is a vowel, it is completely replaced with "ay." apple == applay
4. If the first letter of a word is a consonant, the following consonants are also removed and added to the end of the word.
    So, cream == eamcray, and three == eethray
5. The letter "y" is treated as a consonant in all cases.
'''

pyg = 'ay'

original = raw_input('Enter a word:')

if len(original) > 0 and original.isalpha(): #check name validity
    word = original.lower() #reduce to lower case
    first = word[0] #grabs first letter
    last = word[len(word) - 1] #grabs last letter
    
    if (first == "a") or (first == "e") or (first == "i") or (first == "o") or (first == "u"): #checks for vowel
        new_word = (word + pyg) #assembles pyg word for vowel
        print new_word       
    else:
        if (last == "a") or (last == "e") or (last == "i") or (last == "o") or (last == "u"): #checks vowel
            new_word = word[1:(len(word))] + (word[0]) + pyg #assembles pyg word for consonant, single letter
        else:
# still debugging !!            
            print "consonant"
                    
        print new_word
else:
    print 'Sorry, your answer is invalid. Please enter a name with only letters.'
