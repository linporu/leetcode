# Linked List 資料結構 LeetCode 學習清單

## 技巧使用時機

### 1. 快慢指標技巧 (Fast & Slow Pointers)

使用時機：

- 需要找出鏈結串列的中點（如：判斷回文）
- 需要檢測鏈結串列是否有環
- 需要找出環的起點
- 需要將鏈結串列對半分割

### 2. 反轉技巧 (Reversal)

使用時機：

- 需要完整反轉整個鏈結串列
- 需要反轉特定範圍內的節點
- 需要驗證回文結構（與快慢指標配合）
- 需要重新排列鏈結串列（如：頭尾相接）

### 3. 合併技巧 (Merge)

使用時機：

- 合併兩個已排序的鏈結串列
- 合併 K 個已排序的鏈結串列（搭配分治或優先佇列）
- 需要將兩個鏈結串列以特定模式交錯合併
- 需要將拆分的鏈結串列重新組合

### 4. 雙指標技巧 (Two Pointers)

使用時機：

- 需要找出倒數第 N 個節點
- 需要刪除特定節點（如：倒數第 N 個）
- 需要找出兩個鏈結串列的相交點
- 需要檢測環狀結構（與快慢指標類似）
- 需要以固定間距處理節點

## 基本解題技巧

### 1. 快慢指標技巧 (Fast & Slow Pointers)

- 尋找中點 (Finding Middle)
- 檢測環狀結構 (Cycle Detection)
- 找出環的起點 (Finding Cycle Start)

### 2. 反轉技巧 (Reversal)

- 完整反轉 (Complete Reversal)
- 部分反轉 (Partial Reversal)
- 遞迴反轉 (Recursive Reversal)

### 3. 合併技巧 (Merge)

- 兩個鏈結串列合併 (Merge Two Lists)
- 多個鏈結串列合併 (Merge Multiple Lists)

### 4. 雙指標技巧 (Two Pointers)

- 刪除特定節點 (Remove Nodes)
- 找出倒數第 N 個節點 (Find Nth from End)
- 相交節點 (Intersection Point)

## 練習題目

### 基礎題 - 快慢指標

1. [876. Middle of the Linked List](https://leetcode.com/problems/middle-of-the-linked-list/) (Easy)

   - 技巧：使用快慢指標找中點
   - 時間複雜度：O(n)
   - 空間複雜度：O(1)

2. [141. Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/) (Easy)

   - 技巧：使用快慢指標檢測環狀結構
   - 時間複雜度：O(n)
   - 空間複雜度：O(1)

3. [142. Linked List Cycle II](https://leetcode.com/problems/linked-list-cycle-ii/) (Medium)
   - 技巧：使用快慢指標找出環的起點
   - 時間複雜度：O(n)
   - 空間複雜度：O(1)

### 基礎題 - 反轉技巧

1. [206. Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/) (Easy)

   - 技巧：迭代或遞迴方式反轉整個鏈結串列
   - 時間複雜度：O(n)
   - 空間複雜度：O(1) 迭代，O(n) 遞迴

2. [92. Reverse Linked List II](https://leetcode.com/problems/reverse-linked-list-ii/) (Medium)
   - 技巧：反轉指定範圍內的節點
   - 時間複雜度：O(n)
   - 空間複雜度：O(1)

### 基礎題 - 合併技巧

1. [21. Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/) (Easy)
   - 技巧：合併兩個已排序的鏈結串列
   - 時間複雜度：O(n + m)
   - 空間複雜度：O(1)

### 基礎題 - 雙指標

1. [19. Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/) (Medium)

   - 技巧：使用雙指標找出倒數第 N 個節點
   - 時間複雜度：O(n)
   - 空間複雜度：O(1)

2. [160. Intersection of Two Linked Lists](https://leetcode.com/problems/intersection-of-two-linked-lists/) (Easy)
   - 技巧：找出兩個鏈結串列的相交點
   - 時間複雜度：O(n + m)
   - 空間複雜度：O(1)

## 進階練習題

1. [234. Palindrome Linked List](https://leetcode.com/problems/palindrome-linked-list/) (Easy)

   - 技巧：快慢指標找中點 + 反轉後半部 + 比較
   - 時間複雜度：O(n)
   - 空間複雜度：O(1)

2. [143. Reorder List](https://leetcode.com/problems/reorder-list/) (Medium)

   - 技巧：找中點 + 反轉後半部 + 合併
   - 時間複雜度：O(n)
   - 空間複雜度：O(1)

3. [25. Reverse Nodes in k-Group](https://leetcode.com/problems/reverse-nodes-in-k-group/) (Hard)

   - 技巧：分組反轉 + 鏈結操作
   - 時間複雜度：O(n)
   - 空間複雜度：O(1)

4. [146. LRU Cache](https://leetcode.com/problems/lru-cache/) (Medium)

   - 技巧：雙向鏈結串列 + HashMap
   - 時間複雜度：O(1) 所有操作
   - 空間複雜度：O(capacity)

5. [23. Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/) (Hard)
   - 技巧：分治合併 或 優先佇列
   - 時間複雜度：O(N log k)，N 為總節點數，k 為串列數量
   - 空間複雜度：O(k)

## 效能優化技巧

1. 使用虛擬頭節點（Dummy Node）

   - 簡化邊界條件處理
   - 統一操作邏輯
   - 適用於需要修改頭節點的情況

2. 空間複雜度優化

   - 優先使用迭代而非遞迴
   - 善用原地修改
   - 避免不必要的臨時串列

3. 時間複雜度優化
   - 善用快慢指標
   - 一次遍歷完成多個操作
   - 使用適當的資料結構（如 HashMap）輔助

## 學習建議

1. 鏈結串列的基本操作：

   - 熟悉節點的新增、刪除、修改操作
   - 理解指標的移動和重新連接
   - 注意邊界條件（空串列、單節點）

2. 解題技巧：

   - 畫圖幫助理解指標移動
   - 使用虛擬頭節點（dummy node）簡化操作
   - 先處理簡單案例，再考慮複雜情況
   - 注意指標更新的順序，避免斷鏈

3. 常見錯誤：
   - 忘記處理空串列或單節點情況
   - 未正確更新指標導致斷鏈
   - 在環狀結構中陷入無限循環

## 學習順序建議

1. Week 1: 基本操作 (206)
2. Week 2: 快慢指標題目 (876, 141)
3. Week 3: 合併技巧題目 (21)
4. Week 4: 雙指標題目 (19, 160)
5. Week 5: 進階題目 (234, 143)

## Python 解題模版

### 1. 基礎結構與工具函數

```python
# 節點定義
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 建立測試用的鏈結串列
def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# 印出鏈結串列
def print_linked_list(head):
    values = []
    current = head
    while current:
        values.append(str(current.val))
        current = current.next
    print(" -> ".join(values))
```

### 2. 基本操作模版

```python
# 插入節點
def insert_node(head, val, position):
    dummy = ListNode(0)
    dummy.next = head
    current = dummy

    # 移動到插入位置
    for _ in range(position):
        if not current:
            return dummy.next
        current = current.next

    # 插入新節點
    new_node = ListNode(val)
    new_node.next = current.next
    current.next = new_node

    return dummy.next

# 刪除節點
def delete_node(head, position):
    dummy = ListNode(0)
    dummy.next = head
    current = dummy

    # 移動到刪除位置的前一個節點
    for _ in range(position):
        if not current:
            return dummy.next
        current = current.next

    # 刪除節點
    if current.next:
        current.next = current.next.next

    return dummy.next

# 搜尋節點
def search_node(head, target):
    current = head
    position = 0

    while current:
        if current.val == target:
            return position
        current = current.next
        position += 1

    return -1
```

### 3. 進階操作模版

```python
# 反轉鏈結串列（迭代）
def reverse_iterative(head):
    prev = None
    current = head

    while current:
        next_temp = current.next
        current.next = prev
        prev = current
        current = next_temp

    return prev

# 反轉鏈結串列（遞迴）
def reverse_recursive(head):
    if not head or not head.next:
        return head

    new_head = reverse_recursive(head.next)
    head.next.next = head
    head.next = None

    return new_head

# 快慢指標找中點
def find_middle(head):
    if not head or not head.next:
        return head

    slow = fast = head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    return slow

# 檢測環狀結構
def has_cycle(head):
    if not head or not head.next:
        return False

    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True

    return False
```

### 4. 常用組合操作模版

```python
# 合併兩個排序鏈結串列
def merge_sorted_lists(l1, l2):
    dummy = ListNode(0)
    current = dummy

    while l1 and l2:
        if l1.val <= l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next

    current.next = l1 if l1 else l2
    return dummy.next

# 找出並刪除倒數第 N 個節點
def remove_nth_from_end(head, n):
    dummy = ListNode(0)
    dummy.next = head
    first = dummy
    second = dummy

    # 移動 first 指標
    for _ in range(n + 1):
        first = first.next

    # 同時移動兩個指標
    while first:
        first = first.next
        second = second.next

    # 刪除目標節點
    second.next = second.next.next
    return dummy.next

# 判斷回文鏈結串列
def is_palindrome(head):
    if not head or not head.next:
        return True

    # 找中點
    mid = find_middle(head)

    # 反轉後半部分
    second_half = reverse_iterative(mid.next)

    # 比較兩半部分
    first = head
    second = second_half
    result = True

    while result and second:
        if first.val != second.val:
            result = False
        first = first.next
        second = second.next

    # 恢復原始鏈結串列（可選）
    mid.next = reverse_iterative(second_half)

    return result
```

### 5. 特殊情況處理模版

```python
# 處理環狀鏈結串列
def detect_cycle_start(head):
    if not head or not head.next:
        return None

    # 找到相遇點
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    else:
        return None

    # 找環的起點
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next

    return slow

# 找出兩個鏈結串列的相交點
def get_intersection_node(headA, headB):
    if not headA or not headB:
        return None

    # 計算長度差異
    lenA = lenB = 0
    currA, currB = headA, headB

    while currA:
        lenA += 1
        currA = currA.next
    while currB:
        lenB += 1
        currB = currB.next

    # 對齊起點
    currA, currB = headA, headB
    if lenA > lenB:
        for _ in range(lenA - lenB):
            currA = currA.next
    else:
        for _ in range(lenB - lenA):
            currB = currB.next

    # 找相交點
    while currA != currB:
        currA = currA.next
        currB = currB.next

    return currA
```
