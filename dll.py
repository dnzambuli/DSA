class Node:
    def __init__(self, value):
        """
        Constructor for Node class for a doubly linked list
        :param value:
        """
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self, value = None):
        if value is None:
            self.head = None
            self.tail = None
            self.size = 0
        else:
            new_node = Node(value)
            self.head = new_node
            self.tail = new_node
            self.size = 1

    def __str__(self):
        string = ""
        current = self.head
        while current:
            string += str(current.value)
            current = current.next
        return string

    def __len__(self):
        return self.size

    def append(self, value):
        """
        append a value to the end of the dll
        :param value:
        :return:
        """
        # edge case: empty dll
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node

        # edge case: dll with content
        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node
        self.size += 1

# run the first test

test_empty = DoublyLinkedList()

print("empty dll: ", test_empty)

test_one_element = DoublyLinkedList(1)
print("one element dll: ", test_one_element)