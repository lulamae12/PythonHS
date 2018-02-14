#question number 3
#in python 3
print("please type in a WHOLE number no longer than 10 digits.inputs that are not numbers will error")
num = int(input("Enter a number: "))
if type(num) is int:
    print("Original number:" + str(num))

    digits = []
    for digit in str(num):
        digits.append (int(digit))

    print(digits)
else:
    print('Non-numeric data found in the input.')
