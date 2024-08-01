array = [10, 5, 3, 12, 7, 1, 8, 9]
M = 2  
N = 3 
sorted_array = sorted(array)
Mth_maximum = sorted_array[-M]
Nth_minimum = sorted_array[N-1]
sum_result = Mth_maximum + Nth_minimum
difference_result = Mth_maximum - Nth_minimum
product_result = Mth_maximum * Nth_minimum
print("Original array:", array)
print(f"{M}th maximum number:", Mth_maximum)
print(f"{N}th minimum number:", Nth_minimum)
print("Sum:", sum_result)
print("Difference:", difference_result)
print("Product:", product_result)