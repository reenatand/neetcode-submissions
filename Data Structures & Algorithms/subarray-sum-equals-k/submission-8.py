class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sums = {0: 1}
        count = 0
        current_sum = 0
        for num in nums:
            current_sum += num
            target= current_sum - k
            if target in prefix_sums:
                count += prefix_sums[target]
            prefix_sums[current_sum] = prefix_sums.get(current_sum, 0) + 1
            
        return count

            