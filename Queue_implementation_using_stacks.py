
# ------ QUEUE IMPLEMENTATION USING TWO STACKS -------- #
# By Josue Arana
# Python Solution

class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack1 = MyStack()
        self.stack2 = MyStack()

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.stack1.push(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        #If the second stack is empty then we move all the elements from
        #stack1 to stack2 and then pop. 
        if self.stack2.isEmpty():
            #Reverse the stack1 ans save it into stack2
            for i in range(0, self.stack1.size()):
                self.stack2.push(self.stack1.pop())
        
        #if stack2 is not empty, we just pop the last element.
        return self.stack2.pop()
        

    def peek(self) -> int:
        """
        Get the front element.
        """
        #If the second stack is empty then we move all the elements from
        #stack1 to stack2 and then pop. 
        if self.stack2.isEmpty():
            #Reverse the stack1 ans save it into stack2
            for i in range(0, self.stack1.size()):
                self.stack2.push(self.stack1.pop())
        
        #if stack2 is not empty, we just pop the last element.
        return self.stack2.top()

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return self.stack1.isEmpty() and self.stack2.isEmpty()
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

### This is an implementation of a Stack using arrays ###
class MyStack:
     
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = []
        

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.stack.append(x)
            

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.stack.pop()
        

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.stack[len(self.stack)-1]
        

    def isEmpty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return self.stack == []
    
    def size(self) -> int:
        """
        Returns the size of the stack
        """
        return len(self.stack)
        

