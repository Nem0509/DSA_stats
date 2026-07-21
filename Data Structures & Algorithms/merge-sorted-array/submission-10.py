class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i=0
        j=0
        if n>0:
            while i<m:
                if nums1[i] <= nums2[j]:
                    i+=1
                elif nums1[i] > nums2[j]:
                    nums1[i],nums2[j]=nums2[j],nums1[i]
                    for k in range(0,n-1):
                        if nums2[k]>=nums2[k+1]:
                            nums2[k],nums2[k+1]=nums2[k+1],nums2[k]
                        else:
                            break   
                    i+=1
            for o in nums2:
                nums1[m]=o
                m+=1