from typing import List
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:   
        freq = {}
        res = []
        for i in nums1:
            freq[i] = freq.get(i,0)+1
        for j in nums2:
            if (j in freq) and (freq[j]>0):
                freq[j] -= 1
                res.append(j)
        return res
    
    #def __main__
sol = Solution()
print(sol.intersect(nums1 = [1,2,2,1], nums2 = [2,2]))