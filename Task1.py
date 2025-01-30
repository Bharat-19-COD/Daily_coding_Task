import os

def reverseArray(a):
    # Reverse the array using slicing and return the result
    return a[::-1]

if __name__ == '__main__':
    # Open the file where output needs to be written
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # Read the input count (not really used, but it's part of the input format)
    arr_count = int(input().strip())

    # Read the list of integers
    arr = list(map(int, input().rstrip().split()))

    # Get the reversed array
    res = reverseArray(arr)

    # Write the result to the output file
    fptr.write(' '.join(map(str, res)))
    fptr.write('\n')

    # Close the file
    fptr.close()

