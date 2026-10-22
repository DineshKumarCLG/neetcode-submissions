class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # char_set=set(s)
        # res=0

        # for c in char_set:
        #     count=left=0
        #     for right in range(len(s)):
        #         if s[right]==c:
        #             count+=1
        #         while (right-left+1)-count>k:
        #             if s[left]==c:
        #                 count-=1
        #             left+=1
        #         res=max(res,right-left+1)
        # return res
        count={}
        l=0
        res=0
        maxf=0
        for r in range(len(s)):
            count[s[r]]=1+count.get(s[r],0)
            maxf=max(maxf, count[s[r]])
            while (r-l+1)-maxf>k:
                count[s[l]]-=1
                l+=1
            res=max(res,r-l+1)
        return res