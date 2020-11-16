
# MERGE SORTED ARRAY
# Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

# Note:
# The number of elements initialized in nums1 and nums2 are m and n respectively.
# You may assume that nums1 has enough space(size that is equal to m + n) to hold additional elements from nums2.
# Example:

# Input:
# nums1 = [1, 2, 3, 0, 0, 0], m = 3
# nums2 = [2, 5, 6],          n = 3

# Output: [1, 2, 2, 3, 5, 6]


class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        # check edge cases: if valid sorted arrays one element array
        if n == 0:
            return

        # create position pointers
        p1 = 0
        p2 = 0

        # loop while ther is still space in num1 array
        while n > 0:

            # check index bounds
            if p1 < len(nums1) and p2 < len(nums2):
                # 1 num1 is less than num2
                if nums1[p1] < nums2[p2] and len(nums1)-p1 == n:
                    nums1[p1] = nums2[p2]
                    m -= 1  # update m and n
                    n -= 1
                    p2 += 1
                elif nums1[p1] < nums2[p2]:
                    p1 += 1

            # check index bounds
            if p1 < len(nums1) and p2 < len(nums2):
                # 2 num1 is equal to num2
                # 3 num1 is greater than num2
                if nums1[p1] >= nums2[p2]:
                    # add and increase pointer
                    nums1.insert(p1, nums2[p2])
                    p1 += 1
                    m -= 1  # update m size
                    n -= 1  # update n size
                    p2 += 1
                    nums1.pop()  # remove one zero
                elif len(nums1)-p1 != n:
                    p1 += 1

    # Time Complexity: O(n)
    # Space Complexity: O(n)
