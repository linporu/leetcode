from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Iterative DFS
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []

        path_sum = {root: root.val}
        prev = {root: None}
        stack = [root]
        result = []

        while stack:
            node = stack.pop()

            if not node.left and not node.right and (path_sum[node] == targetSum):
                path = []
                curr_node = node
                while curr_node:
                    path.append(curr_node.val)
                    curr_node = prev[curr_node]
                path.reverse()
                result.append(path)
            if node.left:
                stack.append(node.left)
                prev[node.left] = node
                path_sum[node.left] = path_sum[node] + node.left.val
            if node.right:
                stack.append(node.right)
                prev[node.right] = node
                path_sum[node.right] = path_sum[node] + node.right.val

        return result


class Solution02:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        """
        Find all root-to-leaf paths where the sum of node values equals targetSum.
        Uses an iterative DFS approach with path tracking.

        Key Ideas:
        1. Instead of using separate dictionaries to track path sums and previous nodes,
           we bundle all necessary information (node, current path, current sum) in a tuple
        2. As we traverse deeper, we carry and update this information with us
        3. When we reach a leaf node, we already have the complete path and sum ready

        解題思路：
        1. 問題分析：
           - 需要追踪的信息：當前節點、到達該節點的路徑、當前路徑和
           - 避免在抵達葉子節點時才回溯構建路徑，因為回溯需要額外的時間複雜度

        2. 優化思維：
           - 原始解法使用多個字典分別存儲信息，但這些信息其實是緊密關聯的
           - 使用 tuple 將相關信息打包在一起，減少查詢開銷

        3. 狀態傳遞：
           - 每個節點的狀態都依賴於其父節點
           - 直接從父節點傳遞信息給子節點，而不是通過字典查找

        Time Complexity: O(N) where N is the number of nodes
        Space Complexity: O(N) for storing paths and stack

        Args:
            root: Root node of the binary tree
            targetSum: Target sum to find in paths

        Returns:
            List of paths (each path is a list of node values) that sum to targetSum
        """
        if not root:
            return []

        # Each stack element is a tuple of:
        # (current_node, path_so_far, sum_so_far)
        stack = [(root, [root.val], root.val)]
        result = []

        while stack:
            node, path, curr_sum = stack.pop()

            # Check if it's a leaf node and sum matches target
            if not node.left and not node.right and curr_sum == targetSum:
                result.append(path)

            # Process right child first (so left paths are processed first due to stack)
            if node.right:
                stack.append(
                    (
                        node.right,
                        path + [node.right.val],  # Extend current path
                        curr_sum + node.right.val,  # Update running sum
                    )
                )

            if node.left:
                stack.append((node.left, path + [node.left.val], curr_sum + node.left.val))

        return result


# Recursive DFS
class Solution03:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        """
        Find all root-to-leaf paths where the sum of node values equals targetSum.
        Uses recursive DFS with backtracking for optimal performance.

        優化思路：
        1. 使用遞迴 + 回溯，避免重複創建 list
        2. 用同一個 list 來追踪路徑，通過回溯來恢復狀態
        3. 只在找到完整路徑時才創建新的 list

        Time Complexity: O(N), where N is the number of nodes
        Space Complexity: O(H) for recursion stack, where H is the height of the tree
        """

        def dfs(node: TreeNode, curr_sum: int, path: List[int], result: List[List[int]]) -> None:
            if not node:
                return

            # Add current node to path
            path.append(node.val)
            curr_sum += node.val

            # Check if it's a leaf node and sum matches target
            if not node.left and not node.right and curr_sum == targetSum:
                result.append(path[:])  # Create a new list only when needed

            # Recurse on children
            dfs(node.left, curr_sum, path, result)
            dfs(node.right, curr_sum, path, result)

            # Backtrack
            path.pop()

        result = []
        dfs(root, 0, [], result)
        return result
