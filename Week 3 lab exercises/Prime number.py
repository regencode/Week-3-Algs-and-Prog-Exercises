#input


num = int(input("Enter a number: "))

#Check
check = 2
while num % check != 0:
   # print(check) #testing loop
    check += 1


#Outputs
if num == check:
    print("The number " + str(num) +" is a prime number")
elif num > check:
    print("The number " + str(num) + " is not a prime number")