
ageclear = False
file = open("usrdata", "a+")
print("what is your name?")
name = input()
while ageclear != True:
    print("what is your age?")
    try:
        age = int(input())
        ageclear = True
        break
    except ValueError:
        print("please enter a number")

print("favorite color")
favcolor = input()

#usrnumber += 1
#file.write("User #" + usrnumber )
file.write(f"\nthe users name is:{str(name)}")
file.write(f"\nthe users age is: {str(age)}")
file.write(f"\nthe users favorite color is: " + favcolor + "\n")

file.close()
