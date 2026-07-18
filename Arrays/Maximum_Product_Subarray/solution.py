class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n=len(nums)
        prefix=1
        suffix=1
        maxi=max(nums)
        for i in range(0,n):
            prefix*=nums[i]
            suffix*=nums[n-i-1]
            maxi=max(prefix,maxi,suffix)
            if prefix==0:
                prefix=1
            elif suffix==0:

                suffix=1
        return maxi

