class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1

        def if_alnum(s):
            return ('A' <= s <= 'Z') or ('a' <= s <= 'z') or ('0' <= s <= '9')

        while i < j:
            while not if_alnum(s[i].lower()) and i < j:
                i += 1
            while not if_alnum(s[j].lower()) and i < j:
                j -= 1
            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1

        return True
        