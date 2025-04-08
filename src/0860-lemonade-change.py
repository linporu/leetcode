from typing import List


class Solution01:
    def lemonadeChange(self, bills: List[int]) -> bool:
        num_10_bill, num_5_bill = 0, 0
        num_customer = len(bills)
        idx_customer = 0

        while idx_customer < num_customer and num_5_bill >= 0 and num_10_bill >= 0:
            change = bills[idx_customer] - 5

            if change == 0:
                num_5_bill += 1

            elif change == 5:
                num_10_bill += 1
                num_5_bill -= 1
            else:  # change == 15
                if num_10_bill > 0:
                    num_10_bill -= 1
                    num_5_bill -= 1
                else:
                    num_5_bill -= 3

            idx_customer += 1

        return idx_customer == num_customer and num_5_bill >= 0 and num_10_bill >= 0


class Solution02:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five, ten = 0, 0  # 追蹤 5 元和 10 元紙鈔的數量

        for bill in bills:
            if bill == 5:
                five += 1
            elif bill == 10:
                if five == 0:  # 沒有 5 元紙鈔可找零
                    return False
                five -= 1
                ten += 1
            else:  # bill == 20
                if ten > 0 and five > 0:  # 優先使用 10+5 組合找零
                    ten -= 1
                    five -= 1
                elif five >= 3:  # 如果沒有 10 元，嘗試用三張 5 元找零
                    five -= 3
                else:  # 無法找零
                    return False

        return True
