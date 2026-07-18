class Solution(object):
    def twoSum(self, nums, target):

 
        n=len(nums)
        hm={}
        for i in range(0,n):
            rem=target-nums[i]
            if rem in hm:
                return [hm[rem],i]
            else:
                hm[nums[i]]=i
            