class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #method 1: taking a new list and appending n-k elements from the back
        """n=len(nums)
        l=[0]*n    
        index=0
        k=k%n
        for i in range(0,k):
            l[index]=nums[n-k+index]
            index+=1
        for i in range(0,n-k):
            l[index]=nums[i]
            index+=1
        nums[:]=l[:]"""
        #method 2: reverse the whole list, nreak the list at k and reverse them again
         #for cases when k is larger than n, 
        n=len(nums)
        left=0
        right=n-1
        k=k%n
        while left<right:
            nums[left],nums[right]=nums[right],nums[left]
            left+=1
            right-=1
        nums[:k]=nums[:k][::-1]
        nums[k:]=nums[k:][::-1]



        
        

        