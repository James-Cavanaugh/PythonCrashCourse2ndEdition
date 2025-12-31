import random
import math

nums_sum = 0
nums_min = math.inf
nums_max = -math.inf
nums_squares = []
nums = [random.randint(1, 50) for _ in range(5)]
for num in nums:
    if num < nums_min:
        nums_min = num
    if num > nums_max:
        nums_max = num
    nums_sum += num
    nums_squares.append(num**2)

print(f"Original List: {nums}")
print(f"Sum: {nums_sum}")
print(f"Average: {nums_sum/len(nums)}")
print(f"Minimum: {nums_min}")
print(f"Maximum: {nums_max}")
print(f"Squares: {nums_squares}")