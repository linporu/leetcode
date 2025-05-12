from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """
        max_freq_count = 頻率等於 freq_max 的任務數量
        interval = max(len(tasks), (freq_max - 1) * (n + 1) + max_freq_count)

        ## 解釋
        (freq_max - 1) * (n + 1) 代表安排除了最後一組外所有的最高頻率任務，並確保它們之間有 n 個間隔
        + max_freq_count 代表最後一組所有最高頻率的任務
        max(len(tasks), ...) 確保結果不小於任務總數

        ## 應用到例子
        例子 1：tasks = ["A","A","A","B","B","B"], n = 2

        最高頻率 freq_max = 3 (A 和 B 都出現 3 次)
        頻率為 3 的任務有 2 個 (max_freq_count = 2)
        計算：max(6, (3-1)*(2+1) + 2) = max(6, 8) = 8

        例子 2：tasks = ["A","C","A","B","D","B"], n = 1

        最高頻率 freq_max = 2 (A 和 B 都出現 2 次)
        頻率為 2 的任務有 2 個 (max_freq_count = 2)
        計算：max(6, (2-1)*(1+1) + 2) = max(6, 4) = 6

        例子 3：tasks = ["A","A","A","B","B","B"], n = 3

        最高頻率 freq_max = 3 (A 和 B 都出現 3 次)
        頻率為 3 的任務有 2 個 (max_freq_count = 2)
        計算：max(6, (3-1)*(3+1) + 2) = max(6, 10) = 10
        """
        # 計算任務頻率
        task_freq = {}
        for task in tasks:
            task_freq[task] = task_freq.get(task, 0) + 1

        # 找出最高頻率和擁有最高頻率的任務數量
        freq_max = max(task_freq.values())
        max_freq_count = list(task_freq.values()).count(freq_max)

        # 應用公式
        return max(len(tasks), (freq_max - 1) * (n + 1) + max_freq_count)
