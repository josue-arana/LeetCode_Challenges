


# -------- REVERSE STRING (EASY) -------- #
# Write a function that reverses a string. The input string is given as an array of characters char[].

# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

# You may assume all the characters consist of printable ascii characters.

 

# Example 1:

# Input: ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]
# Example 2:

# Input: ["H","a","n","n","a","h"]
# Output: ["h","a","n","n","a","H"]


# ------------------------------ TWO POINTER APPROACH ------------------------------ #
# Explanation: we use two pointers that to sway values as we iterate through the list
# the first pointer is at the beginning and the other at the end. 
# the number of times we iterate is half the size of the list. 
# we increment and decrement the position of the pointer as we go. 

class Solution:
    def reverseString(self, s: List[str]) -> None:
        
        #two pointer approach
        if s is None or s == []:
            return 
        
        start = 0
        end   = len(s)-1
        num_swaps = int(len(s)/2)
        
        for i in range(0, num_swaps):
            temp = s[start]
            s[start] = s[end]
            s[end] = temp
            
            start +=1
            end   -=1

# -------  Personal Analysis --------- #
# Time Complexity: O(n)
# Space Complexity: O(1)

# -------  Leetcode Analysis --------- #
# 478 / 478 test cases passed.
# Status: Accepted
# Runtime: 216 ms, faster than 51.83% of Python3 online submissions for Reverse String.
# Memory Usage: 18.2 MB, less than 75.44% of Python3 online submissions for Reverse String.



# ------------------------------ ANOTHER APPROACH OF SOLVING THE PROBLEM (PYTHON LIBRARY) ------------------------------ #
class Solution:
    def reverseString(self, s: List[str]) -> None:
        #use python library 
        s.reverse()

# 478 / 478 test cases passed.
# Status: Accepted
# Runtime: 204 ms, faster than 92.46 % of python3 submissions.
# Memory Usage: 18.2 MB, less than 75.44 % of python3 submissions.

# By Josue Aranad
# # Python Solution