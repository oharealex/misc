def abv_calculator():
    start = input("Enter your starting gravity \n")
    end = input("Enter your ending gravity \n")
    abv = (float(end)-float(start))*-131.25
    print("Your ABV is", str(round(abv,2))+"% \n")
    user = input("To start again, press 1, to close press 2 \n")
    if user == "1":
        abv_calculator()
    else:
        quit()

abv_calculator()
