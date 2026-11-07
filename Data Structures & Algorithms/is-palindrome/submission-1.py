class Solution:
    def isPalindrome(self, s: str) -> bool:
        letters_only = ''.join(filter(str.isalnum, s)).lower()

        return letters_only[::-1] == letters_only

        