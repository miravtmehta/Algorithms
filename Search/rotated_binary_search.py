def rotated_binary_search(data, target):
    left = 0
    right = len(data) - 1
    while left <= right:
        middle = (left + right) // 2
        if data[middle] == target:
            return middle

        elif data[middle] > target and data[middle + 1] <= target <= data[right]:
            left = left + 1
        else:
            right = right - 1

    return -1


data = [4, 5, 6, 7, 0, 1, 2]
target = 6
print(rotated_binary_search(data, target))
