#Original data
ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello": "titi!"}

#Modifying the entry directly
ft_list[1] = "World!"

#Changing tuple to a list and then to a tuple, because tuples are immutable
list_tuple = list(ft_tuple)
list_tuple[1] = "France!"
ft_tuple = list_tuple

#using set functions
ft_set.discard("tutu!")
ft_set.add("Paris!")

#modifying the value of the key Hello for the dictionary
ft_dict["Hello"] = "42Paris!"

#Printing modified data
print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
