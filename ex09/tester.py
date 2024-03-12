from ft_package.count import count_in_list

# Use the function
print(count_in_list([1, 2, 3, 2, 2, 4], 2))  # output 3
print(count_in_list(["toto", "tata", "toto"], "toto"))  # output: 2
print(count_in_list(["toto", "tata", "toto"], "tutu"))  # output: 0
