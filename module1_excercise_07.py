userInput = " "
numbers = []

while not(str(userInput).__eq__("QUIT")):
    userInput = raw_input("Enter a number or QUIT to quit: ")
    #if its a number, it gets added to the numbers list
    if not(str(userInput).__eq__("QUIT")):
        numbers.append(int(userInput))

#list for even numbers
evenList = []

for i in range(0, len(numbers)):
    #checks which numbers are even and the even numbers get added to a new list
    if int(numbers[i]%2) == 0:
        evenList.append(int(numbers[i]))

#prints all the numbers on the list
print("All Nums" + str(numbers))

#prints the even number
print("Even Nums" + str(evenList))


#Used this website to learn how to compare two strings: https://www.digitalocean.com/community/tutorials/python-string-equals