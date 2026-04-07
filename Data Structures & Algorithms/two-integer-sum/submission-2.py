class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #Case 1: Trivial Array
        if len(nums) == 2:
            return [0,1]

        #Case 2: Non Trivial Case
        indexed_nums = [(num, i) for i,num in enumerate(nums)]
        sorted_indexed_nums = sorted(indexed_nums, key=lambda item: item[0])
        
        l = 0
        r = len(nums) - 1

        while l <= r:
            left_num = sorted_indexed_nums[l][0]
            left_num_index = sorted_indexed_nums[l][1]
            right_num = sorted_indexed_nums[r][0]
            right_num_index = sorted_indexed_nums[r][1]
            sum_under_test = left_num + right_num
            
            if sum_under_test == target:
                return [
                    min(left_num_index, right_num_index),
                    max(left_num_index, right_num_index)
                ]
            elif sum_under_test < target:
                l += 1
            elif sum_under_test > target:
                r -= 1