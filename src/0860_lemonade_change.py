from typing import List


class Solution:
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
