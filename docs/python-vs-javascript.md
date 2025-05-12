# Python vs JavaScript 語法對照速查表

## 1. 基本語法

### 註解

```python
# Python
# 單行註解
"""
多行註解
"""
```

```javascript
// JavaScript
// 單行註解
/*
多行註解
*/
```

### 變數宣告

```python
# Python
x = 10  # 不需要關鍵字
```

```javascript
// JavaScript
let x = 10; // 可變變數
const y = 20; // 常數（不可重新賦值）
var z = 30; // 舊式宣告（函數作用域）
```

### 打印輸出

```python
# Python
print("Hello")
print(f"Value: {x}")  # f-string
```

```javascript
// JavaScript
console.log("Hello");
console.log(`Value: ${x}`); // 模板字串
```

## 2. 資料型態

### 型態檢查

```python
# Python
type(x)
isinstance(x, int)
```

```javascript
// JavaScript
typeof x;
x instanceof Array;
```

### 字串操作

```python
# Python
s = "hello"
s.upper()
s.lower()
s.replace("h", "H")
len(s)
s[0]  # 索引
s[1:3]  # 切片
s.split(",")
"".join(arr)
```

```javascript
// JavaScript
let s = "hello";
s.toUpperCase();
s.toLowerCase();
s.replace("h", "H");
s.length; // 注意：是屬性，不是方法
s[0]; // 索引
s.substring(1, 3); // 或 s.slice(1, 3)
s.split(",");
arr.join("");
```

### 數字操作

```python
# Python
int("123")
float("123.45")
str(123)
5 // 2  # 整數除法 = 2
5 % 2   # 餘數 = 1
2 ** 3  # 次方 = 8
```

```javascript
// JavaScript
parseInt("123");
parseFloat("123.45");
String(123); // 或 123.toString()
Math.floor(5 / 2); // 整數除法 = 2
5 % 2; // 餘數 = 1
2 ** 3; // 或 Math.pow(2, 3) = 8
```

## 3. 資料結構

### 陣列/列表

```python
# Python
arr = [1, 2, 3]
arr.append(4)
arr.pop()
arr.pop(0)  # 移除第一個
arr.insert(0, 0)
len(arr)
arr[0]
arr[-1]  # 最後一個
arr[1:3]  # 切片
```

```javascript
// JavaScript
let arr = [1, 2, 3];
arr.push(4);
arr.pop();
arr.shift(); // 移除第一個
arr.unshift(0); // 在開頭插入
arr.length; // 屬性
arr[0];
arr[arr.length - 1]; // 最後一個
arr.slice(1, 3); // 切片
```

### 字典/物件

```python
# Python
d = {"key": "value"}
d["key"]
d.get("key", "default")
"key" in d
d.keys()
d.values()
d.items()
```

```javascript
// JavaScript
let obj = { key: "value" };
obj.key; // 或 obj["key"]
obj.key || "default"; // 簡易預設值
"key" in obj;
Object.keys(obj);
Object.values(obj);
Object.entries(obj);
```

### 集合 Set

```python
# Python
s = set([1, 2, 3])
s.add(4)
s.remove(1)  # 會拋出錯誤如果不存在
s.discard(1)  # 不會拋出錯誤
1 in s
```

```javascript
// JavaScript
let s = new Set([1, 2, 3]);
s.add(4);
s.delete(1); // 不會拋出錯誤
s.has(1);
```

## 4. 控制流程

### 條件判斷

```python
# Python
if x > 0:
    print("positive")
elif x < 0:
    print("negative")
else:
    print("zero")
```

```javascript
// JavaScript
if (x > 0) {
  console.log("positive");
} else if (x < 0) {
  console.log("negative");
} else {
  console.log("zero");
}
```

### 三元運算子

```python
# Python
result = "yes" if condition else "no"
```

```javascript
// JavaScript
let result = condition ? "yes" : "no";
```

## 5. 迴圈

### For 迴圈

```python
# Python
for i in range(5):
    print(i)

for item in arr:
    print(item)

for i, item in enumerate(arr):
    print(i, item)
```

```javascript
// JavaScript
for (let i = 0; i < 5; i++) {
  console.log(i);
}

for (let item of arr) {
  console.log(item);
}

arr.forEach((item, i) => {
  console.log(i, item);
});
```

### While 迴圈

```python
# Python
while x > 0:
    x -= 1
```

```javascript
// JavaScript
while (x > 0) {
  x--;
}
```

## 6. 函數

### 函數定義

```python
# Python
def add(a, b):
    return a + b

# 預設參數
def greet(name="World"):
    return f"Hello, {name}"
```

```javascript
// JavaScript
function add(a, b) {
  return a + b;
}

// 箭頭函數
const add = (a, b) => a + b;

// 預設參數
function greet(name = "World") {
  return `Hello, ${name}`;
}
```

## 7. 陣列方法對照

### 高階函數

```python
# Python
# map
result = list(map(lambda x: x * 2, arr))

# filter
result = list(filter(lambda x: x > 0, arr))

# reduce
from functools import reduce
result = reduce(lambda acc, x: acc + x, arr, 0)
```

```javascript
// JavaScript
// map
let result = arr.map((x) => x * 2);

// filter
let result = arr.filter((x) => x > 0);

// reduce
let result = arr.reduce((acc, x) => acc + x, 0);
```

### 其他常用方法

```python
# Python
sorted(arr)  # 返回新陣列
arr.sort()   # 原地排序
arr.reverse()
any(arr)  # 任一為真
all(arr)  # 全部為真
sum(arr)
```

```javascript
// JavaScript
[...arr].sort(); // 返回新陣列
arr.sort(); // 原地排序
arr.reverse();
arr.some((x) => x); // 任一為真
arr.every((x) => x); // 全部為真
arr.reduce((a, b) => a + b, 0); // sum
```

## 8. 特殊語法

### 解構賦值

```python
# Python
a, b = [1, 2]
a, *rest = [1, 2, 3, 4]
```

```javascript
// JavaScript
let [a, b] = [1, 2];
let [a, ...rest] = [1, 2, 3, 4];
let { x, y } = { x: 1, y: 2 }; // 物件解構
```

### 展開運算符

```python
# Python
arr2 = [*arr1, 4, 5]
dict2 = {**dict1, "key": "value"}
```

```javascript
// JavaScript
let arr2 = [...arr1, 4, 5];
let obj2 = { ...obj1, key: "value" };
```

## 9. 邏輯運算

### 比較運算符

```python
# Python
x == y   # 值相等
x is y   # 記憶體位置相同
x != y
x is not y
```

```javascript
// JavaScript
x == y; // 寬鬆相等（會型別轉換）
x === y; // 嚴格相等（不會型別轉換）
x != y; // 寬鬆不等
x !== y; // 嚴格不等
```

### 邏輯運算符

```python
# Python
and, or, not
```

```javascript
// JavaScript
&&, ||, !
```

### 真假值

```python
# Python 的 Falsy 值
False, None, 0, "", [], {}, set()
```

```javascript
// JavaScript 的 Falsy 值
false, null, undefined, 0, "", NaN;
```

## 10. 例外處理

```python
# Python
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Error: {e}")
finally:
    print("Cleanup")
```

```javascript
// JavaScript
try {
  let result = 10 / 0; // 不會拋出錯誤，結果是 Infinity
  throw new Error("Custom error");
} catch (e) {
  console.log(`Error: ${e.message}`);
} finally {
  console.log("Cleanup");
}
```

## 11. 類別/物件導向

```python
# Python
class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, {self.name}"

person = Person("Alice")
```

```javascript
// JavaScript
class Person {
  constructor(name) {
    this.name = name;
  }

  greet() {
    return `Hello, ${this.name}`;
  }
}

let person = new Person("Alice");
```

## 12. 模組/導入

```python
# Python
import math
from math import sqrt
import numpy as np
```

```javascript
// JavaScript (ES6 modules)
import math from "./math.js";
import { sqrt } from "./math.js";
import * as np from "./numpy.js";
```

## 13. 常見陷阱

### Python to JavaScript

1. **縮排 vs 大括號**：JavaScript 使用 `{}` 而不是縮排
2. **分號**：JavaScript 建議使用分號結尾
3. **嚴格相等**：總是使用 `===` 而不是 `==`
4. **陣列長度**：`.length` 是屬性，不是方法
5. **字串不可變**：兩種語言的字串都不可變
6. **整數除法**：JavaScript 需要 `Math.floor()`

### JavaScript 特有

1. **undefined vs null**：JavaScript 有兩個「空」值
2. **NaN**：Not a Number，使用 `isNaN()` 檢查
3. **this 綁定**：箭頭函數和一般函數的 `this` 行為不同
4. **提升（Hoisting）**：變數和函數宣告會被提升

## 14. LeetCode 常用技巧對照

### 二維陣列初始化

```python
# Python
grid = [[0] * cols for _ in range(rows)]
```

```javascript
// JavaScript
let grid = Array(rows)
  .fill(0)
  .map(() => Array(cols).fill(0));
```

### 字典預設值

```python
# Python
from collections import defaultdict
d = defaultdict(int)
d[key] += 1
```

```javascript
// JavaScript
let d = {};
d[key] = (d[key] || 0) + 1;
```

### 無限大

```python
# Python
float('inf')
float('-inf')
```

```javascript
// JavaScript
Infinity - Infinity;
```

### 堆/優先隊列

```python
# Python
import heapq
heapq.heappush(heap, item)
heapq.heappop(heap)
```

```javascript
// JavaScript
// 沒有內建 heap，需要自己實現或使用第三方庫
// 但可以用陣列模擬（效率較低）
arr.push(item);
arr.sort((a, b) => a - b);
let min = arr.shift();
```

### 深拷貝

```python
# Python
import copy
new_arr = copy.deepcopy(arr)
```

```javascript
// JavaScript
// 簡單情況（只有基本型別）
let new_arr = JSON.parse(JSON.stringify(arr));
// 或使用展開運算符（淺拷貝）
let new_arr = [...arr];
```
