# Q36. Write a Python program to add 'polis' at the end of a given string (length should be at least 3). If the given string already ends with 'polis' then add 'polisCS' instead. If the string length of the given string is less than 3, leave it unchanged. 

# Sample String : 'abc' Expected Result : 'abcpolis' Sample String : 'Acropolis' Expected Result : 'AcropolisCS'

def add_string(str1):  
  length = len(str1)  
  
  if length > 2:  
    if str1[-5:] == 'polis':  
      str1 += 'CS'  
    else:  
      str1 += 'polis'  
  
  return str1  
print(add_string('ab'))  
print(add_string('abc'))  
print(add_string('Acropolis'))

# output:

# ab
# abcpolis
# AcropolisCS
