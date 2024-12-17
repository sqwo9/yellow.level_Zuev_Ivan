class Solution:
    def lengthOfLongestSubstring(self, s):
        q = [0]
        for i in range(len(s)):
            a = []
            for j in s[i::]:
                if j not in a:
                    a.append(j)
                else:
                    break
            q.append(len(a))
        return max(q)
print(Solution().lengthOfLongestSubstring('qwertyyyy'))