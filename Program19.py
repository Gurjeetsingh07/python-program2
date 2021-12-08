# Q19. Program to find the digital product of a given number ex: n=43 Digital product ----->4*3=12
 

n = 4513
product = 1

while (n != 0):
    product = product * (n % 10)
    n = n // 10

print("product of digits of a given number = ",product)

# Output:
# product of digits of a given number =  60
