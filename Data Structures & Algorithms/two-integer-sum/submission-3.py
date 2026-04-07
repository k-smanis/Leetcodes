class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #Case 1: Trivial Array
        if len(nums) == 2:
            return [0,1]

        #Case 2: Non Trivial Case
        complement_map = {}

        for i, num in enumerate(nums):
            if num in complement_map:
                return [
                    min(i, complement_map[num]),
                    max(i, complement_map[num]),
                ]

            desired_complement = target - num
            complement_map[desired_complement] = i