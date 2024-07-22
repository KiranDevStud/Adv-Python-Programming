#Write a python program to sort the elements of a dictionary based on a key and value 



my_dict = {'apple': 5, 'banana': 2, 'orange': 4, 'kiwi': 3}

#based on keys
sorted_dict_keys = dict(sorted(my_dict.items(), key=lambda x: x[0]))

#based on values
sorted_dict_values = dict(sorted(my_dict.items(), key=lambda x: x[1]))

print("Sorted dictionary based on keys:", sorted_dict_keys)
print("Sorted dictionary based on values:", sorted_dict_values)
