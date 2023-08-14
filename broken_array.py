# ID 87821420

def broken_search(nums: list, target: int) -> int:
    left = 0
    right = len(nums) - 1
    if nums[left] == target:
        return left
    while left <= right:
        middle = (left + right) // 2
        if is_target(nums, middle, left, right, target):
            return is_target(nums, middle, left, right, target)
        if nums[left] <= nums[middle]:
            if nums[left] <= target < nums[middle]:
                right = middle - 1
            else:
                left = middle + 1
        else:
            if nums[middle] < target <= nums[right]:
                left = middle + 1
            else:
                right = middle - 1
    return -1


def is_target(nums, middle, left, right, target):
    if nums[left] == target:
        return left
    if nums[middle] == target:
        return middle
    if nums[right] == target:
        return right
    return False
