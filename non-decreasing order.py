nums = list(map(int, input("Enter the sorted array elements separated by spaces: ").split()))
target = int(input("Enter the target value: "))
result = [-1, -1]
left = 0
right = len(nums) - 1
while left <= right:
    mid = (left + right) // 2
    if nums[mid] >= target:
        right = mid - 1
    else:
        left = mid + 1
if left < len(nums) and nums[left] == target:
    result[0] = left
left = 0
right = len(nums) - 1
while left <= right:
    mid = (left + right) // 2
    if nums[mid] <= target:
        left = mid + 1
    else:
        right = mid - 1
if right >= 0 and nums[right] == target:
    result[1] = right
print(result)