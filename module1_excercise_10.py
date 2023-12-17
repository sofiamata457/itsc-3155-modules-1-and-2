word = raw_input("Enter a string: ")
arrayOfSingleCharacters = list(word)
#print(arrayOfSingleCharacters)

#this is the "last array"
listOfThrees = []
#used to hold only 3 values, this is the "inner array"
threeList = []

for i in range(0,len(arrayOfSingleCharacters)):
    #once there are three characters in the inner array, the inner array gets added to the last array
    if len(threeList) == 3:
        listOfThrees.append((threeList))
        threeList = []
        threeList.append((arrayOfSingleCharacters[i]))
    #characters are added to the inner array, as long as there are less then three characters in the inner array
    elif len(threeList) < 3:
        threeList.append((arrayOfSingleCharacters[i]))
        #This allows the remaining characters to be added to the last array
        if int(i) == len(arrayOfSingleCharacters) -1:
            listOfThrees.append((threeList))
            threeList= []

print(listOfThrees)