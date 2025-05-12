from typing import List, Optional


# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children if children is not None else []


# Recursice method
class Solution01:
    def preorder(self, root: 'Node') -> List[int]:
        def dfs(node):
            if not node:
                return

            result.append(node.val)

            for child in node.children:
                dfs(child)

        result = []
        dfs(root)
        return result


# Iterative method
class Solution02:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []

        result = []
        stack = [root]

        while stack:
            node = stack.pop()
            result.append(node.val)

            for child in reversed(node.children):
                stack.append(child)

        return result


# Optimized iterative method
class Solution03:
    def preorder(self, root: 'Node') -> List[int]:
        """
        用 range(len(node.children) - 1, -1, -1) 代替 reversed()
        此方法時間效能最佳！
        """
        if not root:
            return []

        result = []
        stack = [root]

        while stack:
            node = stack.pop()
            result.append(node.val)

            # 避免使用 reversed() 函數，直接從後往前遍歷
            for i in range(len(node.children) - 1, -1, -1):
                stack.append(node.children[i])

        return result


# Generator method for memory efficiency
class Solution04:
    def preorder(self, root: 'Node') -> List[int]:
        """使用生成器（Generator）實現 N 元樹的前序遍歷
        
        生成器與 yield 關鍵字的詳細說明：
        
        1. 生成器基本概念：
           - 生成器是一種特殊的迭代器，允許按需產生值，而非一次性產生所有值
           - 使用 yield 關鍵字的函數會變成生成器函數
           - 生成器函數執行時會返回一個生成器對象
        
        2. yield 關鍵字的作用：
           - 暫停函數的執行並返回一個值
           - 保存函數的當前狀態（局部變數、執行位置等）
           - 下次調用時從暫停處繼續執行
        
        3. yield from 的特殊作用：
           - Python 3.3+ 引入的語法
           - 將一個生成器產生的所有值委託給另一個生成器
           - 等效於: for value in sub_generator: yield value
           - 在遞迴結構中特別有用
        
        4. 生成器方法的優勢：
           - 記憶體效率：按需產生值，適合處理大型樹結構
           - 延遲計算：只在需要時才計算下一個值
           - 代碼簡潔：特別是使用 yield from 時
        
        5. 時間與空間複雜度：
           - 時間複雜度：O(n)，其中 n 是樹中的節點數量
           - 空間複雜度：O(h)，其中 h 是樹的高度（遞迴調用棧的深度）
        
        範例執行過程（以簡單的 N 元樹為例）：
            1
           / \
          2   3
             / \
            4   5
        
        執行 preorder_generator(root) 時：
        1. 進入根節點 1，yield 1
        2. 遍歷子節點 2，yield from preorder_generator(2)
           - 進入節點 2，yield 2
           - 節點 2 沒有子節點，返回到節點 1
        3. 遍歷子節點 3，yield from preorder_generator(3)
           - 進入節點 3，yield 3
           - 遍歷子節點 4，yield from preorder_generator(4)
             - 進入節點 4，yield 4
             - 節點 4 沒有子節點，返回到節點 3
           - 遍歷子節點 5，yield from preorder_generator(5)
             - 進入節點 5，yield 5
             - 節點 5 沒有子節點，返回到節點 3
           - 節點 3 的子節點遍歷完畢，返回到節點 1
        4. 根節點 1 的子節點遍歷完畢，生成器結束
        
        最終產生的值序列：1, 2, 3, 4, 5（前序遍歷結果）
        
        Args:
            root: N 元樹的根節點
            
        Returns:
            List[int]: 包含 N 元樹前序遍歷結果的列表
        """

        # 使用生成器函數來產生前序遍歷結果
        def preorder_generator(node):
            if not node:
                return

            yield node.val

            for child in node.children:
                yield from preorder_generator(child)

        # 將生成器結果轉換為列表
        return list(preorder_generator(root))
