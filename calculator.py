# The code below concatenates(meaning joins) the inputs as strings.it does not add them as numbers.
#To add them as numbers, we need to convert the inputs to integers.
x = input("Enter x: ")
y = input("Enter y: ")
z = x + y
print( z)

#The code below converts the inputs to integers using int() function before adding them.
x = int(input("Enter x: "))
y = int(input("Enter y: "))
z = x + y
print(z)

#To make the code more concise, we can combine the input and int() conversion in one line.
print(int(input("Enter x: ")) + int(input("Enter y: ")))

#Float numbers
x = float(input("Enter x: "))
y = float(input("Enter y: "))
z = x + y
print(z)

#round() function;used to round off float numbers to the nearest integer or to a specific number of decimal places.
print(round(z)) #Rounds to the nearest integer
print(round(z, 2)) #Rounds to 2 decimal places


print(f"{z:,}")     #Formats the number with commas as thousand separators eg 1,000,000

#Division
x = int(input("Enter x: ")) 
y = int(input("Enter y: "))
z = x / y          #Standard division;result is always a float
print(z)