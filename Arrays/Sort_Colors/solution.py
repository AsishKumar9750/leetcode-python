class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        c0=0
        c1=0
        c2=0
        index=0
        for i in nums:
            if i==0:
                c0+=1
            elif i==1:
                c1+=1
            else:
                c2+=1
        for i in range(0,c0):
            nums[index]=0
            index+=1
        for i in range(0,c1):
            nums[index]=1
            index+=1
        for i in range(0,c2):
            nums[index]=2
            index+=1