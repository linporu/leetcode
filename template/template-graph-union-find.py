"""
圖論並查集模板 (Graph Union Find Template)

本模板包含：
1. 基本並查集實現
2. 帶路徑壓縮的並查集
3. 帶按秩合併的並查集
4. 帶路徑壓縮和按秩合併的並查集
5. 並查集的應用（環檢測、最小生成樹等）

適用於：
- 需要處理圖的連通性
- 需要合併集合
- 需要檢測環
- 需要處理動態連通性問題

實作重點：
- 路徑壓縮
- 按秩合併
- 集合的維護
- 效率優化
"""

from typing import List, Tuple
from collections import defaultdict


class BasicUnionFind:
    """
    基本並查集實現
    """

    def __init__(self, n: int):
        """
        初始化並查集

        Args:
            n: 元素數量（元素編號從 0 到 n-1）
        """
        self.parent = list(range(n))  # 每個元素的父節點
        self.count = n  # 連通分量數量

    def find(self, x: int) -> int:
        """
        查找元素 x 所屬的集合（尋找 x 的根節點）

        Args:
            x: 要查找的元素

        Returns:
            int: x 的根節點
        """
        while x != self.parent[x]:
            x = self.parent[x]
        return x

    def union(self, x: int, y: int) -> bool:
        """
        合併元素 x 和 y 所屬的集合

        Args:
            x: 第一個元素
            y: 第二個元素

        Returns:
            bool: 如果 x 和 y 原本不在同一個集合則返回 True，否則返回 False
        """
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return False

        self.parent[root_x] = root_y
        self.count -= 1
        return True

    def is_connected(self, x: int, y: int) -> bool:
        """
        檢查元素 x 和 y 是否在同一個集合中

        Args:
            x: 第一個元素
            y: 第二個元素

        Returns:
            bool: 如果 x 和 y 在同一個集合中則返回 True，否則返回 False
        """
        return self.find(x) == self.find(y)

    def get_count(self) -> int:
        """
        獲取連通分量數量

        Returns:
            int: 連通分量數量
        """
        return self.count


class PathCompressionUnionFind:
    """
    帶路徑壓縮的並查集

    路徑壓縮優化：在查找過程中，將路徑上的所有節點直接連接到根節點，
    從而減少後續查找的時間複雜度
    """

    def __init__(self, n: int):
        """
        初始化並查集

        Args:
            n: 元素數量（元素編號從 0 到 n-1）
        """
        self.parent = list(range(n))  # 每個元素的父節點
        self.count = n  # 連通分量數量

    def find(self, x: int) -> int:
        """
        查找元素 x 所屬的集合（尋找 x 的根節點），使用路徑壓縮

        Args:
            x: 要查找的元素

        Returns:
            int: x 的根節點
        """
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y: int) -> bool:
        """
        合併元素 x 和 y 所屬的集合

        Args:
            x: 第一個元素
            y: 第二個元素

        Returns:
            bool: 如果 x 和 y 原本不在同一個集合則返回 True，否則返回 False
        """
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return False

        self.parent[root_x] = root_y
        self.count -= 1
        return True

    def is_connected(self, x: int, y: int) -> bool:
        """
        檢查元素 x 和 y 是否在同一個集合中

        Args:
            x: 第一個元素
            y: 第二個元素

        Returns:
            bool: 如果 x 和 y 在同一個集合中則返回 True，否則返回 False
        """
        return self.find(x) == self.find(y)

    def get_count(self) -> int:
        """
        獲取連通分量數量

        Returns:
            int: 連通分量數量
        """
        return self.count


class RankUnionFind:
    """
    帶按秩合併的並查集

    按秩合併優化：在合併兩個集合時，將較小的集合（秩較小的樹）連接到較大的集合（秩較大的樹）上，
    從而減少樹的高度，提高查找效率
    """

    def __init__(self, n: int):
        """
        初始化並查集

        Args:
            n: 元素數量（元素編號從 0 到 n-1）
        """
        self.parent = list(range(n))  # 每個元素的父節點
        self.rank = [0] * n  # 每個元素的秩（樹的高度）
        self.count = n  # 連通分量數量

    def find(self, x: int) -> int:
        """
        查找元素 x 所屬的集合（尋找 x 的根節點）

        Args:
            x: 要查找的元素

        Returns:
            int: x 的根節點
        """
        while x != self.parent[x]:
            x = self.parent[x]
        return x

    def union(self, x: int, y: int) -> bool:
        """
        合併元素 x 和 y 所屬的集合，使用按秩合併

        Args:
            x: 第一個元素
            y: 第二個元素

        Returns:
            bool: 如果 x 和 y 原本不在同一個集合則返回 True，否則返回 False
        """
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return False

        # 按秩合併
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_x] = root_y
            self.rank[root_y] += 1

        self.count -= 1
        return True

    def is_connected(self, x: int, y: int) -> bool:
        """
        檢查元素 x 和 y 是否在同一個集合中

        Args:
            x: 第一個元素
            y: 第二個元素

        Returns:
            bool: 如果 x 和 y 在同一個集合中則返回 True，否則返回 False
        """
        return self.find(x) == self.find(y)

    def get_count(self) -> int:
        """
        獲取連通分量數量

        Returns:
            int: 連通分量數量
        """
        return self.count


class OptimizedUnionFind:
    """
    帶路徑壓縮和按秩合併的並查集

    結合了路徑壓縮和按秩合併兩種優化，提供近乎常數時間的操作複雜度
    """

    def __init__(self, n: int):
        """
        初始化並查集

        Args:
            n: 元素數量（元素編號從 0 到 n-1）
        """
        self.parent = list(range(n))  # 每個元素的父節點
        self.rank = [0] * n  # 每個元素的秩（樹的高度）
        self.count = n  # 連通分量數量

    def find(self, x: int) -> int:
        """
        查找元素 x 所屬的集合（尋找 x 的根節點），使用路徑壓縮

        Args:
            x: 要查找的元素

        Returns:
            int: x 的根節點
        """
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y: int) -> bool:
        """
        合併元素 x 和 y 所屬的集合，使用按秩合併

        Args:
            x: 第一個元素
            y: 第二個元素

        Returns:
            bool: 如果 x 和 y 原本不在同一個集合則返回 True，否則返回 False
        """
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return False

        # 按秩合併
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_x] = root_y
            self.rank[root_y] += 1

        self.count -= 1
        return True

    def is_connected(self, x: int, y: int) -> bool:
        """
        檢查元素 x 和 y 是否在同一個集合中

        Args:
            x: 第一個元素
            y: 第二個元素

        Returns:
            bool: 如果 x 和 y 在同一個集合中則返回 True，否則返回 False
        """
        return self.find(x) == self.find(y)

    def get_count(self) -> int:
        """
        獲取連通分量數量

        Returns:
            int: 連通分量數量
        """
        return self.count


class UnionFindApplications:
    """
    並查集的應用
    """

    @staticmethod
    def detect_cycle_in_undirected_graph(n: int, edges: List[List[int]]) -> bool:
        """
        檢測無向圖中是否存在環

        Args:
            n: 節點數量（節點編號從 0 到 n-1）
            edges: 邊列表，格式為 [[u, v], ...]

        Returns:
            bool: 如果存在環則返回 True，否則返回 False
        """
        uf = OptimizedUnionFind(n)

        for u, v in edges:
            # 如果兩個節點已經在同一個集合中，則添加這條邊會形成環
            if uf.is_connected(u, v):
                return True

            uf.union(u, v)

        return False

    @staticmethod
    def kruskal_mst(n: int, edges: List[List[int]]) -> Tuple[List[List[int]], int]:
        """
        使用 Kruskal 算法求解最小生成樹

        Args:
            n: 節點數量（節點編號從 0 到 n-1）
            edges: 邊列表，格式為 [[u, v, weight], ...]

        Returns:
            Tuple[List[List[int]], int]: (最小生成樹的邊列表, 最小生成樹的總權重)
        """
        # 按權重排序邊
        edges = sorted(edges, key=lambda x: x[2])

        uf = OptimizedUnionFind(n)
        mst = []
        total_weight = 0

        for u, v, weight in edges:
            # 如果加入這條邊不會形成環，則加入最小生成樹
            if not uf.is_connected(u, v):
                uf.union(u, v)
                mst.append([u, v, weight])
                total_weight += weight

                # 如果已經有 n-1 條邊，則最小生成樹已經完成
                if len(mst) == n - 1:
                    break

        # 如果最小生成樹的邊數少於 n-1，則圖不連通
        if len(mst) < n - 1:
            return [], -1

        return mst, total_weight

    @staticmethod
    def number_of_islands(grid: List[List[str]]) -> int:
        """
        計算二維網格中島嶼的數量

        Args:
            grid: 二維網格，'1' 表示陸地，'0' 表示水

        Returns:
            int: 島嶼的數量
        """
        if not grid or not grid[0]:
            return 0

        rows, cols = len(grid), len(grid[0])
        uf = OptimizedUnionFind(rows * cols)

        # 將水域的計數減去
        water_count = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '0':
                    water_count += 1

        # 方向數組：右、下
        directions = [(0, 1), (1, 0)]

        # 合併相鄰的陸地
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    current = i * cols + j

                    for di, dj in directions:
                        ni, nj = i + di, j + dj

                        if 0 <= ni < rows and 0 <= nj < cols and grid[ni][nj] == '1':
                            neighbor = ni * cols + nj
                            uf.union(current, neighbor)

        # 島嶼數量 = 連通分量數量 - 水域數量
        return uf.get_count() - water_count

    @staticmethod
    def accounts_merge(accounts: List[List[str]]) -> List[List[str]]:
        """
        合併帳戶

        Args:
            accounts: 帳戶列表，每個帳戶格式為 [name, email1, email2, ...]

        Returns:
            List[List[str]]: 合併後的帳戶列表
        """
        # 構建郵箱到帳戶索引的映射
        email_to_id = {}
        email_to_name = {}

        for i, account in enumerate(accounts):
            name = account[0]
            for j in range(1, len(account)):
                email = account[j]
                email_to_id[email] = email_to_id.get(email, i)
                email_to_name[email] = name

        # 使用並查集合併帳戶
        uf = OptimizedUnionFind(len(accounts))

        for email, id in email_to_id.items():
            uf.union(id, email_to_id[email])

        # 構建合併後的帳戶
        id_to_emails = defaultdict(set)

        for email in email_to_id:
            root_id = uf.find(email_to_id[email])
            id_to_emails[root_id].add(email)

        # 格式化結果
        result = []
        for id, emails in id_to_emails.items():
            name = email_to_name[next(iter(emails))]
            result.append([name] + sorted(emails))

        return result


def example_usage():
    """
    示範如何使用並查集模板
    """
    print("===== 基本並查集示範 =====")

    # 創建並查集
    n = 10
    uf = BasicUnionFind(n)

    # 合併集合
    uf.union(1, 2)
    uf.union(2, 3)
    uf.union(4, 5)
    uf.union(6, 7)
    uf.union(7, 8)
    uf.union(5, 6)

    # 檢查連通性
    print(f"1 和 3 是否連通: {uf.is_connected(1, 3)}")
    print(f"1 和 5 是否連通: {uf.is_connected(1, 5)}")
    print(f"5 和 7 是否連通: {uf.is_connected(5, 7)}")

    # 獲取連通分量數量
    print(f"連通分量數量: {uf.get_count()}")

    print("\n===== 優化並查集示範 =====")

    # 創建優化並查集
    uf_opt = OptimizedUnionFind(n)

    # 合併集合
    uf_opt.union(1, 2)
    uf_opt.union(2, 3)
    uf_opt.union(4, 5)
    uf_opt.union(6, 7)
    uf_opt.union(7, 8)
    uf_opt.union(5, 6)

    # 檢查連通性
    print(f"1 和 3 是否連通: {uf_opt.is_connected(1, 3)}")
    print(f"1 和 5 是否連通: {uf_opt.is_connected(1, 5)}")
    print(f"5 和 7 是否連通: {uf_opt.is_connected(5, 7)}")

    # 獲取連通分量數量
    print(f"連通分量數量: {uf_opt.get_count()}")

    print("\n===== 並查集應用示範 =====")

    # 檢測環
    edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 2]]
    has_cycle = UnionFindApplications.detect_cycle_in_undirected_graph(5, edges)
    print(f"無向圖是否存在環: {has_cycle}")

    # 最小生成樹
    weighted_edges = [[0, 1, 10], [0, 2, 6], [0, 3, 5], [1, 3, 15], [2, 3, 4]]
    mst, total_weight = UnionFindApplications.kruskal_mst(4, weighted_edges)
    print(f"最小生成樹: {mst}")
    print(f"最小生成樹總權重: {total_weight}")

    # 島嶼數量
    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"],
    ]
    islands = UnionFindApplications.number_of_islands(grid)
    print(f"島嶼數量: {islands}")


if __name__ == "__main__":
    example_usage()
