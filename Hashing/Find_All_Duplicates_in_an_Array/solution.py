class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        n=len(nums)
        hm={}
        for i in nums:
            if i in hm:
                hm[i]+=1
            else:
                hm[i]=1
        keys = []

        for k, v in hm.items():
            if v == 2:
                keys.append(k)
        return keys
