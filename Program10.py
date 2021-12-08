# Q10. A shop will give discount of 50% if the cost of purchased quantity is more than 10000. Ask user for quantity suppose, one unit will cost 100. Judge and print total cost for user.

quan = int(input("Enter quantity : "))

if (quan*100) > 10000: 
    print("Cost is",((quan*100)-(0.5*quan*100)) )
else: 
    print("Cost is",(quan*100))

# Output : 

# Enter quantity : 100
# Cost is 10000
