def PaymentType():
    question=input ('Choose your payment method: ')
    if question == "credit":
        print("Insert your card")

    elif question == "debit":
        print("Insert your card")

    elif question == "cash":
        print("Insert coin(s) first")

    else: 
        print ("Ask for Assistance")