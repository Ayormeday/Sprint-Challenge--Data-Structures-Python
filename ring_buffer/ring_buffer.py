from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        # while the buffer is not yet full, add item to the end and update the current
        if self.storage.length < self.capacity:
            self.storage.add_to_tail(item)
            self.current = self.storage.tail
        # if list is full?
        if self.storage.length == self.capacity:
            self.current.value = item
            # if the cureent value is at the tail, move to head
            if self.current is self.storage.tail:
                self.current = self.storage.head
            else:
                self.current = self.current.next


    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here
        node = self.storage.head
        while node is not None:
            list_buffer_contents.append(node.value)
            node = node.next
        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        self.storage = RingBuffer(capacity)
      
       
    def append(self, item):
        return self.storage.append(item)
        
    def get(self):
        return self.storage.get()