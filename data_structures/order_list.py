class OrderNode:
    def __init__(self, quantity, price):
        self.quantity = quantity
        self.price = price
        self.next = None

class OrderList:
    def __init__(self):
        self.head = None

    def add(self, quantity, price):
        new_node = OrderNode(quantity, price)
        if self.head is None or self.compare(new_node, self.head):
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next and not self.compare(new_node, current.next):
                current = current.next
            new_node.next = current.next
            current.next = new_node

    def remove_head(self):
        if self.head:
            removed = self.head
            self.head = self.head.next
            return removed
        return None

    def peek(self):
        return self.head

class BuyOrderList(OrderList):
    def compare(self, node1, node2):
        # For buy orders, higher price has priority
        return node1.price > node2.price

class SellOrderList(OrderList):
    def compare(self, node1, node2):
        # For sell orders, lower price has priority
        return node1.price < node2.price
