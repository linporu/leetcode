class Solution:
    def romanToInt(self, s: str) -> int:
        value = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        sum = value[s[-1]]  # 先加入最後一個數字

        for i in range(len(s) - 2, -1, -1):  # 從倒數第二個開始往前
            curr = value[s[i]]
            prev = value[s[i + 1]]
            if curr >= prev:
                sum += curr
            else:
                sum -= curr

        return sum
