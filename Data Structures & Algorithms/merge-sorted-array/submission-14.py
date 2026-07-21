class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        l=m+n-1
        i=m-1
        j=n-1
        while j>=0 and i>=0:
            if nums1[i]>=nums2[j]:
                nums1[l]=nums1[i]
                l-=1
                i-=1
            elif nums2[j]>=nums1[i]:
                nums1[l]=nums2[j]
                l-=1
                j-=1
        if i<0:
            p=0
            for o in range(j+1):
                nums1[p]=nums2[o]
                p+=1



