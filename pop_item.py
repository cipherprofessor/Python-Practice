test_dict = {"Mohsin": 1, "Manzoor": 2, "Bhat": 3}

# Printing initial dict
print("Before using popitem(), test_dict: ", test_dict)
print("")

# using popitem() to return+
# remove the last keym value pair
res = test_dict.popitem()
print("")

# Printing the pair returned
print('The key, value pair returned is : ', res)
print("")

# Printing dict after deletion
print("After using popitem(), test_dict: ", test_dict)
print("")