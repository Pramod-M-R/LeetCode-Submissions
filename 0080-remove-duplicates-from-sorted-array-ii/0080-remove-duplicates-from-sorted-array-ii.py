class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        k=0
        for i in range(2,len(nums)):
            if nums[i]!=nums[k]:
                nums[k+2]=nums[i]
                k+=1
        return k+2