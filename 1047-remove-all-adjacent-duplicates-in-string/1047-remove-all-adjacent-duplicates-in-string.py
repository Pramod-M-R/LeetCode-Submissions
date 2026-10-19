class Solution:
    def removeDuplicates(self, s: str) -> str:
        a=list(s)
        st=[]
        for i in a:
            if (st) and (st[-1]==i):
                st.pop()
            else:
                st.append(i)

        return "".join(st)

        




        