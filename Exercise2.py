words = raw_input("Enter a string: ")
lowercase =""
uppercase =""

for i in words:
    if i.islower() and i != " ":
        lowercase = lowercase + i
    elif i.isupper() and i != " ":
        uppercase = uppercase + i 

print(lowercase + uppercase)