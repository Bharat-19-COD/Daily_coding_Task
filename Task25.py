class Solution:
    def intersection(self, nums1, nums2):
        # Convert both arrays to sets
        set1 = set(nums1)
        set2 = set(nums2)
        
        # Return the intersection of both sets
        return list(set1 & set2)

# Create an instance of Solution class
solution = Solution()

# Test cases
nums1 = [4, 9, 5]
nums2 = [9, 4, 9, 8, 4]

# Get the intersection
result = solution.intersection(nums1, nums2)

# Print the result
print(result)  # Output: [9, 4]
