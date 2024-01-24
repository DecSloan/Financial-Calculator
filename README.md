# Financial Calculator
**Simple program that allows users to access two different types of calculator**

The aim of this task is to calculate either the repayments on a loan or the interest earned on an investment based on user inputs. 

---
## Initial

First a welcome message is displayed, then the user is asked to enter either investment or bond to continue.
Users answer is stripped and formatted to all lower case to avoid entry errors.
Error message displayed when invalid input i.e not investment or bond.
While loop created so that only broken once valid input is entered.

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
            
