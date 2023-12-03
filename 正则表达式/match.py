class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s == s[::-1]:
            print(s)
        else:
            L = len(s)
            step = L // 2
            NewString1 = ''
            NewString2 = ''
            n = 1
            while n <= step:
                NewString1 = s + s[0:n + 1]
                NewString2 = s[::-1] + s
                if NewString1 == NewString1[::-1]:
                    return NewString1
                elif NewString2 == NewString2[::-1]:
                    return NewString2
                else:
                    n += 1
            return s[::-1] + s

solution = Solution()
s = 'ab'
print(solution.shortestPalindrome(s))
