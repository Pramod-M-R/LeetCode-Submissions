class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        i=0
        j=0
        start1=0
        start2=0
        while i<len(version1) or j<len(version2):
            revision1 = 0
            revision2 = 0
            if i < len(version1):
                while i < len(version1) and version1[i] != ".":
                    i += 1

                revision1 = int(version1[start1:i])

                if i < len(version1):
                    i += 1

                start1 = i

            if j < len(version2):
                while j < len(version2) and version2[j] != ".":
                    j += 1

                revision2 = int(version2[start2:j])

                if j < len(version2):
                    j += 1

                start2 = j
                
            if revision1==revision2:
                continue
            elif revision1<revision2:
                return -1
            elif revision1>revision2:
                return 1
            
        return 0
            


        
            

        