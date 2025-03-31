
def bubbleSort(arr):
    sorted = False
    while sorted == False:
        sorted = True
        for num in range(0, len(arr) - 2):
            if arr[num] > arr[num + 1]:
                [arr[num], arr[num + 1]] = [arr[num + 1], arr[num]]
                sorted = False

    return arr
