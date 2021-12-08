# Q29. Program to find whether a given number is a prime number or not.

a = int(input("Enter an input number:"))  

if a > 1:  
    for j in range(2, int(a/2) + 1):  
        if (a % j) == 0:  
            print(a, "is not a prime number")  
            break 
    else:  
        print(a, "is a prime number")  
else:  
    print(a, "is not a prime number") 

# Output:
# Enter an input number:17
# 17 is a prime number
