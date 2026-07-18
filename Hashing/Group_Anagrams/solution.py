class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''hm={}
        for value in strs:
            key=''.join(sorted(value))
            if key in hm:
                hm[key].append(value)
            else:
                hm[key]=[value]
        
        return list(hm.values())
        '''
        if len(strs)==0:
            return []
        hm={}
        for word in strs:
            l=[0]*26
            for ch in word:
                l[ord(ch)-ord('a')]+=1
            key=tuple(l)
            if key in hm:
                hm[key].append(word)
            else:
                hm[key]=[word]
        return list(hm.values())
            