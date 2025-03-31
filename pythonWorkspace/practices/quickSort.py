
def quickSort(arr):
    if len(arr) > 1:
        pivot = arr[0]
        left = []
        right = []
        for n in arr[1:]:
            if n > pivot:
                right.append(n)
            else:
                left.append(n)
    else:
        return arr

    return quickSort(left) + [pivot] + quickSort(right)
