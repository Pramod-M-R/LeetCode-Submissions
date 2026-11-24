class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        c=1
        can=nums[0]
        for i in range(1,len(nums)):
            if nums[i]==can:
                c+=1
            else:
                c-=1
            if c==0:
                can=nums[i]
                c=1

        return can
