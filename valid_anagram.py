# ------ VALID ANAGRAM -------- #
# Given two strings s and t , write a function to determine if t is an anagram of s.

# Example 1:
    # Input: s = "anagram", t = "nagaram"
    # Output: true

# Example 2:
    # Input: s = "rat", t = "car"
    # Output: false

# -------  Personal Analysis --------- #
# Time Complexity: O(n)
# Space Complexity: O(n)

# -------  Leetcode Analysis --------- #
# 34 / 34 test cases passed.
# Status: Accepted
# Runtime: 48 ms, faster than 65.84% of Python3 online submissions for Valid Anagram.
# Memory Usage: 14 MB, less than 92.67% of Python3 online submissions for Valid Anagram.


def isAnagram(self, s: str, t: str) -> bool:
    # edge cases, check if given incorrect input
    # not an anagram is the length of the words are different.
    if s is None or t is None or len(s) != len(t):
        return False

    # dictionary to store count of characters
    alphabet = dict({})

    # Loop through the first word
    for char in s:
        # count each word and add it to container.
        if char not in alphabet:
            alphabet[char] = 1
        else:
            alphabet[char] += 1

    # Loop through the second word counting the characters.
        # check if character is not stored
        # else checck if character is not repeted the same amount of times.
        # else we decrement the count of the given char by one.
    for char2 in t:
        if char2 not in alphabet:
            return False
        elif alphabet[char2] < 1:
            return False
        else:
            alphabet[char2] -= 1

    return True


# By Josue Aranad
# # Python Solution