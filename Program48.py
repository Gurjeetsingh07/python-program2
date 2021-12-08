#48 Write a Python function that takes a list of words and returns the length of the longest one

def longest_length_string(my_string):
   len_str = len(my_string[0])
   temp_val = my_string[0]

   for i in my_string:
      if(len(i) > len_str):

         len_str = len(i)
         temp_val = i

   print("The word with the longest length is:", temp_val, " and length is ", len_str)

my_string = ["three", "Jane", "quick", "lesson", 'London', 'newyork']
print("The list is :")
print(my_string)
longest_length_string(my_string)

# OUTPUT:-The list is :
#         ['three', 'Jane', 'quick', 'lesson', 'London', 'newyork']
# The word with the longest length is: newyork  and length is  7
