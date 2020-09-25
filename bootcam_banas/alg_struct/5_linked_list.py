class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def get_data(self):
        return self.data

    def set_data(self, new_data):
        self.data = new_data

    def set_next(self, new_next):
        self.next = new_next

    def get_next(self):
        return self.next


class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def add(self, data):
        # 1. Create a new node and assigned data
        # 2. Set next as thge previuos head node
        # 3. Make the new node the lists new head node
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node

    def remove(self, search_value):
        # 1. Start at the head node
        # 2. Check if it has the data we are searching for
        # 3. If not search the next node
        # 4. Repeat as long an nodes exist
        current_node = self.head
        prev_node = None
        data_found = False
        while not data_found:
            if current_node.get_data() == search_value:
                data_found = True
            else:
                prev_node = current_node
                current_node = prev_node.get_next()
        if prev_node is None:
            self.head = current_node.get_next()
        else:
            prev_node.set_next(current_node.get_next())

    def length(self):
        current_node = self.head
        total_nodes = 0
        while current_node is not None:
            total_nodes += 1
            current_node = current_node.get_next()
        return total_nodes

    def search(self, search_value):
        current_node = self.head
        data_found = False
        while current_node is not None and not data_found:
            if current_node.get_data() == search_value:
                data_found = True
            else:
                current_node = current_node.get_next()
        return data_found


ll = LinkedList()
ll.add(1)
ll.add(2)
print(f"Lenght : {ll.length()}")
print(f"Search 1 : {ll.search(1)}")
ll.remove(1)
print(f"Lenght : {ll.length()}")
print(f"Search 1 : {ll.search(1)}")
