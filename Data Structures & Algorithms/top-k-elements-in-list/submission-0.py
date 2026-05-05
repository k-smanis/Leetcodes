class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #Dependency
        from collections import Counter

        #Step 1: Count Element Instances
        nums_counts = Counter(nums)

        #Step 2: Pick Top-K Elements
        result = [num for num, _ in nums_counts.most_common(k)]

        #Step 3: Return
        return result