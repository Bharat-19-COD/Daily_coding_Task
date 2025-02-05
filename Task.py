T = int(input())  # Number of test cases

for t in range(T):
    N = int(input())  # Number of moves for this test case
    # The number of distinct reachable positions is 2 * N + 1
    print(2 * N + 1)
