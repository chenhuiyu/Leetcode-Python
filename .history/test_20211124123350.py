nums = [5, 1, 4, 2, 3]
left = 0
right = len(nums) - 1
L = left - 1
R = right
target = nums[right]
i = left
while i < R:
    if nums[i] == target:
        i += 1
    elif nums[i] > target:
        nums[i], nums[R - 1] = nums[R - 1], nums[i]
        R -= 1
    else:
        nums[i], nums[L + 1] = nums[L + 1], nums[i]
        L += 1
        i += 1
nums[right], nums[R] = nums[R], nums[right]