#Input

inputsec = int(input("Enter the number of seconds: "))

#Eval

inputmin = inputsec//60
sec = inputsec % 60
hr = inputmin//60
minute = inputmin % 60

#Format

hr = str("{:02d}".format(hr))
minute = str("{:02d}".format(minute))
sec = str("{:02d}".format(sec))

#Outputs
print("Result: " + hr + ":" + minute + ":" + sec)

