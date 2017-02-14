# grocery_string = "item:apples,quantity:4,price:1.50\n"

# split_data = grocery_string.split(',')

# quantity = int(split_data[1].split(':')[1])

# question 1
# my_name = 'mod'
# new_name = list(my_name)

# print new_name

#question2

# string = "1,2,3,4,5"



# new_string = string.split(',')
# print new_string
# #new_int = int(new_string[0].split(',')[0])

# new_list = []

# for number in new_string:
#     new_list.append(int(number))


# print new_list
# print type(new_list)


# print new_list[0]
# print type(new_list[0])

# question 3

# string2 = "One fish two fish red fish blue fish"

# replace_data2 = string2.replace(" fish","")
# print replace_data2

# split_data2 = replace_data2.split(' ')
# print split_data2

#question 5
grocery_list = ["item:apples,quantity:4,price:1.50\n",
"item:pears,quantity:5,price:2.00\n",
"item:cereal,quantity:1,price:4.49\n"]

#grocery_list = "item:apples,quantity:4,price:1.50\n"

total = 0



for thing in grocery_list:
    name = thing.split(',')
    list_q = name[1].split(':')
    quantity = int(list_q[1])
    list_p = name[2].split(':')
    price = float(list_p[1])
    total +=  quantity*price
print total




