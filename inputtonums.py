#in python 
print("please type in a WHOLE number no longer than 10 digits.inputs that are not numbers will error")
num = int(input("Enter a number: "))
if type(num) is int:
    print("Original number:" + str(num))

    c = []
    for digit in str(num):
        c.append (int(digit))

    print(c)
else:
    print('Non-numeric data found in the input.')
