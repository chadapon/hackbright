#shopping list
input_str = raw_input("what is your shopping list? ").lower()

#input_up = input_str.upper()
print input_str.lower()
#input_list = input_str.split(',')

remove_str = raw_input("what you want to remove? ")

def shopping_list():
    shop_list = ['oil']
    if shop_list[0] in input_str:
        print "yes, in the list"
    else:
        print "no, it is not in the list"
        shop_list.append(input_str)
        shop_list.sort()
    return shop_list


print shopping_list()

def remove_list():
    remove_list[0] in shop_list: