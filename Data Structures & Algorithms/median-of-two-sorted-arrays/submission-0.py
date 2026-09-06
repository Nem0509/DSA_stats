class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        rs=nums1+nums2
        rs.sort()
        print(rs)
        if len(rs)%2==0:
            return (rs[len(rs)//2]+rs[len(rs)//2-1])/2
        return rs[len(rs)//2]