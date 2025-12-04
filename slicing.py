'''
Goal: Practice element access and slicing.
'''

# Create a 'temperatures' list
Initial_list: list[str] = ["15", "18", "22", "25", "28", "30", "27", "24", "20"] 

# ------------ #

# Print the first temperature
print(Initial_list[0]) 

# SPrint the last temperature
print(Initial_list[-1]) 

# Print the temperatures from position 2 up to 5 (excluse)
print(Initial_list[1:4])

# Print all temperatures with step 2 (skipping one every two)
print(Initial_list[::2])

# Print the list
print(Initial_list)