"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.



Example:

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Note:

Although the above answer is in lexicographical order, your answer could be in any order you want.
"""


class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if "" == digits:
            return []
        d_map = {}
        d_map["1"]=[]
        d_map["2"] = ["a","b","c"]
        d_map["3"] = ["d","e","f"]
        d_map["4"] = ["g","h","i"]
        d_map["5"] = ["j","k","l"]
        d_map["6"] = ["m","n","o"]
        d_map["7"] = ["p","q","r","s"]
        d_map["8"] = ["t","u","v"]
        d_map["9"] = ["w","x","y","z"]

        all_letter = {}
        k = 0

        for digit in digits:
            all_letter[k]= d_map[digit]
            k += 1

        print(all_letter)
        result = [""]
        for i in range(len(all_letter)):
            butten = all_letter[i]
            while len(result[0]) == i:
                t = result.pop(0)
                for v in butten:
                    result.append(t+v)
        return result









s = Solution()
r = s.letterCombinations("23")
print(r)