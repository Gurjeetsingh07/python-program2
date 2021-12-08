# Write a function that returns the middle value among three integers. (Hint: make use of min() and max()).
# Write code to test this function with different inputs.


def middle(a, b ,c) :
    m = min(a,b,c)
    M = max(a,b,c)
    R = a+b+c-m-M
    return R

print(middle(8,7,6))

# OUTPUT:- 
# middle value: 7
