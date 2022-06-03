old_list = [10, 76, 43, 15, 25, -4, 0, 99]


def bubble_sort(mylist):
    last_item = len(mylist) - 1
    for y in range(0, last_item):
        for x in range(0, last_item-y):
          # print(mylist)
            if mylist[x] > mylist[x+1]:
                mylist[x], mylist[x+1] = mylist[x+1], mylist[x]
    return mylist


new_list = bubble_sort(old_list).copy()
print("Old list ", old_list)
print("New list ", new_list)