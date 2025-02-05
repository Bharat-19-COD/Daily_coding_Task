T = int(input())  # Number of test cases

for t in range(T):
    N = int(input())  # Number of moves for this test case
    # The number of distinct reachable positions is 2 * N + 1
    print(N* N + 1)
    
#  Explanation :
# Initial position (0,0)
# case1: when X in increasing direction
# N =1+2+3+4+5......=n(n+1)/2
# case2: when X in decreasing direction
# N =-1-2-3-4-5......=|-n(n+1)/2|
# case3:remains constant
# T=n(n+1)/2+|-n(n+1)/2|+0=N*(N+1)

