import numpy as np
x = np.array([[0, 10, 20], [20, 30, 40]])
print("Original array: ")
print(x)
# choosing a specific value
a = 10

# finding the row values with value greater than 10
answer = np.where(np.any(x > a, axis = 1))

print("Result: \n", answer)
