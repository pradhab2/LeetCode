"""
Given two strings s and t of lengths m and n respectively, return the
minimum window substring of s such that every character in t (including duplicates)
is included in the window. If there is no such substring, return the empty string "".
A substring is a contiguous sequence of characters within the string.

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.


Input: s = "aa", t= "aa"
Output: "aa"

Approach :
1. Find the first window that contains all letters in t;
2. Keep expanding the window to the right by 1 char at a time, reducing left side if possible.
Make sure that THE ACTIVE WINDOW ALWAYS CONTAINS ALL LETTERS IN t. In this case,
 every time the window is expanded, only the new char need to be checked.
i. create a lookup dictionary to check the ongoing window has every charaters and the count are matched.
ii. there would be two pointer, one is start and other is end, end pointer will keep on increasing till all the characters matched.
iii. Once all the charactes matched, we need to note it and then look for any other window has all charactes and has minimum length.
iv. count variable which is the desired match count ~ length of the lookup/dictionary.
v. when the count is 0 resister the result and look for other window by increasing start variable.
vi.return the window having minimum length
"""

from collections import Counter
def minWindow(s: str, t: str) -> str:
    lookup=Counter(t)
    mx=float('inf')
    start,end=0,0
    l=len(s)
    desired_count=len(lookup)   # to track the match count, initial value is the length of lookup
    res=""
    while end < l:
        while end < l and desired_count != 0:
            if s[end] in lookup:
                lookup[s[end]] -= 1
                if lookup[s[end]] == 0:
                    desired_count -= 1
            end += 1
        while start < end and desired_count == 0:
            if end-start < mx:
                mx =end-start
                res=s[start:end]
            if s[start] in lookup:
                lookup[s[start]] += 1
                if lookup[s[start]] > 0:
                    desired_count += 1
            start += 1

    return res

print(minWindow("ADOBECODEBANC", "ABC"))   # o/p "BANC"
print(minWindow("aa", "aa"))   # o/p "aa"
print(minWindow("abc", "ac"))   # o/p "abc"
print(minWindow("a", "b"))   # o/p ""


























"""inp=['ABCDE','DEBCD']"""
from collections import defaultdict

def find_three_combinations(inp):
    res= defaultdict(int)
    for item in inp:
        l=len(item)
        for i in range(l-2):
            res[item[i:i+3]]+=1
    return res

# print(find_three_combinations(['ABCDE','DECDE']))


def minWinSubstr(s):
    l=len(s)
    res=[]
    for end in range(l):
        for start in range(end):
            res.append(s[start:end+1])
    return res

# print(minWinSubstr('ABCDEF'))