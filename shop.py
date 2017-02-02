items = []


while (True):
    print ("If you are done with shopping list, type q to exit or type r to remove your list ")
    print ('My list', sorted(items))
    item = input("add an item: ")
    if(item == 'q'):
        break
    elif (item in items): 
        items.remove(item)
    else:
        items.append(item)






