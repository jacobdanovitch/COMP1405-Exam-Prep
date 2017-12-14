def insertionsort(lst):
    for i in range(len(lst)):
        index = 0
        for j in range(len(lst[:i])):
            if lst[i] < lst[j]:
                lst.insert(j, lst.pop(i))
                break
    return lst

print(insertionsort([1,3,2,6,12,8]))