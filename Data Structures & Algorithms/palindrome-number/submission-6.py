class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x > 9 and x % 10 == 0):
            print('are you here')
            return False

        if -1 < x < 10:
            return True

        num = x
        reverse = 0
        while num > 0:
            reverse = (reverse * 10) + (num % 10)
            num = num // 10

        return x == reverse




