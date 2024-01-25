elif answer == 'bond':
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
print("Thank you for using this program, have a nice day!")