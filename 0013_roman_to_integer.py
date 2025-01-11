class Solution:
    def romanToInt(self, s: str) -> int:
        symbol = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        list = [char for char in s]

        value = 0

        for i in range(len(list) - 1):
            if list[i] == "I" and (list[i + 1] == "V" or list[i + 1] == "X"):
                value -= 1
            elif list[i] == "X" and (list[i + 1] == "L" or list[i + 1] == "C"):
                value -= 10
            elif list[i] == "C" and (list[i + 1] == "D" or list[i + 1] == "M"):
                value -= 100
            else:
                value += symbol[list[i]]

        value += symbol[list[len(list) - 1]]

        return value
