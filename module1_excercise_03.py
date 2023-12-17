number = raw_input("Enter a number greater than 1: ")
resultOfCube = 0

for num in range(0, int(number) +1):
    for i in range(1, int(num)+1):
        numToMultiply = num
        resultOfCube = numToMultiply * numToMultiply * numToMultiply
    print("The cube of " + str(num) + " is " + str(resultOfCube) )