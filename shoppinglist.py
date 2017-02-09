# # create shopping list

# 11 create a shopping list{}
# 2. sort(shopping_list)
# 3. remove duplicate items in shopping_list
# 4. nickname case sensitive
# 5. 




shopping_list = {'target':['socks','soap','detergent','sponges'],
'bi-bite':['butter','cake','cookies','bread']}

shopping_list['Yenny'] = []

shopping_list['Yenny'].append('milk')

# shopping_list['Yenny'].append(raw_input('What you want? '))



    

# shopping_list['Yenny'].remove(raw_input('What do you want to remove? '))

del shopping_list['Yenny']


print shopping_list

print "Show Target list ", shopping_list['target']

print type(shopping_list)

print shopping_list['target']


def add_shopping_list():
    print shopping_list
    add_list = raw_input('What is your new shopping list? ')
    if add_list not in shopping_list:
        shopping_list[add_list] = []
        print add_list
    print shopping_list

def add_item(add_item_list):
    add_item = raw_input("What a new item in your list? ")
    print add_item
    print shopping_list[add_item_list]
    shopping_list[add_item_list].append(add_item)
    print shopping_list




def print_direction():
    print '0 - Main Menu'
    print '1 - Show all lists.'
    print '2 - Show a specific list.'
    print '3 - Add a new shopping list.'
    print '4 - Add an item to a shopping list.'
    print '5 - Remove an item from a shopping list.'
    print '6 - Remove a list by nickname.'
    print '7 - Exit when you are done.'

def main():
    user_list = int(raw_input('What options you want? 0-7 and 7 is exit '))
    print user_list
    print type(user_list)
    while (True):
        if user_list == 7:
            break
        elif user_list == 0:
            print print_direction
        elif user_list == 1:
            print shopping_list
        elif user_list == 2:
            print shopping_list[raw_input('what list you want to see? ').lower()]
        elif user_list == 3:
            add_shopping_list()
        elif user_list == 4:
            add_item_list = raw_input('What is the list you want to add item? ')
                while add_item_list != 'q':
                    print shopping_list[add_item_list]
                    add_item(add_item_list)







if __name__ == '__main__':
    main()
