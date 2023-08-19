# for i in range(5, -1, -1):
#     print('iiii: ', i)


def sort(arr):
    for i in range(1, len(arr)):
        pIndex, pValue = i, arr[i]
        for j in range(i-1, -1, -1):
            if pValue < arr[j]:
                arr[j+1] = arr[j]
                pIndex = j
            else:
                break
        arr[pIndex] = pValue
    return arr


given = [5, 7, 8, 1, 4, 6, 9]
expected = [1, 4, 5, 6, 7, 8, 9]
output = sort(given)
print(output)
