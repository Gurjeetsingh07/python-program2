# Q13. Write a program to input marks of five subjects Physics, Chemistry, Biology, Mathematics and Computer. Calculate percentage and grade according to following:
# Percentage >= 90% : Grade A
# Percentage >= 80% : Grade B
# Percentage >= 70% : Grade C
# Percentage >= 60% : Grade D
# Percentage >= 40% : Grade E
# Percentage < 40% : Grade F

mark = []
print("Enter 5 different marks : ")
x=1
for i in range(5):
    mark.append(int(input("sub " + str(x) + " marks =")))
    x=x+1

p = (sum(mark)/500)*100
print("percentage of students = ",p)

if p>=90:
    print("Grade A")
elif p>=80:
    print("Grade B")
elif p>=70:
    print("Grade C")
elif p>=60:
    print("Grade D")
elif p>=40:
    print("Grade E")
else:
    print("Grade F")


# Output:

# Enter 5 different marks : 
# sub 1 marks =40
# sub 2 marks =50
# sub 3 marks =30
# sub 4 marks =60
# sub 5 marks =80
# percentage of students =  52.0
# Grade E
