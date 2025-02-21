# 21-02-2025
class Solution:
    def intersection(self, nums1, nums2):
        set1 = set(nums1)
        set2 = set(nums2)
        return list(set1 & set2)
solution = Solution()
nums1 = [4, 9, 5]
nums2 = [9, 4, 9, 8, 4]
result = solution.intersection(nums1, nums2)
print(result)  
