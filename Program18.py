# Q18. Program to find digital sum of a given Number ex: n=123 Digital sum----->1+2+3=6


n = 687
sum = 0
while (n != 0):
    sum = sum + int(n % 10)
    n = int(n/10)

print("sum of digits of a given number = " ,sum)

# Output :

# sum of digits of a given number =  21
