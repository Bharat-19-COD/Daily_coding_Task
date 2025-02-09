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

## Read the input tag
tag = input().strip()

# Check if the input is exactly 9 characters 
if len(tag) != 9:
    print("invalid")
else:
    # Define vowels
    vowels = {'A', 'E', 'I', 'O', 'U', 'Y'}

    # Check if the character at position 3 is a vowel
    if tag[2] in vowels:
        print("invalid")
    else:
        # Check if the sum of every two consecutive digits is even
        for i in range(8):
            if (int(tag[i]) + int(tag[i + 1])) % 2 != 0:
                print("invalid")
                break
        else:
            print("valid")
