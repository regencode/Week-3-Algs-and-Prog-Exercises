
#inputs

totalbill = int(input("Enter total amount of bill: "))
totalpeople = int(input("Enter number of people: "))
percenttip = float(input("Enter amount of tips (%) : "))

#Eval

totaltip = totalbill*(percenttip/100)
persontip = totaltip/totalpeople
personbill = (totalbill + totaltip)/totalpeople

#Formatting float values to 2 decimal places

persontip = "{:.2f}".format(persontip)
personbill = "{:.2f}".format(personbill)

#prints

print("\nTip amount per person $" + str(persontip))
print("Total amount per person $" + str(personbill))


