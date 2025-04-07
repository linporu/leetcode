from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:

        g.sort()
        s.sort()
        count = 0
        curr_g = 0
        curr_s = 0

        for i in g:
            for j in s:
                if curr_s == len(s):
                    break

                if g[curr_g] <= s[curr_s]:
                    count += 1
                    curr_g += 1
                    curr_s += 1
                    break
                else:
                    curr_s += 1

        return count
