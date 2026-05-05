class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #Step 1: Count
        nums_counts = {}

        for num in nums:
            if num in nums_counts:
                nums_counts[num] += 1
            else:
                nums_counts[num] = 1
        
        #Step 2: Sort
        nums_counts_sorted = sorted(nums_counts.items(), key=lambda x: x[1], reverse=True)
        result = [num_count[0] for num_count in nums_counts_sorted[:k]]

        #Step 3: Return
        return result