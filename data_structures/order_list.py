import threading

class LockFree:
    def __init__(self, initial_value):
        self._value = initial_value
        self._lock = threading.Lock()

    def compare_and_swap(self, expected, new_value):
        with self._lock:
            if self._value == expected:
                self._value = new_value
                return True
            return False

    def get(self):
        return self._value

class OrderNode:
    def __init__(self, quantity, price):
        self.quantity = quantity
        self.price = price
        self.next = LockFree(None)

class LockFreeOrderList:
    def __init__(self):
        self.head = LockFree(None)

    def add(self, quantity, price):
        new_node = OrderNode(quantity, price)
        while True:
            old_head = self.head.get()
            new_node.next = LockFree(old_head)
            if self.head.compare_and_swap(old_head, new_node):
                return

    def remove_head(self):
        while True:
            old_head = self.head.get()
            if old_head is None:
                return None
            new_head = old_head.next.get()
            if self.head.compare_and_swap(old_head, new_head):
                return old_head

    def peek(self):
        return self.head.get()


class BuyOrderList(LockFreeOrderList):
    def compare(self, node1, node2):
        # For buy orders, higher price has priority
        return node1.price > node2.price

class SellOrderList(LockFreeOrderList):
    def compare(self, node1, node2):
        # For sell orders, lower price has priority
        return node1.price < node2.price
