print("Enter 10 Elements: ")
arr = []
for i in range(10):
    arr.append(input())

print("\nEnter the Value to Delete: ")
val = input()

arr.remove(val)
print(arr)
