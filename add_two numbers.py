


# -------- ADD TOW NUMBERS (MEDIUM) -------- #
#You are given two non-empty linked lists representing two non-negative integers. 
# The digits are stored in reverse order and each of their nodes contain a single digit. 
# Add the two numbers and return it as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Example:

# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.


# ------------------------------ THE RIGHT WAY OF SOLVING THE PROBLEM (TECHNICAL) ------------------------------ #
# Explanation: You loop through booth lists at the same time, adding two values at the time and placing the sum value on a new list. 
# If the value is greater than 9, you will have to split the sum in to values: 1st value is the carry (like in normal sum)
# and 2nd value is the number to place as the sum. Ex: 12, you place 2 and carry 1. 
# The you get the 1st value by using the modulous (% and 10). e.g. 12 % 10 = 2
# The you get the carry by divide the sum by 10 and floor it or make it an integer. e.g. 12 % 10 = 1
# Then you just need to move the pointers to the next value if there is a next value in the list. 
# Note: When adding the correct value to the returning list, its best to create a "dummy" node will point to the beggining
# of the list as you add the values. At the end you will need to add the carry if it's greater than 1. 


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
    #variables to use: dummy(head of return list), pointer to list1, pointer to list2, current node and carry.
    dummy = ListNode()
    p1 = l1
    p2 = l2
    curr = dummy
    carry = 0 
    
    while p1 or p2:
        x = p1.val if p1 else 0
        y = p2.val if p2 else 0  
        
        # add p1 + p2 + carry
        temp_sum = x + y + carry
        
        # get carry if any ( num / 10 )
        carry = int(temp_sum/10)
        
        # get leading number ( num % 10 )
        curr.next = ListNode(temp_sum % 10)
        curr = curr.next
        
        if p1:
            p1 = p1.next
        if p2:
            p2 = p2.next
    
    if carry > 0:
        curr.next = ListNode(carry)
    
    return dummy.next

# -------  Personal Analysis --------- #
# Time Complexity: O(n)
# Space Complexity: O(n)

# -------  Leetcode Analysis --------- #
# 1563 / 1563 test cases passed.
# Status: Accepted
# Runtime: 96 ms, faster than 14.55% of Python3 online submissions for Add Two   Numbers.
# Memory Usage: 13.8 MB, less than 73.10% of Python3 online submissions for Add Two Numbers.


# ---------------------------------------------------------------------------------------------------------------





# ------------------------------ ANOTHER APPROACH OF SOLVING THE PROBLEM (NON TECHNICAL) ------------------------------ #
# Explanation: Use String to Integer conversion and vice versa to add the values. 
# First, we loop the each list and store the values in a string, using string lib function str()
# Second, reverse each string. You can do so by using [::-1] e,g. "hello"[::-1] = "olleh". 
# Third, add both numbers as integers, convert to string and reverse again. 
# Lastly, loop though sum string and add each character as a different list node. 

def addTwoNumbers2(self, l1: ListNode, l2: ListNode) -> ListNode:

    #edge cases, if list is empty 
    num1 = ""
    num2 = ""
    l3 = ListNode()

    #traverse each linked lists
    while l1:
        #convert each number in linked list to string char
        num1 += str(l1.val)
        l1 = l1.next;
    
    while l2:
        #convert each number in linked list to string char
        num2 += str(l2.val)
        l2 = l2.next;
    
    #To Return if both lists are empty 
    if num1 == "" and num2 == "":
        return l1
    
    one = 0
    two = 0
    # Reverse the strings and save value as int
    if l1 is None and num1 != "":
        one = int(num1[::-1]) 
    if l2 is None and num2 != "":
        two = int(num2[::-1])
        
    #add both values. 
    sum = one + two
    #reverse the sum 
    sum = str(sum)[::-1]
    #dummy that points to the beginning of the list.
    dummy = l3
    #add each char to the list separately.
    for n in sum:
        l3.next = ListNode(int(n))
        l3 = l3.next
        
    return dummy.next

# 1563 / 1563 test cases passed.
# Status: Accepted
# Runtime: 84 ms, faster than 24.00 % of python3 submissions.
# Memory Usage: 13.9 MB, less than 44.53 % of python3 submissions

# By Josue Aranad
# # Python Solution