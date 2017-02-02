items = []
while (True):
    print "If you are done with shopping list, type q to exit "
    item = raw_input("add an item: ")
    if(item == 'q'):
        break
    else:
        items.append(item)
print "Your items are ", items
