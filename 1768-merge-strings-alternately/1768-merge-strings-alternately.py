class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l=[]
        n=min(len(word1),len(word2))
        for i in range(n):
            l.append(word1[i])
            l.append(word2[i])

        if word1:
            for i in range(n,len(word1)):
                l.append(word1[i])
        
        if word2:
            for i in range(n,len(word2)):
                l.append(word2[i])

        return "".join(l)



            
        