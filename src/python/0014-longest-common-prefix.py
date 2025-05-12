from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """找出字串陣列中所有字串的最長共同前綴。

        關鍵：「共同前綴」必然出現在所有字串中，所以只要有一個字不符合，比對就結束了。

        解題思路：
        1. 以第一個字串為基準，逐字元檢查其他所有字串相同位置是否相同
        2. 如果發現任何字串在該位置的字元不同，或已達到某字串末尾，則返回目前的共同前綴
        3. 如果所有字串在該位置都相同，則將該字元加入結果中

        時間複雜度：O(S)，其中 S 是所有字串中的字元總數
        空間複雜度：O(1)，只需要存儲結果字串

        Args:
            strs: 字串陣列

        Returns:
            str: 最長共同前綴

        Examples:
            >>> strs = ["flower", "flow", "flight"]
            >>> longestCommonPrefix(strs)
            "fl"

            >>> strs = ["dog", "racecar", "car"]
            >>> longestCommonPrefix(strs)
            ""
        """
        # []
        if not strs:
            return ""

        first = strs[0]
        answer = ""

        for i in range(len(first)):
            for string in strs[1:]:
                if i >= len(string) or string[i] != first[i]:
                    return answer
            answer += first[i]

        return answer
