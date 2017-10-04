# Here you can write your python code
# The "#" sign tells the python interpreter that this is a comment.

# 'print' is the name of the function
# The string "Hello World" is the argument/input to the function
print("Hello World!")

# 'name' is a variable, a variable is used to store a value
print("What is your name?")
name = input()

# the variable 'name' will hold the value of whatever you type in.

print("Hello " + name + "!")

answer = input("How many states are there in the United States?\n")

# if/else/elif are used to make decisions on what code to run
# They're called control flow statements because they control the flow of your code
# Flow control statements are one of the most fundamental elements of computer programming
# It's how we can make a program do different things based on different circumstances.
if answer == "52":
    print("It can be argued you're correct")
elif answer == "50":
    print("You're correct")
else:
    print("Use Google to answer all the questions in your life")

# Excercise: Write a quick script that asks the user for their age, if they're older than 18
# print 'you're an adult', else print 'alright, cool.'

# Let's say we want to let the user try to answer a question multiple times
# until they get the right answer.
# We would require another flow control statement called a "loop".
# The simplest loop is the "while loop".
# It's just like an if-statement, only it repeats the code 'inside' (indentation)
# the loop until the condition becomes false.

correct_number = "7"
guess_number = input("I'm thinking of a number between 1 and 10. Guess it!\n")

while guess_number != correct_number:
    print("Sorry, that's wrong! Try again!")
    guess_number = input()

print("You got it! Congratulations!")

# You can interpret the loop as follows:
# guess_number = 1, is guess_number not equal to correct number? True, print "sorry" msg and ask for new guess
# guess_number = 2, is guess_number not equal to correct number? True, print "sorry" msg and ask for new guess
# guess_number = 5, is guess_number not equal to correct number? True, print "sorry" msg and ask for new guess
# guess_number = 3, is guess_number not equal to correct number? True, print "sorry" msg and ask for new guess
# guess_number = 7, is guess_number not equal to correct number? False, print "congrats"


# "While" can get you in a lot of trouble if you don't have a way to terminate it.
# Example:
while ("4" == "4"):
    print("INFINITE LOOP!")

# The last thing I want to talk about is types, casting, and formatting strings.
# So far, our numbers are being treated like strings.
# This makes it hard for us to do mathematical stuff with them.
# For example, what is the value of z below?
x = "3"
y = "4"
z = x + y
print("z is " + z)

# If you guessed "34", you are correct!
# If we want to actually add 3 and 4 and store the answer in z, we need to
# cast them as integers.
z = int(x) + int(y)
print("now z is {}".format(z))

# That last thing I did was called "formatting a string". It's a cleaner way to
# do concatenation, but it also works for inputting non-strings into a string.
# For example, the following wouldn't work:
#
# num = 3
# print("num is " + num)
#
# That doesn't work because you can only concatenate a strings with other strings.
# The format() function takes care of this for strings as well as other data types, like integers.
my_string = "Hello {}".format("World!")
print(my_string)
my_string_two = "I am {} years old"
print(my_string_two.format(32))

# With this knowledge about formatting, we can now parse or "read" input strings as
# integer values, which let us do stuff like this:
correct_number = 7
print("I'm thinking of a number between 1 and 10. Guess it!")
guess_number = int(input())
while guess_number != correct_number:
    if guess_number < correct_number:
        print("Too low. Try again!")
    else:
        print("Too high. Try again!")
    guess_number = int(input())
print("You got it! Congratulations!")

# You can interpret the loop as follows:
# guess_number = 5, is guess_number not equal to correct_number? True, go inside the loop
#                   is guess_number less than correct_number? True, print "too low"
#                   ask for new guess.
# guess_number = 8, is guess_number not equal to correct_number? True, go inside the loop
#                   is guess_number less than correct_number? False, print "too high"
#                   ask for new guess.
# guess_number = 7, is guess_number not equal to correct_number? False, end loop
# print "congrats"


# Are you ready to write the whole game? Let's begin!

# For your homework you will need to generate a random number between 1 and 20.
# To do this, we can import a module. A module is essentially code someone else has
# written that you can use. They're very useful since you don't have to implement it or
# even understand how it works.

# Here we can import random and call the randint() function
import random
x = random.randint(1, 20)
print(x)
