import time


class Stack:
    def __init__(self):
        #FILO First-in, last-out
        self.stack = []

    def push(self, data):
        self.stack.insert(0, data)

    def is_empty(self):
        return self.stack == []

    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        return self.stack.pop(0) # Remove and return item at index (default last).

    def peek(self):
        return self.stack[0]

    def size(self):
        return len(self.stack)

    def reverse_string(self):
        while True:
            if len(self.stack) == 0:
                break
            else:
                print(self.stack.pop(0), end="")


s_1 = Stack()
s_1.push("Cat")
s_1.push("Dog")
print(s_1.size())
# print(s_1.peek())
print(s_1.pop())
print(s_1.pop())

s_1.push("C")
s_1.push("a")
s_1.push("t")
s_1.reverse_string()
print()
print("*"*79)

#################################################
# FIFO - QUEUES
class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, data):
        self.queue.insert(0, data)

    def is_empty(self):
        return self.queue == []

    def dequeue(self):
        if self.is_empty():
            return "Empty Queue"
        return self.queue.pop() # Remove and return item at index (default last).

    def peek(self):
        return self.queue[0]

    def size(self):
        return len(self.queue)

    def wait_your_turn(self):
        while True:
            if len(self.queue) == 0:
                break
            else:
                print(f"{self.dequeue()} takes their turn")
                time.sleep(3)

q_1 = Queue()
q_1.enqueue("Cat")
q_1.enqueue("Dog")
q_1.wait_your_turn()

q_1.enqueue("Cat")
q_1.enqueue("Dog")
print(q_1.size())
# print(q_1.peek())
print(q_1.dequeue())
print(q_1.dequeue())
print(q_1.dequeue())
