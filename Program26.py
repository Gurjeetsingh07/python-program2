# Q26. Program to find whether a given number is a strong number or not. e.g. n=145 1!+4!+5!==145
  
sum=0  
num=int(input("Enter a number:"))  
temp=num  
while(num):  
    i=1  
    fact=1  
    rem=num%10  
    while(i<=rem):  
        fact=fact*i
        i=i+1  
    sum=sum+fact  
    num=num//10  
if(sum==temp):  
    print("Given number is a strong number")  
else:  
    print("Given number is not a strong number")  

# Output:
# Enter a number: 145
# Given number is a strong number.
