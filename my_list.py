# my_list variable 
my_list = []
my_new_list = [10, 20, 30, 40]
for item in my_new_list:
    my_list.append(item)
print(my_list)


# Insert 15 at index 2
my_list = my_list[:2] + [15] + my_list[2:]
print(my_list)

another_list = [50, 60, 70]
#Extend my_list with another_lsit
my_list.extend(another_list)
print(my_list)

# Remove the last element from my_list
my_list.remove(70)
print(my_list)

# Sort my_list in ascending order
my_list.sort()

print(my_list)

# Find and print the index of the value of 30
value = 30
try:
    index = my_list.index(value)
    print(f"The index of '{value}' is: {index}")
except ValueError:
    print(f" '{value}' is not found in the list.")
