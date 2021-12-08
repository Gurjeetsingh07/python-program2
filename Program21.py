# Q21. Print the following pattern
'''
    * 
    * * 
    * * * 
    * * * * 
    * * * * *
    * * * *
    * * *
    * *
    *
'''
rows = 5
for i in range(rows):
    for j in range(i):
        print("*", end=' ')
    print('')
num = rows
for i in range(rows, 0, -1):
    for j in range(0, i):
        print("*", end=' ')
    print("\r")
