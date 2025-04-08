class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dict_magazine = {f"{c}": 0 for c in "abcdefghijklmnopqrstuvwxyz"}
        dict_ransomNote = {f"{c}": 0 for c in "abcdefghijklmnopqrstuvwxyz"}

        for c in magazine:
            dict_magazine[f"{c}"] += 1

        for c in ransomNote:
            dict_ransomNote[f"{c}"] += 1

        for key in dict_magazine.keys():
            if dict_magazine[key] >= dict_ransomNote[key]:
                continue
            else:
                return False
        return True
