# 06-02-2025

t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    have = {}
    a = list(map(int, input().split()))
    for i in range(n):
        if a[i] not in have:
            have[a[i]] = []
        have[a[i]] += [i]
    ans = 0
    for key, occ in have.items():
        ans += occ[-1] - occ[0]
    print(ans)

# Explanation:
# Read the number of test cases and for each test case, read the array.
# Use a dictionary to store the first and last index of each element.
# For each unique element, compute the absolute difference between the first and last occurrence, sum them, and print the result.
  
