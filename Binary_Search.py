mylist = [10, 12, 13, 15, 20, 24, 28, 32, 41, 57, 69, 77, 78, 88, 91, 100]


def binary_search(mylist, search, start, stop):
    if start > stop:
        return False
    else:
        mid = (start + stop) // 2
        if search == mylist[mid]:
            return mid
        elif search < mylist[mid]:
            return binary_search(mylist, search, start, mid - 1)
        else:
            return binary_search(mylist, search, mid + 1, stop)


search = 32
start = 0
stop = len(mylist)
x = binary_search(mylist, search, 0, len(mylist))

if not x:
    print("Item", search, "Not Found")
else:
    print("Item ", search, "Found an index ", x)
