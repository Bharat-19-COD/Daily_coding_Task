# 05-02-2025
def is_mathematically_beautiful(x, k):
    while x:
        if x % k > 1: 
            return "NO"
        x //= k
    return "YES"

T = int(input())
for _ in range(T):
    x, k = map(int, input().split())
    print(is_mathematically_beautiful(x, k))

Explanation :
Convert x to base k.
If the base k representation of x contains only 0s and 1s, print "YES".
Otherwise, print "NO".
