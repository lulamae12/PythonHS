# Write a function that, given a number, returns True if the number is strictly increasing,
# or returns False if it is not.  For example, 2579 would return True, while
# 9742 would return False

def getnumber():
    while True:
        try:
            number = int(input("please enter your number:"))
            number = eval_increase(number)

        except(ValueError):
            print("that is not a valid number!")
def eval_increase(number):
    x = 1
    print(number)
    numberssplit = [int(x) for x in str(number)]#converts to string to iterate and the back to integer.
    previousnumber = numberssplit[0]#sets to first cus python goes to 0
    for number in numberssplit:
        if number < previousnumber:
            print("False. the number is monotonically decreasing")
            return
        previousnumber = number#sets number to previous
    print('True. the number is monotonically increasing')


getnumber()
