#47 Write a Python program to compute sum of digits of a given string

def getSum(n):
    
    sum = 0
    for digit in str(n): 
      sum += int(digit)      
    return sum
   
n = 26794

print(getSum(n))

# OUTPUT:-28
