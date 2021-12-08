# Take the following Python code that stores a string: ‘str = 'Y-tatata-acropolis: 0.8475'. Use find and string
# slicing to extract the portion of the string after the colon character and then use the float function to convert
# the extracted string into a floating point number.

str = 'Y-tatata-acropolis: 0.8475'
start = str.find(':')
end = len(str)

number = str[start+1:end]

fpnumber = float(number)
print(fpnumber)

# OUTPUT:- 0.8475
