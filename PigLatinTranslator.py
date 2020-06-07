# English to Pig Latin
print('Enter the English message to translate into Pig Latin:')
message = str(input())

VOWELS = ('a', 'e', 'i', 'o', 'u', 'y')

pigLatin = [] # A list of the words in Pig Latin.
for word in message.split():
    # Separate the non-letters at the start of this word:
    prefixNonLetter = ''
    while len(word) > 0 and not word[0].isalpha():
        #save the character to a prefix to prepend later
        prefixNonLetter += word[0]
        word = word[1:]
    if len(word) == 0:
        pigLatin.append(prefixNonLetter)
        continue

    #Separate the non letters at the END of the word.
    suffixNotLetter = ''
    while len(word) > 0 and not word[-1].isalpha():
        #save character to a suffix this time
        suffixNotLetter += word[-1]
        word = word[:-1]
    # Correct the order of suffixNonLetter, as it was recorded from last to first
    suffixNotLetter = suffixNotLetter[::-1]

    # Remember if the word was in uppercase or title case.
    wasUpper = ''
    wasTitle = ''
    if word.isupper():
        wasUpper = True
    if word.istitle():
        wasTitle = True

    # Make lowercase to translate
    word = word.lower()

    # Separate the consonants at the start of this word:
    consonantStart = ''
    while len(word) > 0 and word[0] not in VOWELS:
            consonantStart += word[0]
            word = word[1:]

    # Add the Pig Latin ending to the word:
    if consonantStart != '':
        word += consonantStart + 'ay'
    else:
        word += 'yay'

    # Set the word back to uppercase or title case:
    if wasUpper:
        word = word.upper()
    if wasTitle:
        word = word.title()

    # Add the non-letters back to the start or end of the word.
    word = prefixNonLetter + word + suffixNotLetter
    pigLatin.append(word)

    # Join all the words back together into a single string:
pigLatin = ' '.join(pigLatin)
print(pigLatin)
