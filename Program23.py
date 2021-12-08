# Q23. Program to check whether a given number is a palindrome or not

n=int(input("Enter number:"))
temp=n
rev=0
while(n>0):
    dig=n%10
    rev=rev*10+dig
    n=n//10
if(temp==rev):
    print("The number is a palindrome!")
else:
    print("The number isn't a palindrome!")


# Output:

# Enter number:20
# The number isn't a palindrome!

# Enter number:232
# The number is a palindrome!
