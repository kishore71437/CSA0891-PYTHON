def search_range(nums, target):
    if not nums:
        return [-1, -1]
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] < target:A= 12
B=19
for num in range(A,B+1):

    if num<=1:
        print(num)
    continue
is_prime=True
for i in range (2,int(num*0.5)+1):
    if num%i==0:
        is_prime=False
    break
if not is_prime:
    print(num)
            left = mid + 1
        else:
            right = mid - 1
    left_index = left
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] <= target:
            left = mid + 1
        else:
            right = mid - 1
    right_index = right
    if left_index <= right_index and nums[left_index] == target:
        return [left_index, right_index]
    else:
        return [-1, -1]
nums = [5,7,7,8,8,10]
target = 8
print(search_range(nums, target))  

 
