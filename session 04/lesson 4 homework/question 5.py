def selection_sort(list):
    b = []
    while(len(list) > 0):
        b.append(min(list))
        list.remove(min(list))
    return b

print(selection_sort([4,8,1,3,2,9,5,7,6]))
