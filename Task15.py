<<<<<<< HEAD
import math
n = int(input())
count = 0
for j in range(2, 1000000):
    i = str(j)
    if '1' not in i and '0' not in i and (n == math.prod([int(x) for x in i])):
        count += 1
print(count)
=======
# 08-02-2025
def count_supernatural_numbers(n):
    valid_digits = [2, 3, 4, 5, 6, 7, 8, 9]
    count = 0
    def find_factors(n, start):
        nonlocal count
        if n == 1:
            count += 1
            return
        for i in range(start, len(valid_digits)):
            if n % valid_digits[i] == 0:
                find_factors(n // valid_digits[i], i)
  find_factors(n, 0)
    return count
n = int(input())
print(count_supernatural_numbers(n))
 Explaination:
Summary:
The code uses recursion to explore all combinations of valid digits whose product equals n.
It avoids 1 and 0 as digits and ensures each combination is counted only once.
The recursive approach helps systematically find all valid combinations without duplicates.
>>>>>>> b856a1a4ce759d13bfed0046c29716b922ee1ba6
