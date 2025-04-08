# Sorting 排序演算法 LeetCode 學習清單

## 基本解題技巧

### 1. 比較排序 (Comparison Sort)

- 氣泡排序 (Bubble Sort)
- 選擇排序 (Selection Sort)
- 插入排序 (Insertion Sort)
- 快速排序 (Quick Sort)
- 合併排序 (Merge Sort)
- 堆積排序 (Heap Sort)

### 2. 非比較排序 (Non-comparison Sort)

- 計數排序 (Counting Sort)
- 基數排序 (Radix Sort)
- 桶排序 (Bucket Sort)

### 3. 排序應用技巧

- 自定義排序 (Custom Sort)
- 部分排序 (Partial Sort)
- 多重排序條件 (Multiple Criteria Sort)

### 4. 特殊排序技巧

- 雙指標排序 (Two Pointers Sort)
- 三指標排序 (Three Pointers Sort)
- 原地排序 (In-place Sort)

## 排序演算法使用時機

### 1. 比較排序使用時機

#### 氣泡排序 (Bubble Sort)

使用時機：

- 資料量小（n < 50）
- 資料幾乎已經排序
- 需要穩定排序
- 空間要求嚴格，只能使用 O(1) 額外空間
- 實作簡單，適合教學或快速實作

#### 選擇排序 (Selection Sort)

使用時機：

- 資料量小（n < 50）
- 寫入成本很高，需要最小化寫入次數
- 不在意排序穩定性
- 需要原地排序，額外空間要求 O(1)

#### 插入排序 (Insertion Sort)

使用時機：

- 資料量小（n < 50）
- 資料幾乎已經排序
- 需要穩定排序
- 需要線上排序（即時插入新元素）
- 作為其他排序算法的優化（如快速排序的小區間優化）

#### 快速排序 (Quick Sort)

使用時機：

- 資料量大
- 不需要穩定排序
- 需要原地排序
- 平均情況下需要最佳效能
- 資料隨機分布
- 記憶體快取要求高

#### 合併排序 (Merge Sort)

使用時機：

- 需要穩定排序
- 資料量大
- 有足夠的額外記憶體空間
- 適合外部排序
- 需要平穩的效能表現（最壞情況仍為 O(n log n)）
- 適合平行處理

#### 堆積排序 (Heap Sort)

使用時機：

- 需要原地排序
- 不需要穩定排序
- 需要找出最大/最小的 k 個元素
- 需要持續處理動態加入的資料
- 記憶體限制嚴格

### 2. 非比較排序使用時機

#### 計數排序 (Counting Sort)

使用時機：

- 資料範圍已知且較小
- 資料為整數或可映射為整數
- 資料分布密集
- 需要線性時間複雜度
- 需要穩定排序
- 有足夠的額外記憶體

#### 基數排序 (Radix Sort)

使用時機：

- 資料可以分割為位數（如整數、字串）
- 每個位數的範圍較小
- 需要穩定排序
- 資料位數不會太多
- 有足夠的額外記憶體

#### 桶排序 (Bucket Sort)

使用時機：

- 資料均勻分布
- 資料範圍可以有效分割成桶
- 有足夠的額外記憶體
- 需要線性時間複雜度
- 適合浮點數排序

### 3. 特殊排序技巧使用時機

#### 雙指標排序

使用時機：

- 需要 in-place 操作
- 處理特定模式（如移動零到末尾）
- 需要保持相對順序
- 資料有特殊的分類要求

#### 三指標排序

使用時機：

- 三路快排（處理大量重複元素）
- 三色排序問題（如荷蘭國旗問題）
- 需要同時處理三種類別的元素
- 需要原地排序

#### 原地排序

使用時機：

- 記憶體空間受限
- 資料量大
- 需要最小化記憶體使用
- 需要就地修改原陣列

## 進階概念

### 1. 排序算法的穩定性

- 穩定排序：
  - 合併排序 (Merge Sort)
  - 插入排序 (Insertion Sort)
  - 氣泡排序 (Bubble Sort)
  - 計數排序 (Counting Sort)
- 不穩定排序：
  - 快速排序 (Quick Sort)
  - 堆積排序 (Heap Sort)
  - 選擇排序 (Selection Sort)

### 2. 排序算法的選擇準則

1. 資料規模考量：

   - 小規模資料（n < 50）：插入排序
   - 中等規模：快速排序
   - 大規模資料：合併排序或堆積排序

2. 空間限制考量：

   - 有額外空間：合併排序
   - 原地排序需求：快速排序

3. 資料特性考量：
   - 大量重複元素：三路快排
   - 部分已排序：插入排序
   - 資料範圍已知且較小：計數排序

### 3. 常見最佳化技巧

1. 快速排序優化：

   - 三數取中選擇 pivot
   - 處理重複元素的三路快排
   - 小規模子陣列使用插入排序

2. 合併排序優化：
   - 小規模子陣列使用插入排序
   - 避免不必要的合併操作
   - 原地合併的實作

## 練習題目

### 基礎題 - 基本排序實作

1. [912. Sort an Array](https://leetcode.com/problems/sort-an-array/) (Medium)

   - 技巧：實作各種基本排序算法
   - 時間複雜度：O(n log n)
   - 空間複雜度：O(n) 或 O(1)

2. [75. Sort Colors](https://leetcode.com/problems/sort-colors/) (Medium)
   - 技巧：三指標排序（荷蘭國旗問題）
   - 時間複雜度：O(n)
   - 空間複雜度：O(1)

### 基礎題 - 計數排序應用

1. [242. Valid Anagram](https://leetcode.com/problems/valid-anagram/) (Easy)

   - 技巧：使用計數排序思想
   - 時間複雜度：O(n)
   - 空間複雜度：O(1)

2. [1122. Relative Sort Array](https://leetcode.com/problems/relative-sort-array/) (Easy)
   - 技巧：計數排序 + 自定義順序
   - 時間複雜度：O(n)
   - 空間複雜度：O(max(arr1))

### 基礎題 - 合併排序應用

1. [88. Merge Sorted Array](https://leetcode.com/problems/merge-sorted-array/) (Easy)

   - 技巧：合併兩個已排序陣列
   - 時間複雜度：O(m + n)
   - 空間複雜度：O(1)

2. [21. Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/) (Easy)
   - 技巧：合併兩個已排序鏈結串列
   - 時間複雜度：O(m + n)
   - 空間複雜度：O(1)

### 進階題 - 排序變體

1. [179. Largest Number](https://leetcode.com/problems/largest-number/) (Medium)

   - 技巧：自定義排序規則
   - 時間複雜度：O(n log n)
   - 空間複雜度：O(n)

2. [148. Sort List](https://leetcode.com/problems/sort-list/) (Medium)
   - 技巧：鏈結串列的合併排序
   - 時間複雜度：O(n log n)
   - 空間複雜度：O(1)

## 額外練習題目

### 中級題目

1. [147. Insertion Sort List](https://leetcode.com/problems/insertion-sort-list/) (Medium)

   - 技巧：鏈結串列的插入排序實作
   - 時間複雜度：O(n²)
   - 空間複雜度：O(1)

2. [324. Wiggle Sort II](https://leetcode.com/problems/wiggle-sort-ii/) (Medium)

   - 技巧：特殊排序要求，需要考慮重複元素
   - 時間複雜度：O(n log n)
   - 空間複雜度：O(n)

3. [280. Wiggle Sort](https://leetcode.com/problems/wiggle-sort/) (Medium)
   - 技巧：相鄰元素交換的特殊排序
   - 時間複雜度：O(n)
   - 空間複雜度：O(1)

### 高級題目

1. [315. Count of Smaller Numbers After Self](https://leetcode.com/problems/count-of-smaller-numbers-after-self/) (Hard)

   - 技巧：合併排序 + 索引追蹤
   - 時間複雜度：O(n log n)
   - 空間複雜度：O(n)

2. [493. Reverse Pairs](https://leetcode.com/problems/reverse-pairs/) (Hard)
   - 技巧：合併排序 + 計數
   - 時間複雜度：O(n log n)
   - 空間複雜度：O(n)

## 效能優化建議

1. 記憶體管理：

   - 避免不必要的記憶體分配
   - 善用原地排序算法
   - 考慮快取友好的實作

2. 特殊情況處理：

   - 空陣列或單元素陣列
   - 已排序或接近排序的輸入
   - 大量重複元素的情況

3. 實作細節：
   - 使用適當的 pivot 選擇策略
   - 處理邊界條件
   - 優化遞迴深度

## 學習建議

1. 循序漸進：

   - 從基本排序算法開始
   - 理解每種算法的優缺點
   - 掌握常見的優化技巧

2. 實作練習：

   - 手寫基本排序算法
   - 處理特殊輸入情況
   - 實作效能優化版本

3. 應用場景：
   - 理解不同排序算法的適用場景
   - 練習分析問題並選擇合適的算法
   - 考慮實際系統限制

## 學習順序建議

1. Week 1: 基本排序算法實作 (912)
2. Week 2: 特殊排序問題 (75)
3. Week 3: 計數排序應用 (242, 1122)
4. Week 4: 合併排序應用 (88, 21)
5. Week 5: 進階排序問題 (179, 148)

## Python 實作提示

### 1. 基礎排序模板

```python
# 氣泡排序
def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        # 最後 i 個元素已經排好
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# 選擇排序
def selectionSort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# 插入排序
def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# 堆積排序
def heapSort(arr):
    def heapify(arr, n, i):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2

        if l < n and arr[l] > arr[largest]:
            largest = l
        if r < n and arr[r] > arr[largest]:
            largest = r

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(arr, n, largest)

    n = len(arr)
    # 建立最大堆
    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i)

    # 一個一個取出元素
    for i in range(n-1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)
    return arr
```

### 2. 進階排序模板

```python
# 三路快速排序
def quickSort3Way(arr):
    def sort(arr, lo, hi):
        if hi <= lo:
            return

        lt = lo
        gt = hi
        i = lo + 1
        pivot = arr[lo]

        while i <= gt:
            if arr[i] < pivot:
                arr[lt], arr[i] = arr[i], arr[lt]
                lt += 1
                i += 1
            elif arr[i] > pivot:
                arr[i], arr[gt] = arr[gt], arr[i]
                gt -= 1
            else:
                i += 1

        sort(arr, lo, lt - 1)
        sort(arr, gt + 1, hi)

    sort(arr, 0, len(arr) - 1)
    return arr

# 桶排序
def bucketSort(arr):
    if not arr:
        return arr

    # 找出範圍
    max_val, min_val = max(arr), min(arr)

    # 建立桶
    bucket_range = (max_val - min_val) / len(arr)
    buckets = [[] for _ in range(len(arr) + 1)]

    # 分配到桶中
    for num in arr:
        if num == max_val:
            bucket_idx = len(arr) - 1
        else:
            bucket_idx = int((num - min_val) / bucket_range)
        buckets[bucket_idx].append(num)

    # 對每個桶排序
    for bucket in buckets:
        bucket.sort()

    # 組合結果
    result = []
    for bucket in buckets:
        result.extend(bucket)

    return result

# 基數排序
def radixSort(arr):
    def countingSort(arr, exp):
        n = len(arr)
        output = [0] * n
        count = [0] * 10

        for i in range(n):
            idx = arr[i] // exp
            count[idx % 10] += 1

        for i in range(1, 10):
            count[i] += count[i - 1]

        i = n - 1
        while i >= 0:
            idx = arr[i] // exp
            output[count[idx % 10] - 1] = arr[i]
            count[idx % 10] -= 1
            i -= 1

        for i in range(n):
            arr[i] = output[i]

    if not arr:
        return arr

    max_val = max(arr)
    exp = 1
    while max_val // exp > 0:
        countingSort(arr, exp)
        exp *= 10

    return arr
```

### 3. 特殊排序應用模板

```python
# 自定義排序（以 Largest Number 為例）
def largestNumber(nums):
    def compare(a, b):
        return int(b + a) - int(a + b)

    nums = [str(num) for num in nums]
    nums.sort(key=functools.cmp_to_key(compare))
    return ''.join(nums).lstrip('0') or '0'

# 部分排序（以 Top K 為例）
def findKthLargest(nums, k):
    def quickSelect(nums, k, left, right):
        if left == right:
            return nums[left]

        pivot_idx = random.randint(left, right)
        pivot = nums[pivot_idx]
        nums[pivot_idx], nums[right] = nums[right], nums[pivot_idx]

        store_idx = left
        for i in range(left, right):
            if nums[i] > pivot:
                nums[store_idx], nums[i] = nums[i], nums[store_idx]
                store_idx += 1

        nums[right], nums[store_idx] = nums[store_idx], nums[right]

        if k == store_idx + 1:
            return nums[store_idx]
        elif k < store_idx + 1:
            return quickSelect(nums, k, left, store_idx - 1)
        else:
            return quickSelect(nums, k, store_idx + 1, right)

    return quickSelect(nums, k, 0, len(nums) - 1)

# 多重條件排序
def customSortArray(arr):
    # 使用 lambda 和 tuple 進行多重條件排序
    arr.sort(key=lambda x: (condition1(x), condition2(x), condition3(x)))
    return arr

# 三指標排序（以 Sort Colors 為例）
def sortColors(nums):
    left = curr = 0
    right = len(nums) - 1

    while curr <= right:
        if nums[curr] == 0:
            nums[left], nums[curr] = nums[curr], nums[left]
            left += 1
            curr += 1
        elif nums[curr] == 2:
            nums[curr], nums[right] = nums[right], nums[curr]
            right -= 1
        else:
            curr += 1
```

### 4. 實用的排序相關函數

```python
# Python 內建排序
def pythonSortExample():
    # 基本排序
    arr.sort()  # 原地排序
    sorted_arr = sorted(arr)  # 返回新陣列

    # 反向排序
    arr.sort(reverse=True)
    sorted_arr = sorted(arr, reverse=True)

    # 自定義 key 函數
    arr.sort(key=lambda x: len(str(x)))

    # 多重條件排序
    arr.sort(key=lambda x: (len(x), x))

    # 使用 operator 模組
    from operator import itemgetter, attrgetter
    arr.sort(key=itemgetter(1))  # 根據第二個元素排序
    objects.sort(key=attrgetter('name'))  # 根據物件屬性排序

# 穩定排序檢查
def isStableSort(original, sorted_arr):
    # 檢查排序後相等元素的相對位置是否保持不變
    positions = {}
    for i, item in enumerate(original):
        if item not in positions:
            positions[item] = []
        positions[item].append(i)

    for i, item in enumerate(sorted_arr):
        if not positions[item] or positions[item][0] > positions[item][-1]:
            return False
        positions[item].pop(0)

    return True
```
