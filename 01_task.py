print("-----------------List-------------------")
print("\n")
#  Creating a List

my_list = [10,20,25,35,50]
print("Initial List:",my_list)

# Add an element in the list.

my_list.append(65)
print("List after adding an element :",my_list)

# Removing an element from the list.

my_list.remove(35)
print("List after removing an element:",my_list)

# Modify an element in the list.

my_list[2] = 30
print("List after modifying an element:",my_list)


print("\n")

print("-----------------Dictionary-------------------")
print("\n")
# Creating a Dictionary

my_dict = {"Name":"Harsh","age":20,"city":"Noida"}
print("Initial Dictionary:",my_dict)

# Add an element in the Dictionary.

my_dict["Category"] = "General"
print("Dictionary after adding an element:",my_dict)

# Removing an element from the Dictionary.

del my_dict["age"]
print("Dictionary after Removing an element:",my_dict)

# Modify an element in the dictionary.

my_dict["city"] = "Greater Noida"
print("Dictionary after Modifying an element:",my_dict)


print("\n")

print("-----------------Sets-------------------")
print("\n")
# Creating a Set.

my_set = {1,2,3,4,5}
print("Initial Set :",my_set)

# Adding an element in set.

my_set.add(6)
print("List after adding an element :")

# Removing an element from set.

my_set.remove(2)
print("Set after Removing an element :",my_set)

# Modifying an element in the set.

my_set.discard(1)
my_set.add(10)
print("Set after modifying an element :",my_set)