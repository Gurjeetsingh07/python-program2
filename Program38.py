# Q38. Write a Python program to change a given string to a new string where the second and last chars have been exchanged.

def change_sring(str1):
      return str1[0] + str1[-1] + str1[2:-1] + str1[1]
	  
print(change_sring('abcd'))
print(change_sring('12345'))

# Output:

# adcb                                                                                                          
# 15342
