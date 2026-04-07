class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if not nums:
            return False

        nums.sort()

        potential_duplicate = nums[0]
        for num in nums[1:]:
            if num == potential_duplicate:
                return True
            potential_duplicate = num

        return False