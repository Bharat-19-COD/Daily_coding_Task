class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        result = []
        for num in nums:
            result.append(num)  # Add each element from nums
        for num in nums:
            result.append(num)  # Add each element again
        return result
     
#   Explaination: 
# The method getConcatenation takes a list of integers (nums).
# It creates an empty list result.
# It then iterates over nums twice and appends each element to result during each iteration. This effectively "duplicates" the original list, 
# meaning the final result contains two copies of nums concatenated together.
# Finally, it returns the concatenated 
