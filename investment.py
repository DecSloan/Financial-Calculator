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