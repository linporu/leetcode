class Solution01:
    def isAnagram(self, s: str, t: str) -> bool:
        if not len(s) == len(t):
            return False

        hash = {}
        for char in s:
            if char in hash:
                hash[char] += 1
            else:
                hash[char] = 1

        for char in t:
            if char not in hash:
                return False
            else:
                if hash[char] == 0:
                    return False
                hash[char] -= 1

        return True


class Solution02:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        使用 zip() 和 dict.get() 實現字符統計。

        zip() 函數:
        - 將兩個可迭代對象打包成一個元組的迭代器
        - 例如: zip('ab', 'cd') 產生 [('a','c'), ('b','d')]
        - 可以同時遍歷兩個字串，減少迴圈次數

        dict.get() 方法:
        - get(key, default) 在鍵不存在時返回默認值
        - 避免了額外的 if-else 判斷
        """
        if len(s) != len(t):
            return False

        char_count = {}
        # 一次遍歷完成計數
        for c1, c2 in zip(s, t):
            char_count[c1] = char_count.get(c1, 0) + 1
            char_count[c2] = char_count.get(c2, 0) - 1

        # 檢查所有計數是否為0
        return all(count == 0 for count in char_count.values())


class Solution03:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        使用 collections.Counter 實現字符統計。

        Counter 類:
        - Counter 是 dict 的子類，用於計數可哈希對象
        - Counter('hello') 返回 {'h': 1, 'e': 1, 'l': 2, 'o': 1}
        - Counter 對象可以直接比較是否相等
        - Counter 對象支持加減乘除等運算

        優點:
        - 代碼簡潔易讀
        - 自動處理計數邏輯
        - 效率高，是專門為計數優化的數據結構
        """
        from collections import Counter

        return len(s) == len(t) and Counter(s) == Counter(t)
