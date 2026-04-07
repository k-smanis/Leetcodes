class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        discovered_values = []

        for num in nums:
            if num in discovered_values:
                return True
            else:
                discovered_values.append(num)
        
        return False
