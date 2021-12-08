# Q52. Write a function that computes the area of a rectangle. Then, write a second function that calls this function three times to compute the surface area of a rectangular solid.

 
def arear(w,l):
    return 2*w*l

def arear(h,l):
    return 2*h*l

def arear(w,h):
    return 2*w*h

def arear(l,w):
    return (l*w)

# main code begins   
l = int(8)
w = int(2)   
h = int(6)
print("Area of rectangle = ",arear(l,w))
print("surface area of rectangular solid = ", arear(w,l)+arear(h,l)+arear(w,h))      


# Output: 
# Area of rectangle =  16
# surface area of rectangular solid =  76
