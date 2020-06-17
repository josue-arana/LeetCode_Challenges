# Implement a Stack using a single Queue
class MyStack:
     
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = MyQueue()
        

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.queue.enqueue(x)
        
        rotations = self.queue.size()-1
        
        for i in range(0,rotations):
            self.queue.enqueue(self.queue.dequeue())
            

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.queue.dequeue()
        

    def top(self) -> int:
        """
        Get the top element.
        """
        
        return self.queue.peek()
        

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return self.queue.isEmpty()
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()


class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = []

    def enqueue(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.queue.append(x)
        

    def dequeue(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        return self.queue.pop(0)
        

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.queue[0]
        

    def isEmpty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return self.queue==[]
    
    def size(self) -> int:
        return len(self.queue)