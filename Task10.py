import math
# Read the number of test cases
T = int(input().strip())
# Process each test case
for _ in range(T):
    N,M,K = map(int, input().split())  # Read values
    rooms_boys = math.ceil(N / K)  # Rooms needed for boys
    rooms_girls = math.ceil(M /K)  # Rooms needed for girls
    print(rooms_boys + rooms_girls)  # Total rooms
# Explanation:
# The code first reads the number of test cases (T), then for each test case, it reads the number of boys (N), girls (M), and room capacity (K), 
# and calculates the total number of rooms by dividing the number of students by the room capacity and rounding up using math.ceil()
# to account for any remaining students.

