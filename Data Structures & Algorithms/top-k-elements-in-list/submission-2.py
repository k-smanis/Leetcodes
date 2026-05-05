class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #1. Count Frequencies
        nums_counts = {}
        for num in nums:
            nums_counts[num] = nums_counts.get(num, 0) + 1
        
        
        #2. Build Frequency Buckets (index = count = frequency)
        frequency_buckets = [[] for _ in range(len(nums) + 1)]
        for num, count in nums_counts.items():
            frequency_buckets[count].append(num)

        
        #3. Collect Top K Elements (iterate over buckets)
        results = []
        remaining_elements = k
        for top_bucket in range( len(frequency_buckets)-1, 0, -1):
            while (remaining_elements > 0) and (frequency_buckets[top_bucket]):
                top_k_element = frequency_buckets[top_bucket].pop()
                results.append(top_k_element)
                remaining_elements -= 1
        
        #4. Return
        return results
        