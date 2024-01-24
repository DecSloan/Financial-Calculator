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

## Investment

If investment selected user is then prompted to enter more info e.g. amount, interest rate, years saving.
User inputs are stored and entered into equations, these outcomes are then rounded to 2 decimal places. 
Then they are formatted so they conform to normal currency standards.

    if answer == "investment":
        print(" ")
        amount = float(input("Please enter the amount you wish to deposit: "))
        interest_rate = float(input("Please enter the chosen interest rate: "))
        years = int(input("Please enter the number of years you would like to invest: "))

        r = interest_rate / 100
        simpleA = amount * (1 + r * years)
        compoundA = amount * math.pow((1 + r), years)

        rounded_simpleA = round(simpleA, 2)
        answer_simpleA = "{:,}".format(rounded_simpleA)

        rounded_compoundA = round(compoundA, 2)
        answer_compoundA = "{:,}".format(rounded_compoundA)

User asked if they want simple or compound interest, the relevant equation needed is then selected.
Message is printed with the total at the end of the amount of years selected.
If no valid input selected then error message displayed and repeat through while loop until 'simple' or 'compound' selected.
       
        while True:
            interest = input("Please enter either 'simple' or 'compound' interest: ")
            print(" ")
            interest = interest.strip()
            lowercased_interest = interest.casefold()

            if lowercased_interest == "simple":
                print(f"Your total at the end of the {years} year/s would be £{answer_simpleA}")
                break

            elif lowercased_interest == "compound":
                print(f"Your total at the end of the {years} year/s would be £{answer_compoundA}")
                break

            else:
                print("Error")
                print(" ")

## Bond

If bond selected then user prompted to enter more info e.g. house price, interest rate, months to pay back.
User inputs then stored and entered into equation, this outcome is then rounded down to 2 decimal places.
Then it is formatted to conform to normal currency standards. 
Monthly repayment then displayed. 

    if answer == 'bond':
        print(" ")
        house_value = int(input("Please enter the value of the house: "))
        interest_rate = float(input("Please enter the chosen interest rate: "))
        months = int(input("Please enter the number of months you want to take to repay: "))
        print(" ")

        i = (interest_rate / 100) / 12
        repayment = (i * house_value) / (1 - (1 + i) ** (-months))

        rounded_repayment = round(repayment, 2)
        monthly_repayment = "{:,}".format(rounded_repayment)

        print(f"Your monthly repayment would be £{monthly_repayment}")

    print(" ")
    print("Thank you for using this program, have a nice day!")oading bond.py…]()

Thanks for checking this out, you can run the full program and try it out for yourself.
