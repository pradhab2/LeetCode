""" Medium
Given a string s, find the length of the longest substring without repeating characters.
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

 # Move the i pointer till we find the same chacter, j should be the start of the window
        # Keep on removing the charcters from set at j postion till s[i] found in the set
        # P W W K E W
        # j   i

This is a windowing problem

"""

def lengthOfLongestSubstring(s: str) -> int:
    st=set()
    max_ln=0
    j=0
    for i in range(len(s)):
        chr=s[i]
        while chr in st:
            st.remove(s[j])       # Here it removes s[j] not s[i] which is P and for W, it has to remove P then W
            j += 1
        st.add(chr)
        max_ln = max(max_ln,i-j+1)

    return max_ln

print(lengthOfLongestSubstring('PWWKEW'))
