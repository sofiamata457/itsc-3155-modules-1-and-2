firstList = []
secondList = []

#the for-loop collects five numbers for the first list
for i in range(0,5):
    firstList.append(input("Enter a number for the first list: "))

#the for-loop collects five numbers for the second list
for i in range(0,5):
    secondList.append(input("Enter a number for the second list: "))

#Collects the common numbers
commonList =[]
for a in range(0,5):
    #assigns a number from the firstList to firstNumber variable
    firstNumber = firstList[a]
    #this boolean value is used to check if theres a common value
    commonValue = False
    for b in range(0,5):
        #assigns a number from the firstList to secondNumber variable
        secondNumber = secondList[b]
        #Checks if firstNumber and secondNumber are common values
        if int(firstNumber) == int(secondNumber) :
            #the boolean value is assigned to true
            commonValue = True
    #if commonValue is equal to true then a value is added to the commonList
    if commonValue == True:
        commonList.append(int(firstNumber))

#prints the first list
print("First List: " + str(firstList))

#prints the second list
print("Second List: " + str(secondList))

#prints the common list
print("Common List: " + str(commonList))