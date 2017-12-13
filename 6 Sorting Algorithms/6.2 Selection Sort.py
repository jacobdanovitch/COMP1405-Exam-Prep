#http://www.geeksforgeeks.org/selection-sort/
def selectionsort(unsorted):
    sorted_list = []
    while unsorted != []:
        min_index = 0
        min_num = unsorted[0]
        for i in range(len(unsorted)):
            if unsorted[i] < min_num:
                min_num = unsorted[i]
                min_index = i
        sorted_list.append(unsorted.pop(min_index))
    return sorted_list

print(selectionsort([2,1,4,6,3,10,8,27,25,16,22,19]))