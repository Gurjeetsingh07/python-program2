# Q30. Print downward Half-Pyramid Pattern with Star (asterisk) 
'''
        * * * * * 
         * * * * 
          * * * 
           * * 
            * 
'''

rows = 5
  
k = 2 * rows - 2  
for i in range(rows, -1, -1):  
    for j in range(k, 0, -1):  
        print(end=" ")  
    k = k + 1  
    for j in range(0, i + 1):  
        print("*", end=" ")  
    print("")
