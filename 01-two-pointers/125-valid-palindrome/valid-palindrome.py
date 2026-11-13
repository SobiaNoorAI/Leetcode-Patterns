class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        clean_list=[]
        for i in s:
            if i.isalnum():
                clean_list.append(i)
        j=0
        k=len(clean_list)-1

        while j<k:
            if clean_list[j]!=clean_list[k]:
                return False
            j+=1
            k-=1
        return True