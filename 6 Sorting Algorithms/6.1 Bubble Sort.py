#http://www.geeksforgeeks.org/bubble-sort/
def bubblesort(unsorted):
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


print(bubblesort([2,1,4,6,3,10,8,27,25,16,22,19]))