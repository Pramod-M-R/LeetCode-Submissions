import heapq
class Solution:
    def kWeakestRows(self, mat: list[list[int]], k: int) -> list[int]:
        self.pq=[]
        self.sol=[]
        for i in range(len(mat)):
            count=0
            for j in range(len(mat[i])):
                if mat[i][j]==1:
                    count+=1
            heapq.heappush(self.pq,(count,i))

        for i in range (k):
            count,i=heapq.heappop(self.pq)
            self.sol.append(i)

        return self.sol


            
                

        