class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set() 
        for i, num in enumerate(nums):
            # If our window has grown larger than k, remove the oldest element
            if i > k:
                window.remove(nums[i - k - 1]) 
            # If the current number is already in our window, we found a match!
            if num in window:
                return True
            window.add(num)
            
        return False
