import heapq
class Solution:
    def kSmallestPairs(self, nums1: list[int], nums2: list[int], k: int) -> list[list[int]]:
        heap=[]
        for i in range(min(k,len(nums1))):
            j=0
            s=nums1[i]+nums2[j]
            heapq.heappush(heap,(s,i,j))

        result=[]
        for _ in range(k):
            if not heap:
                break

            s,i,j=heapq.heappop(heap)
            result.append([nums1[i],nums2[j]])

            j+=1

            if j<len(nums2):
                s=nums1[i]+nums2[j]
                heapq.heappush(heap,(s,i,j))

        return result




        

        

        