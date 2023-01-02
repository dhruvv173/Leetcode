class MyStack:

    def __init__(self):
        self.queue = deque()                   #initialize the data structure

    def push(self, x: int) -> None:
        self.queue.append(x)                    #adds the element to the queue

    def pop(self) -> int:
        for i in range(len(self.queue) - 1):
            self.push(self.queue.popleft())
        return self.queue.popleft()

    def top(self) -> int:
        return self.queue[-1]                   #returns the most recent element added

    def empty(self) -> bool:
        return len(self.queue) == 0                       #returns T if length  is zero or else false
