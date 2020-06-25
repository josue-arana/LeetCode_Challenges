

# ------ MAYORITY ELEMENT -------- #
# Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

# You may assume that the array is non-empty and the majority element always exist in the array.

# Example 1:
    # Input: [3,2,3]
    # Output: 3

# Example 2:
    # Input: [2,2,1,1,1,2,2]
    # Output: 2

# -------  Personal Analysis --------- #
# Time Complexity: O(n)
# Space Complexity: O(n)

# -------  Leetcode Analysis --------- #
# 46 / 46 test cases passed.
# Status: Accepted
# Runtime: 180 ms, faster than 46.27 % of python3 submissions for Mayority Element. 
# Memory Usage: 15.1 MB, less than 75.23 % of python3 submissions for Mayority Element.

def majorityElement(self, nums: List[int]) -> int:
    #HashMap Approach
    
    #Create a hash map where key= number and value=#of appearances.
    elements = dict({})
    
    #majority flag
    flag = len(nums)/2
    majority = nums[0]
    
    #Loop though elements saving them in hash map and also checking if values is greater than n/2
    for num in nums:
        
        #check if element is in hash and if it's more than majority flag
        if num in elements:
            elements[num] = elements[num]+1
            
            if elements[num] > flag:
                return num
        else:
            #add element to hash
            elements[num] = 1
                
    return majority


# By Josue Aranad
# # Python Solution