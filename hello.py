
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

#Capitalize the first letter of each word in the string
name = name.title()

#A simpler way to do all of the above in one line
name = input("Hello,what is your name? ").strip().title()

#prints the final output
print("Nice to meet you,",name)

#split() method splits a string into a list where each word is a list item
first, last = name.split(" ")

print("Your first name is",first)
print("Your last name is",last)
print("Nice to meet you,", name)

myfriends = "john, jane, mary, bob"
friends = myfriends.split(",")
print("These are my friends:", friends)