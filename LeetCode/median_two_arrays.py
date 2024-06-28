# 4. Median of Two Sorted Arrays
# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

# The overall run time complexity should be O(log (m+n)).

def findMedianSortedArrays(nums1: list[int], nums2: list[int]) -> float:
    for y in nums2:
        nums1.append(y)
    nums1.sort()
    if not len(nums1) % 2:
        i = len(nums1) // 2
        difference = (nums1[i] - nums1[i-1]) / 2
        result = nums1[i-1] + difference
        return result
    else:
        i = len(nums1) // 2
        return nums1[i]
     
        

# Example 1:

# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.

# Example 2:

# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

# Chiamate alle funzioni seguendo gli esempi forniti

# Esempio 1
nums1 = [1, 3]
nums2 = [2]
print(findMedianSortedArrays(nums1, nums2))  # Output atteso: 2.00000

# Esempio 2
nums1 = [1, 2]
nums2 = [3, 4]
print(findMedianSortedArrays(nums1, nums2))  # Output atteso: 2.50000