# Q15. Write a program to input electricity unit charges and calculate total electricity bill according to the given condition:
# For first 50 units Rs. 0.50/unit
# For next 100 units Rs. 0.75/unit
# For next 100 units Rs. 1.20/unit
# For unit above 250 Rs. 1.50/unit
# An additional surcharge of 20% is added to the bill

u = int(input('Enter The Amount Of Units Consumed:'))

if u <= 50:
    amt = u*0.50
    print('Amount To Be Paid Is:',amt)

elif u <= 150 and u > 50:
    amt = (50*0.5) + ((u-50)*0.75)
    print('Amount To Be Paid Is:',amt)

elif u <= 250 and u > 150:
    amt = (50*0.5) + (100*0.75) + ((u-150)*1.2)
    print('Amount To Be Paid Is:',amt)

else:
    amt = (50*0.5) + (100*0.75) + (100*1.2) + ((u-250)*1.5)
    print('Amount To Be Paid Is:',amt)

print('Process Completed')

# output :

# Enter The Amount Of Units Consumed:100
# Amount To Be Paid Is: 62.5
# Process Completed
