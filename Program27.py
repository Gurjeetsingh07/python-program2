# Q27. Program to find whether a given number is a unique number. For example, 20, 56, 9863, 145, etc. are the unique numbers while 33, 121, 900, 1010, etc. are not unique numbers


n = input("Enter the number you want to check: ")
l=len(n)
flag=0
i=0

while i<l-1:
    j=i+1
    while j<l:
        if n[i]==n[j]:
            flag=1
            break
        j=+1
    i=+1

if flag == 0:
    print("The number is unique.")
else:
    print("The number is not unique.")

# output:
# Enter the number you want to check: 33
# The number is not unique.
