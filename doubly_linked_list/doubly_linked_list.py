"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
  after this node. Note that this node could already
  have a next node it is point to."""

    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
  before this node. Note that this node could already
  have a previous node it is point to."""

    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
  accordingly, effectively deleting this ListNode."""

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    def add_to_head(self, value):
        if self.head is None:
            node = ListNode(value)
            self.head = node
            self.tail = node
        else:
            self.head.insert_before(value)
            self.head = self.head.prev
        self.length += 1

    def remove_from_head(self):
        old_head = self.head
        if self.head is self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = old_head.next
        self.length -= 1
        return old_head.value

    def add_to_tail(self, value):
        if self.tail is None:
            node = ListNode(value)
            self.head = node
            self.tail = node
        else:
            self.tail.insert_after(value)
            self.tail = self.tail.next
        self.length += 1

    def remove_from_tail(self):
        old_tail = self.tail
        if self.head is self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail = old_tail.prev
        self.length -= 1
        return old_tail.value

    def move_to_front(self, node):
        if self.head is not self.tail:
            self.add_to_head(node.value)
            if self.tail == node:
                self.tail = self.tail.prev
            node.delete()
            self.length -= 1

    def move_to_end(self, node):
        if self.head is not self.tail:
            self.add_to_tail(node.value)
            if self.head is node:
                self.head = self.head.next
            node.delete()
            self.length -= 1

    def delete(self, node):
        if self.head is node:
            self.head = node.next
        if self.tail is node:
            self.tail = node.prev
        node.delete()
        self.length -= 1

    def get_max(self):
        curr_max = 0
        curr_node = self.head
        while curr_node is not None:
            curr_max = max(curr_node.value, curr_max)
            curr_node = curr_node.next
        return curr_max
