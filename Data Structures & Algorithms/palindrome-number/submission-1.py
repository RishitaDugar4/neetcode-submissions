class Solution:
    def isPalindrome(self, x: int) -> bool:
        stringX = str(x)
        return stringX == stringX[::-1]

