my_list = [None,1,'F',{}]
# for item in my_list:
#     print(item)

# print('-------------------------')

my_list_iter = iter(my_list)
item = next(my_list_iter)
print(item)
item = next(my_list_iter)
print(item)