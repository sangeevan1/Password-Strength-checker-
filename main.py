import re

def passstrenth():
    if strength < 3 :
        print("Weak Password")
    elif  strength >=3 and strength!=5  :
        print("Medium strong password")
    elif strength==5:
        print("Strong password")

def generate_pass(password):

    repla = {
        'a': '@',
        'e': '3',
        'i': '!',
        'l': '1',
        'o': '0',
        's': '$',
        't': '+',
    }

    for char, replacement in repla.items():
     password = password.replace(char, replacement)




    print(password)

print("Welcome to Password strength Checker ")
print("Tips : Please avoid entering your Date of Birth or your name as a password!")
while True :
    password = input("Please enter your password : ")
    lenn = len(password)
    strength = 0
    suggestion = []
    if lenn >= 12:
        strength += 1
    else:
        suggestion.append("The password should be more than 12 characters.")
    num ={'numbers': r'\d'}
    for num in num.values():
     if re.search(num, password) :
        strength += 1
     else :
         suggestion.append(f"The password should contain number.")

    upper = {'uppercase': r'[A-Z]'}
    for upper in upper.values():
        if re.search(upper, password):
            strength += 1
        else:
            suggestion.append("The password should contain upper cases letters.")
    lower = {'lowercase': r'[a-z]'}
    for lower in lower.values():
        if re.search(lower, password):
            strength += 1
        else:
            suggestion.append("The password should contain lower cases letters.")

    spl = {'special characters': r'[^0-9a-zA-Z]'}
    for spl in spl.values():
        if re.search(spl, password):
            strength += 1
        else:
            suggestion.append("The password should contain special characters.")


    print(f"\nYour Password strength is : {strength}/5")
    passstrenth()


    if strength !=5:
        print("---------------------Suggestions---------------------")
        for sug in suggestion:
            print("-> " + sug)
        print("-----------------------------------------------------")
        gva = input("Do you required password suggestion Y or No : ").lower()
        if gva == "y":
            generate_pass(password)
    else:
        val = input("Do you want to check another password ? Yes Or No : ").lower()
        if val == "yes":
            pass
        elif val == "no" :
            break
        else:
            print("Check the value")


