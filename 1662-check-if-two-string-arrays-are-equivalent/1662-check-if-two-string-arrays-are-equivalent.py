class Solution:
    def arrayStringsAreEqual(self, word1: list[str], word2: list[str]) -> bool:
        a=""
        for i in range(len(word1)):
            a+=word1[i]
        b=""
        for i in range(len(word2)):
            b+=word2[i]

        return a==b




        