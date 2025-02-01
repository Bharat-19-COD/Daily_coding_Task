## Read the input tag
tag = input().strip()

# Check if the input is exactly 9 characters long
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
