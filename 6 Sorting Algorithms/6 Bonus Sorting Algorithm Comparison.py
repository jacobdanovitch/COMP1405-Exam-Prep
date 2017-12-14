from random import choice
from time import time
from matplotlib import pyplot as plt
plt.style.use('fivethirtyeight')

class Sort:
    def bubblesort(self, unsorted):
        while True:
            counter = 0
            for i in range(len(unsorted)-1):
                if unsorted[i] > unsorted[i+1]:
                    big = unsorted[i]
                    small = unsorted[i+1]

                    unsorted[i+1] = big
                    unsorted[i] = small

                    counter += 1
            if counter == 0:
                return unsorted

    def selectionsort(self, unsorted):
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

    def merge(self, left, right):
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

    def mergesort(self, lst):
        if len(lst) == 1:
            return lst
        else:
            midpoint = len(lst) // 2
            left = lst[:midpoint]
            right = lst[midpoint:]
            sorted_left = self.mergesort(left)
            sorted_right = self.mergesort(right)
            return self.merge(sorted_left, sorted_right)

    def insertionsort(self, lst):
        for i in range(len(lst)):
            index = 0
            for j in range(len(lst[:i])):
                if lst[i] < lst[j]:
                    lst.insert(j, lst.pop(i))
                    break
        return lst


sort = Sort()
runtimes = []
x = range(2,101)

funcs = {
    "bubble" : sort.bubblesort,
    "selection" : sort.selectionsort,
    "merge" : sort.mergesort,
    "insertion" : sort.insertionsort
}

for i in x:
    for func in funcs:
        elapsed = 0
        trials = 100
        for trial in range(trials):
            start = time()
            funcs[func]([choice(range(100)) for _ in range(i)])
            elapsed += time()-start
        avg = elapsed / trials
        runtimes.append([func,(i,avg)])

bubblerun = [i[1][1] for i in runtimes if i[0] == 'bubble']
selectionrun = [i[1][1] for i in runtimes if i[0] == 'selection']
mergerun = [i[1][1] for i in runtimes if i[0] == 'merge']
insertionrun = [i[1][1] for i in runtimes if i[0] == 'insertion']

plt.plot(x, bubblerun, label='Bubble')
plt.plot(x, selectionrun, label='Selection')
plt.plot(x, mergerun, label='Merge')
plt.plot(x, insertionrun, label='Insertion')
plt.legend()
plt.show()


