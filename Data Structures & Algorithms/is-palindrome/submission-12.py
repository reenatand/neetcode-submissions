class Solution:
    def isPalindrome(self, s: str) -> bool:
        Palindromeoutput = True
        clean_s = ""
        for char in s:
            if char.isalnum():
                clean_s += char
        clean_s = clean_s.lower()
        n = len(clean_s)
        for i in range(0,n // 2):
            if clean_s[i] != clean_s[(n-i-1)]:
                    Palindromeoutput = False
        return Palindromeoutput 
