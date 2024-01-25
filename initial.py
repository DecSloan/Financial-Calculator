import math

print("Welcome to the financial calculator.\n")

while True:
    print("Investment  -  to calculate the amount of interest you'll earn on your investment")
    print("Bond        -  to calculate the amount you will have to pay on a home loan")
    print(" ")
    answer = input("Please enter either 'Investment' or 'Bond' from the menu above to proceed: ")
    answer = answer.strip()
    answer = answer.casefold()
    
    if answer == "investment": 
        print(" ")
        print("Investment selected")
        break

    elif answer == "bond":
        print(" ")
        print("Bond selected")
        break
    
    else: 
        print(" ")
        print("Error!")
        print(" ")