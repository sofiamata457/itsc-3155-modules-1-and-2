originalList = []
numsThatAppearOnce = []
for i in range(0, 10):
    number = input("Enter number " + str(int(i)+1) + ": ")
    originalList.append(int(number))

#Checks how many times a number appears in the original list
for a in range(0,10):
    firstNum = originalList[a]
    #boolean to track if two values are the same
    sameValue = False
    for b in range(a,9):
        secondNum = originalList[int(b)+1]
        #compares firstNum and SecondNum
        if int(firstNum) == int(secondNum):
            sameValue = True

    if sameValue == False:
            numsThatAppearOnce.append(int(firstNum))

        

print("Original List: " + str(originalList))
print("Nums that appear once: " + str(numsThatAppearOnce))