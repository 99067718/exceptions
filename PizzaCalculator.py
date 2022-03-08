# Emiel 't Lam
# 99067718
# Pizza Calculator

SmallCost = 5.99
MediumCost = 6.99
LargeCost = 7.50
try:
    print("Hello Costumer, welcome to our pizza-ordering-site")
    name = input("Please enter your name: ")
    adress = input(name + " what is your adress?? : ")
    #Klant krijgt de vraag hoe groot de pizza moet zijn
    print("""
    -------------------------------
    |      Prices                
    |                            
    | Small costs  €5.99         
    | Medium costs €6.99         
    | Large costs  €7.50           
    |                             
    -------------------------------
    """)
    small = int(input("how much small pizza's would you like to have?: "))
    smalltotal = round(float(small) * float(SmallCost),2)
    print(str(small) + " pizza's with a cost of "+ str(smalltotal))

    medium = int(input("how much medium pizza's would you like to have?: "))
    mediumtotal = round(float(medium) * float(MediumCost),2)
    print(str(medium) + " pizza's with a cost of "+ str(mediumtotal))

    large = int(input("how much large pizza's would you like?: "))
    print(str(large) + " pizza's with a cost of "+ str(large * LargeCost))
    largetotal = round(float(large) * float(LargeCost),2)
    amo = small + medium + large
    totalcost = round((small * SmallCost) + (medium * MediumCost) + (largetotal),2)

    # Asks for completion of purchase
    print("------------------------------------------------")
    print("| kosten van bestelling")
    print("| small: "+ str(small) + " € " + str(SmallCost) + " = €" + str(smalltotal))
    print("| medium: "+ str(medium) + " € " + str(MediumCost) + " = €" + str(mediumtotal))
    print("| large: "+ str(large) + " € " +str(LargeCost) + " = €" + str(largetotal))
    print("|")
    print("Total:                €" + str(totalcost))
    print("------------------------------------------------")
    input("Thanks for your order, would you like to pay now, or will you purchase when delivery arrives? : ")
    input("The pizza(s) will be delivered at " + adress + " is that correct? ")
    print("Thanks, "+ name + " you will receive your pizza in " + str(amo * 4) + " minutes.")
except:
    print("something went wrong.")
#order completed
