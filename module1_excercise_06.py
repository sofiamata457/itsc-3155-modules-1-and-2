import sys
row = input("Enter a row num from 1 to 5: ") #2
column = input("Enter a column num from 1 to 5: ") #4


bValue = False
#This for-loop prints each row
for a in range(0, 5):
    if int(a) == int(row-1):
        bValue = True
    else:
        bValue = False
    #This for-loop prints each column
    for b in range(0, 5):
        if int(b) == int(column-1) and bValue == True:
            sys.stdout.write("1 ")
        elif (int(b) < 4):
            sys.stdout.write("0 ")
        else:
            print("0")


#I used this website to help me print the number of values on the same print line for each row: https://www.geeksforgeeks.org/print-without-newline-python/