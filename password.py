accpetableChar = ["a","b","c","d","0","1","2","3","''","!","}"]

num = int(input("NUM: "))


    
for i in range(num):
        
    if i > len(accpetableChar):
        output = []
        output.append(accpetableChar[i] - 1) 
        i = 0   
    
print(accpetableChar[i])

print(output)