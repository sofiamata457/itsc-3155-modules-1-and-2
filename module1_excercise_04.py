number = input("Enter a number: ")
listOfNumber = []

#the for-loop collects all the input for the list of numbers
for i in range(0,int(number)):
    num =  input("Enter number "+ str(i+1) + ": ")
    listOfNumber.append(float(num))

#This calculates the sum of the numbers in the list
sum = 0
for i in range(0,int(number)):
    sum = float(sum) + float(listOfNumber[i])


#prints the list
print("List: " + str(listOfNumber))
#prints the mean
mean = float(sum) / float(number)
print("Average: " + str(mean))



#This website helped me with list comprehension: https://docs.python.org/3/tutorial/datastructures.html#using-lists-as-stacks