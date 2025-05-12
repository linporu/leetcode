from typing import List


# Iterative DFS
class Solution01:
    def restoreIpAddresses(self, s: str) -> List[str]:
        """
        把問題視為「用 1 or 2 or 3 個數字，4 次內湊出 len(s)，這就是個可行的分割方式」
        """

        def split_string_as(path: List[int]) -> List[str]:

            digits = []
            curr = 0

            for p in path:
                digits.append(s[curr: curr + p])
                curr += p

            return digits

        def is_valid(digits: str) -> bool:
            # 檢查空字串
            if not digits:
                return False

            # 檢查前導零
            if len(digits) > 1 and digits.startswith("0"):
                return False

            # 檢查數值範圍
            digits_num = int(digits)
            if digits_num < 0 or digits_num > 255:
                return False

            return True

        ip_length = len(s)

        # Check impossible IP string length
        if ip_length < 4 or ip_length > 12:
            return []

        result = []
        path = []
        curr_sum = 0
        curr_num = 0  # 累積有幾個數字
        stack = [(path, curr_sum, curr_num)]

        while stack:
            path, curr_sum, curr_num = stack.pop()

            if curr_sum > ip_length:
                continue

            if curr_num > 4:
                continue

            if curr_sum == ip_length and curr_num == 4:

                digits = split_string_as(path)

                if all([is_valid(digit) for digit in digits]):
                    digit_1, digit_2, digit_3, digit_4 = digits
                    valid_ip_address = digit_1 + "." + digit_2 + "." + digit_3 + "." + digit_4
                    result.append(valid_ip_address)
                    continue

            for i in range(1, 4):
                new_sum = curr_sum + i
                new_num = curr_num + 1

                if new_sum > ip_length:
                    continue

                if new_num > 4:
                    continue

                # 創建 path 的副本，然後添加新元素
                new_path = path.copy()
                new_path.append(i)
                stack.append((new_path, new_sum, new_num))

        return result


class Solution02:

    def restoreIpAddresses(self, s: str) -> List[str]:
        if len(s) < 4 or len(s) > 12:
            return []

        result = []

        def backtrack(start: int, dots: int, current_ip: str):
            # 如果已經放置了3個點，且剩餘的字串是合法的，則添加到結果中
            if dots == 3:
                segment = s[start:]
                # 直接檢查最後一個段落是否合法
                if is_valid_segment(segment):
                    result.append(current_ip + segment)
                return

            # 剩餘字符不足以形成有效IP
            remaining = len(s) - start
            if remaining < (4 - dots) or remaining > (4 - dots) * 3:  # 4 - dots：還需要處理的段落數
                return

            # 嘗試放置點的位置
            for i in range(1, min(4, remaining + 1)):
                segment = s[start: start + i]
                if is_valid_segment(segment):
                    backtrack(start + i, dots + 1, current_ip + segment + '.')

        def is_valid_segment(segment: str) -> bool:
            # 空字串不合法
            if not segment:
                return False

            # 長度超過1且有前導零不合法
            if len(segment) > 1 and segment[0] == '0':
                return False

            # 數值範圍檢查
            return 0 <= int(segment) <= 255

        backtrack(0, 0, '')
        return result
