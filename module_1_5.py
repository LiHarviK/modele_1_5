immutable_var = 1, 2, 3, 4, 5, 6, 7, 8, 9
print(immutable_var)

# immutable_var [0] = 1337 потому что кортеж неизменяемыый тип

mutable_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(mutable_list)

mutable_list[0] = 888
print(mutable_list)

print(immutable_var.__sizeof__())
print(mutable_list.__sizeof__())