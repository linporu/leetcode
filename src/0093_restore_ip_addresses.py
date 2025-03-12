from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:

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
