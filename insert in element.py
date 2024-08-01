nums = list(map(int, input("Enter the elements of the list: ").split()))
element = int(input("Enter the element to insert: "))
index = int(input("Enter the index at which to insert the element: "))
if 0 <= index <= len(nums):
    nums.insert(index, element)
else:
  print("Index out of bounds.")
  print("Modified list:", nums)