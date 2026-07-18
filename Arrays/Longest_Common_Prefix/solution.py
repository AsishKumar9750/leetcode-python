class Solution(object):
    def longestCommonPrefix(self, strs):
        n=len(strs)
        res=""
        base=strs[0]
        if n==0:
            return ""
        for i in range(0,len(base)):
            for word in strs[1:]:
                if i==len(word) or word[i]!=base[i]:
                    return res
            res+=base[i]
            
        return res
            
        