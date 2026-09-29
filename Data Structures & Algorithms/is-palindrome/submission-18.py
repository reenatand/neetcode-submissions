class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ''
        for c in s:
            if c.isalnum():
                newStr += c.lower()
        right = len(newStr)-1
        left = 0
        while left<right:
            if newStr[right] == newStr[left]:
                left += 1
                right -= 1
            else:
                return False
        return True 