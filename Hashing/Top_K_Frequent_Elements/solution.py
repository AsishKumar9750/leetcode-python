class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''n=len(nums)
        hm={}
        for i in nums:
            if i in hm:
                hm[i]+=1   #hash map
            else:
                hm[i]=1
        items=list(hm.items())
        items.sort(key=lambda x:x[1],reverse=True)
        l=[]
        for i in range(0,k):
            l.append(items[i][0])
        return l'''
        hm={}
        n=len(nums)
        if n==1:
            return [nums[0]]
        for key in nums:
            if key in hm:
                hm[key]+=1   #bucket sort
            else:
                hm[key]=1
        bucket=[]
        ans=[]
        for i in range(0,len(nums)+1):
            bucket.append([])
        for key,value in hm.items():
            bucket[value].append(key)
        for i in range(n,0,-1):
            for j in bucket[i]:
                    ans.append(j)
                    if len(ans)==k:
                        return ans



            


        

