from collections import deque
class FrontMiddleBackQueue:

    def __init__(self):
        self.q=deque()
        
    def pushFront(self, val: int) -> None:
        self.q.appendleft(val)
        
    def pushMiddle(self, val: int) -> None:
        l=list(self.q)
        n=len(l)
        l.insert(n//2 , val)
        self.q=deque(l)

    def pushBack(self, val: int) -> None:
        self.q.append(val)
        
    def popFront(self) -> int:
        if self.q:
            a=self.q.popleft()
            return a

        else:
            return -1

    def popMiddle(self) -> int:
        if self.q:
            l=list(self.q)
            n=len(l)
            c=l.pop((n-1)//2)
            self.q=deque(l)
            return c

        else:
            return -1
        
    def popBack(self) -> int:
        if self.q:
            b=self.q.pop()
            return b

        else:
            return -1
        


# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()