'''
Implement the following operations of a queue using stacks.

push(x) -- Push element x to the back of queue.
pop() -- Removes the element from in front of queue.
peek() -- Get the front element.
empty() -- Return whether the queue is empty.
Example:

MyQueue queue = new MyQueue();

queue.push(1);
queue.push(2);
queue.peek();  // returns 1
queue.pop();   // returns 1
queue.empty(); // returns false
Notes:

You must use only standard operations of a stack -- which means only push to top, peek/pop from top, size, and is empty operations are valid.
Depending on your language, stack may not be supported natively. You may simulate a stack by using a list or deque (double-ended queue), as long as you use only standard operations of a stack.
You may assume that all operations are valid (for example, no pop or peek operations will be called on an empty queue).
'''


class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        self.stack.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if not self.empty():
            a = self.stack[0]
            self.stack.remove(a)
            return a


        return a


    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if not self.empty():
            return self.stack[0]


    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        if len(self.stack) ==0:
            return True
        else:
            return False


obj = MyQueue()
obj.push(1)
obj.push(2)
print('push stack',obj.stack)


param_3 = obj.peek()
print(param_3)
print('peek stack',obj.stack)


param_2 = obj.pop()
print(param_2)
print('pop stack',obj.stack)




param_4 = obj.empty()
print('stack',obj.stack)
