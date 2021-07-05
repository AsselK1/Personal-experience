class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        hs1 = {}
        for i in range(len(s1)):
            hs1[s1[i]] = hs1.get(s1[i],0)+1        
        l=0
        r=len(s1)-1
        hs2 = {}
        for i in range(l,r+1):
            hs2[s2[i]] = hs2.get(s2[i],0)+1
        while r<len(s2):
            k=0
            for i in range(l,r+1):
                if hs1[s2[i]]!=hs2[s2[i]]:
                    break
                else:
                    k+=1
            if k==len(s1):
                print(hs2)
                return True
            if r==len(s2)-1:
                return False
            hs2[s2[l]]-=1
            l+=1
            r+=1
            hs2[s2[r]] = hs2.get(s2[r],0)+1
        return False