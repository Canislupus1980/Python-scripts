#Binary Search
def binarysearch(mylist, search, start, stop):
    if start > stop:
        return False
    else:
        mid = (start + stop) // 2
        if search == mylist[mid]:
            return mid
        elif search < mylist[mid]:
            return binarysearch(mylist, search, start, mid - 1)
        else:
            return binarysearch(mylist, search, mid +1, stop)

mylist = [10, 12, 13, 15, 20, 24, 27, 33, 42, 51, 57, 68, 70, 77, 79, 81]
search = 70
start = 0
stop = len(mylist)

x= binarysearch(mylist, search, start, stop)

if x == False:
    print("Item ", search, "Not Found!")
else:
    print("Item ", search, "Found at Index ", x)
