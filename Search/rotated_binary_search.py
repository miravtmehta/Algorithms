def rotated_binary_search(nums, target):
    left = 0
    right = len(nums) - 1
    while left <= right:
        middle = (left + right) // 2
        if nums[middle] == target:
            return middle
        if nums[right] >= nums[middle]:
            if nums[middle] <= target <= nums[right]:
                left = middle + 1
            else:
                right = middle - 1
        if nums[middle] >= nums[left]:
            if nums[left] <= target <= nums[middle]:
                right = middle - 1
            else:
                left = left + 1
    return -1


data = [4, 5, 6, 7, 0, 1, 2]
target = 1
print(rotated_binary_search(data, target))
