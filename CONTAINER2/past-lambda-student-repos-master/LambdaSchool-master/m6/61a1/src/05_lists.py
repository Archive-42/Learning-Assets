# For the exercise, look up the methods and functions that are available for use
# with Python lists.

# For the following, DO NOT USE AN ASSIGNMENT (=).

x = [1, 2, 3]
y = [8, 9, 10]

# Change x so that it is [1, 2, 3, 4]
x.append(4)
print(x)

# Using y, change x so that it is [1, 2, 3, 4, 8, 9, 10]
x.extend(y)
print(x)

# Change x so that it is [1, 2, 3, 4, 9, 10]
del x[4]
print(x)

# Change x so that it is [1, 2, 3, 4, 9, 99, 10]
x.insert(5, 99)
print(x)

# Print the length of list x
print(len(x))

# Print all the values in x multiplied by 1000
for valueX in x:
    print(valueX*1000)
