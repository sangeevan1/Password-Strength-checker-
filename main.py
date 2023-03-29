import re
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


    print(f"\nYour Password strength is : {strength}/5\n")
    if strength !=5:
        print("---------------------Suggestions---------------------")
        for sug in suggestion:
            print("-> " + sug)
        print("-----------------------------------------------------")

    else:
        val = input("Do you want to check another password ? Yes Or No : ").lower()
        if val == "yes":
            pass
        elif val == "no" :
            break
        else:
            print("Check the value")
