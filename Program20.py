# Q20. Find the sum of the series 3 +33 + 333 + 3333 + .. n terms

n=int(input("Enter the range of number:"))
sum=0
p=3
for i in range(1,n+1):
    sum += p
    p=(p*10)+3
print("The sum of the series = ",sum)

# Output:
# Enter the range of number:10
# The sum of the series =  3703703700
