class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hm={}
        for i in nums:
            if i in hm:
                hm[i]+=1
            else:
                hm[i]=1
            if hm[i]>len(nums)//2:
                return i