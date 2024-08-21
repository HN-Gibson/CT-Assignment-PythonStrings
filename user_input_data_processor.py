# Objective: The aim of this assignment is to process and format user input data.

# Task 1: Input Length Validator Write a script that asks for and checks the length of the user's first name and last name. Both should be at least 2 characters long. If not, print an error message.

def input_length_validator(variable):
    if len(variable) >= 2:
        print ("Thank You!")
    else:
        print ("Invalid Entry: Ensure you enter atleast two characters.") 

while True:
    first_name = input ("What is your first name? ")
    input_length_validator(first_name)
    last_name = input ("What is your last name? ")
    input_length_validator(last_name)

    continue_input = input("Would you like to enter another name? (yes/no)").lower()
    if continue_input != "yes":
        print (f"Goodbye, {first_name} {last_name}!")
        break