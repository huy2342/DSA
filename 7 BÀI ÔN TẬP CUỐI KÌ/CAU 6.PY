class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)

a.next = b
b.next = c
c.next = d
d.next = e
e.next = c

slow = a
fast = a

while fast and fast.next:
    slow = slow.next
    fast = fast.next.next

    if slow == fast:
        break

slow = a

while slow != fast:
    slow = slow.next
    fast = fast.next

print(slow.data)