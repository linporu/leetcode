from typing import List


# Brutal
class Solution01:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        count = 0
        curr_g = 0
        curr_s = 0

        for _ in g:
            for _ in s:
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


# Optimized two pointer approach
class Solution02:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        num_children = len(g)
        num_cookies = len(s)
        count = 0
        idx_child = 0
        idx_cookie = 0

        while idx_cookie < num_cookies and idx_child < num_children:
            if g[idx_child] <= s[idx_cookie]:
                idx_child += 1
                idx_cookie += 1
                count += 1
            else:
                idx_cookie += 1

        return count
