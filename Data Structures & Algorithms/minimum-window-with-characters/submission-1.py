
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need=defaultdict(int)
        window=defaultdict(int)
        for c in t: 
            need[c]+=1
        formed=0
        required=len(t)
        left=0
        best=len(s)+20
        res=''
        for right,c in enumerate(s): 
            window[c]+=1
            if window[c]<=need[c]: 
                formed+=1
            while formed==required : 
                if right-left+1<best: 
                    best=right-left+1
                    res=s[left:right+1]
                window[s[left]]-=1
                if window[s[left]]<need[s[left]]: 
                    formed -=1
                if window[s[left]]==0: 
                    del window[s[left]]
                left+=1
           
        return res
            
