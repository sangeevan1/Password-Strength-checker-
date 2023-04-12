import re
import random
import string

# Function for print the password strength level based on strength score
def passstrenth():
    # Print password as weak if it's get score under 3
    if strength < 3 :
        print("Weak Password")
    # Print password as medium strong if it's get score above 3 and under 5
    elif  strength >=3 and strength!=5  :
        print("Medium strong password")

    # Print password as strong if it's get score 5
    elif strength==5:
        print("Strong password")

# Function to generate password with variable password
def generate_pass(password):
    newpassword = 0
    # Assign syntax and digits to replace letters
    repla = {
        'a': '@',
        'e': '3',
        'i': '!',
        'l': '1',
        'o': '0',
        's': '$',
        't': '+',
    }

    # Replace words into other syntax and digits to make password more strong
    for char, replacement in repla.items():
        password = password.replace(char, replacement)
    return password


    # print(password)


print("Welcome to Password strength Checker ")
print("Tips : Please avoid entering your Date of Birth or your name as a password!")
while True :
    # Getting input from the user
    password = input("Please enter your password : ")
    lenn = len(password)
    strength = 0
    # creating a list variable suggestion
    suggestion = []
    # Checking the password length 
    if lenn >= 12:
        strength += 1
    #Append suggestion
    else:
        suggestion.append("The password should be more than 12 characters.")

       #check the password consists numbers
    num ={'numbers': r'\d'}
    for num in num.values():
     if re.search(num, password) :
        strength += 1
     else :
         suggestion.append(f"The password should contain number.")
    # checking the password having atleast an uppercase
    upper = {'uppercase': r'[A-Z]'}
    for upper in upper.values():
        if re.search(upper, password):
            strength += 1
        else:
            suggestion.append("The password should contain upper cases letters.")
    #Checking the password having a small letters
    lower = {'lowercase': r'[a-z]'}
    for lower in lower.values():
        if re.search(lower, password):
            strength += 1
        else:
            suggestion.append("The password should contain lower cases letters.")
    #checking the password having syntax
    spl = {'special characters': r'[^0-9a-zA-Z]'}
    for spl in spl.values():
        if re.search(spl, password):
            strength += 1
        else:
            suggestion.append("The password should contain special characters.")


    print(f"\nYour Password strength is : {strength}/5")
    passstrenth()

 # Printing suggestions based on the result
    if strength !=5:
        print("---------------------Suggestions---------------------")
        for sug in suggestion:
            print("-> " + sug)
        print("-----------------------------------------------------")
        gva = input("Do you required password suggestion Y or No : ").lower()
        if gva == "y":
            #function for generate new password with random numbers and syntax
            passs = len(password)
            if passs < 12 and passs > 6 :
                random_digits = ''.join(random.choices(string.digits, k=3))
                random_special_chars = ''.join(random.choices(string.punctuation, k=3))
                ran = random_digits + random_special_chars
                print(generate_pass(password.capitalize())+ran)

            elif passs <= 6 :
                random_digits = ''.join(random.choices(string.digits, k=4))
                random_special_chars = ''.join(random.choices(string.punctuation, k=4))
                ran = random_digits + random_special_chars
                print(generate_pass(password.capitalize())+ran)

            else:
                print(generate_pass(password))


    else:
        val = input("Do you want to check another password ? Yes Or No : ").lower()
        if val == "yes":
            pass
        elif val == "no" :
            break
        else:
            print("Check the value")


