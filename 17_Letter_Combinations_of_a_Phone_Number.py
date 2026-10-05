"""Using DFS """
""" Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
dictionary = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
Example 2:

Input: digits = "2"
Output: ["a","b","c"]

"""
from typing import List

class Solution(object):
    def letterCombinations(self, digits): # Simple way of cross join
        """
        :type digits: str
        :rtype: List[str]
        """
        dictionary = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        if digits == "":
            return []
        start=list(dictionary[digits[0]])

        for digit in digits[1:]:
            start = [i+j for i in start for j in dictionary[digit]]
        return start

    # clear expanded version of the iterative method

    def letterCombinations1(self, digits):
        dictionary = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        if digits == "":
            return []
        combo=list(dictionary[digits[0]])
        for digit in digits[1:]:
            int_combo = []
            for elm in combo:
                for chr in dictionary[digit]:
                    int_combo.append(elm + chr)
            combo = int_combo
        return combo

# DFS recursion

    def letterCombinations2(self, digits: str) -> [str]:

        # result = []
        phone_dict = {'2': 'abc', '3': 'def', '4': 'ghi',
                      '5': 'jkl', '6': 'mno', '7': 'pqrs',
                      '8': 'tuv', '9': 'wxyz'}

        def dfs(curr_string, left_over_digits,result):
            if left_over_digits == '':
                result.append(curr_string)
                return
            else:
                for char in phone_dict[left_over_digits[0]]:
                    dfs(curr_string + char, left_over_digits[1:], result)

        if not digits:
            return []
        else:
            result=[]
            dfs('', digits,result)
        return result


# Google DFS way ( Recommended )

    def letterCombinations4(self, digits: str) -> List[str]:
        if not digits:
            return []

        # Map digits to their corresponding letters
        phone_map = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }

        result = []

        # DFS/backtracking helper function
        def dfs(index: int, current_path: List[str]):
            # Base case: if the path length equals digits length, a combination is complete
            if index == len(digits):
                result.append("".join(current_path))
                return

            # Get letters for the current digit
            current_digit = digits[index]
            letters = phone_map[current_digit]

            # Explore each letter (DFS branch)
            for letter in letters:
                current_path.append(letter)  # Choose
                dfs(index + 1, current_path)  # Explore
                current_path.pop()  # Unchoose (Backtrack)

        # Start DFS from the first digit with an empty path
        dfs(0, [])
        return result
    """ How the Algorithm WorksThe Map: 
    A dictionary links each string digit to its specific cluster of letters.
    The Index: Track your current position in the input digits string.
    The Base Case: When index equals the length of digits, you hit a leaf node.
    The Backtracking: current_path.pop() cleans up the last letter so the next loop iteration can try a new letter branch. 
    Complexity AnalysisTime Complexity: O(4^N * N). N is the number of digits.
     4 is the maximum number of letters mapped to a digit (like 7 and 9). 
     The extra N comes from building the final string.Space Complexity: O(N) 
    The recursion stack depth matches the length of the input digits."""

aa = Solution()
print(aa.letterCombinations('23'))  #res: ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']
# print(aa.letterCombinations1('23'))  #res: ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']
# print(aa.letterCombinations4('234'))  #res: ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']
# print(aa.letterCombinations2('23'))  #res: ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']
# print(aa.letterCombinations('253'))  # ['ajd', 'aje', 'ajf', 'akd', 'ake', 'akf', 'ald', 'ale', 'alf', 'bjd', 'bje', 'bjf', 'bkd', 'bke', 'bkf', 'bld', 'ble', 'blf', 'cjd', 'cje', 'cjf', 'ckd', 'cke', 'ckf', 'cld', 'cle', 'clf']



"""  Complexity Analysis
letterCombinations (lines 19-31)
Time Complexity: O(n × m^n)
n = number of digits in the input
m = average number of letters per digit (max is 4 for digits 7 and 9)
The loop runs n-1 times (line 29)
In each iteration, the list comprehension (line 30) creates new combinations by multiplying existing combinations with new letters
After iteration i, the list has size m^i, and we generate m^i × m = m^(i+1) new combinations
The final result has m^n combinations, and creating all of them takes O(n × m^n) time
Space Complexity: O(m^n)
The result list grows to store all m^n combinations
Each combination string can be up to n characters long
Total space for output: O(n × m^n), but we typically count the output space separately, so O(m^n) for the main data structure
 
letterCombinations2 (lines 34-54)
Time Complexity: O(n × m^n)
n = number of digits, m = average letters per digit
The DFS explores all possible paths in the recursion tree
The recursion tree has depth n and each node branches into up to m children
Total nodes in tree: m^n
At each node, we perform string concatenation curr_string + char which takes O(n) time (strings are immutable in Python)
Total: O(n × m^n)
Space Complexity: O(n + m^n)
Recursion call stack depth: O(n) (at most n levels deep)
Output list storing m^n combinations: O(m^n)
String concatenation at each level creates intermediate strings: O(n) for each recursive call
Total: O(n × m^n) when accounting for all intermediate strings created during concatenation
 
Summary Table
Aspect
letterCombinations
letterCombinations2
Time
O(n × m^n)
O(n × m^n)
Space
O(m^n)
O(n × m^n)
Key Difference: letterCombinations2 has worse space complexity due to repeated string concatenation in the recursive calls, which creates many temporary strings of varying lengths (O(n) per concatenation). The first approach builds the strings more efficiently through list comprehension."""