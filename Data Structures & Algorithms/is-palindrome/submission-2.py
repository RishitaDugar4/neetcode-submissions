class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ""
        for char in s:
            if char.isalnum():
                char = char.lower()
                newStr += char


        return newStr == newStr[::-1]