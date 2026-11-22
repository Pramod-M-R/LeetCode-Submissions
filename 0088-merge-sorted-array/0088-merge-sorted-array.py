class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        j=n-1
        k=m+n-1
        while j>=0:
            nums1[k]=nums2[j]
            j-=1
            k-=1

        nums1.sort()
                