def reverse_list(items):
    last_item = len(items)-1
    first_item = 0
    while first_item < last_item:
        items[first_item],items[last_item] = items[last_item],items[first_item]
        first_item+=1
        last_item-=1
    return items

items = [1, 2, 3, 4]
print(reverse_list(items))

    