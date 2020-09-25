class Deque:
    def __init__(self):
        self.deque = []

    def add_front(self, data):
        self.deque.append(data) # Append object to the end of the list

    def add_rear(self, data):
        self.deque.insert(0, data) # Insert object before index

    def is_empty(self):
        return self.deque == []

    def remove_rear(self):
        if self.is_empty():
            return "Empty Deque"
        else:
            return self.deque.pop(0) # Remove and return item at index (default last)

    def remove_front(self):
        if self.is_empty():
            return "Empty Deque"
        else:
            return self.deque.pop() # Remove and return item at index (default last)

    def size(self):
        return len(self.deque)

    def check_palindrome(self):
        is_palindrome = True
        while self.size() > 1 and is_palindrome:
            front = self.remove_front()
            rear = self.remove_rear()
            if front != rear:
                is_palindrome = False
        return is_palindrome


d_1 = Deque()
d_1.add_front("Dog")
d_1.add_rear("Cat")
d_1.add_rear("Mouse")

print(f"Front: {d_1.remove_front()}")
print(f"Front: {d_1.remove_rear()}")
print(f"Size: {d_1.size()}")
print(f"Rear: {d_1.remove_rear()}")
print(f"Rear: {d_1.remove_rear()}")

d_2 = Deque()
word = "racecar"
for i in word:
    d_2.add_rear(i)
print(f"Palindrome: {d_2.check_palindrome()}")