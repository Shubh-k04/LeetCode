class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums3 = nums1+ nums2
        nums3.sort()
        l = len(nums3)
        if l%2==0:
            return float(nums3[(l/2)]+nums3[(l/2) - 1])/2
            
        else:
            return float(nums3[l//2])
        