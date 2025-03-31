
def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = mergeSort(arr[:mid])
        right = mergeSort(arr[mid:])

        return merge(left, right)
    else:
        return arr

def merge(left, right = []):
    result = []
    while len(left) > 0 and len(right) > 0:
        if left[0] < right[0]:
            result.append(left[0])
            left.remove(left[0])
        else:
            result.append(right[0])
            right.remove(right[0])

    for num in left:
        result.append(num)

    for num in right:
        result.append(num)

    return result




