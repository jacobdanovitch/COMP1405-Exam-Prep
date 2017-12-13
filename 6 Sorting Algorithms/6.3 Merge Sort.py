#https://www.khanacademy.org/computing/computer-science/algorithms/merge-sort/a/overview-of-merge-sort
def merge(left, right):
    sorted_list = []
    while True:
        if len(left) == 0:
            return sorted_list + right
        elif len(right) == 0:
            return sorted_list + left

        if left[0] > right[0]:
            sorted_list.append(right.pop(0))
        else:
            sorted_list.append(left.pop(0))


def mergesort(lst):
    if len(lst) == 1:
        return lst
    else:
        midpoint = len(lst) // 2
        left = lst[:midpoint]
        right = lst[midpoint:]
        sorted_left = mergesort(left)
        sorted_right = mergesort(right)
        return merge(sorted_left, sorted_right)


#print(merge([1,4,9,12,16],[2,3,5,6,8,10]))
print(mergesort([2,1,4,6,3,10,8,27,25,16,22,19]))