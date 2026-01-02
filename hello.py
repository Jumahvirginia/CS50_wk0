
# print("hello,world")
#print("This is cs50P:Programming in Python")
#input("Hello,what is your name?")
#print("Nice to meet you,")

name = input("Hello,what is your name? ")

#Remove whitespace from beginning & end of string
name = name.strip()

#Capitalizes the name
#It only Capitalizes only the first letter of the string
name = name.capitalize()

print("Nice to meet you,",name)
