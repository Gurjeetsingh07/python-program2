# Q22 Program to reverse a given Number. ex: n=123 Reversed no is 321

n = 4562
rev = 0
 
while(n > 0):
    a = n % 10
    rev = rev * 10 + a
    n = n // 10
 
print("Reverse value = ",rev)

# Output:
# Reverse value =  2654
