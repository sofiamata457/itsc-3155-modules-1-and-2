listOfWords = []
#This for-loop creates the list of strings
for i in range(0,5):
    word = raw_input("Enter a word: ")
    listOfWords.append(str(word))

#This for-loop will take the values in the list and make it into one string
oneString = " "
for i in range(0,5):
    oneString = oneString + listOfWords[i] + " "

#prints the list of words
print("Words: " + str(listOfWords))

#prints the words that are in one string
print("One String" + str(oneString))