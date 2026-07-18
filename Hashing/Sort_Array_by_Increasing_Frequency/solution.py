class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        hm={}
        for i in nums:
            if i in hm:
                hm[i]+=1
            else:
                hm[i]=1
        items=list(hm.items())
        items.sort(key=lambda x:x[0], reverse=True) #sort by value of number-descending
        items.sort(key=lambda x:x[1]) #sort by frequency ascending
        l=[]
        for k,v in items:
            for i in range(v):
                l.append(k)
        return l
            