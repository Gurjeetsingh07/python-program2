# Q53. Create an outer function that will accept three parameters, a, b and c. Create an inner function inside an outer function that will calculate the addition of a, b and c. At last, an outer function will add 5 into addition and return it

# outer function
def outer_fun(a, b, c):
    

    # inner function
    def addition(a, b,c):
        return a + b + c

    # call inner function from outer function
    add = addition(a, b, c)
    # add 5 to the result
    return add + 5

result = outer_fun(5, 10,15)
print(result)
