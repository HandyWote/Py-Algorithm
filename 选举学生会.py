def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)

n, m = map(int, input().split())
c = [int(i) for i in input().split()]
sorted_c = quicksort(c)
print(' '.join([str(i) for i in sorted_c]))