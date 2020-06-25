

# ------ REMOVE DUPLICATES FROM SORTED LIST -------- #
# Given a sorted linked list, delete all duplicates such that each element appear only once.

# Example 1:
    # Input: 1->1->2
    # Output: 1->2

# Example 2:
    # Input: 1->1->2->3->3
    # Output: 1->2->3

# -------  Personal Analysis --------- #
# Time Complexity: O(n)
# Space Complexity: O(1)

# -------  Leetcode Analysis --------- #
# 165 / 165 test cases passed.
# Status: Accepted
# Runtime: 24 ms, faster than 99.98 % of python3 submissions for Remove Duplicates from Sorted List. 
# Memory Usage: 12.8 MB.



# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        
        #edge cases when empty or only one element
        if head is None:
            return None
        
        curr = head.next
        prev = head
        
        while curr is not None:
            
            if curr.val == prev.val:
                prev.next = curr.next
                curr = curr.next
            else:
                curr = curr.next
                prev = prev.next
                
        return head


# By Josue Aranad
# # Python Solution