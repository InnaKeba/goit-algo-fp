class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = new_node

    def print_list(self):
        cur = self.head
        while cur:
            print(cur.data, end=" --> ")
            cur = cur.next
        print("None")

    def reverse(self):
        prev = None
        cur = self.head
        while cur:
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node
        self.head = prev

    def insertion_sort(self):
        sorted_head = None
        cur = self.head
        while cur:
            next_node = cur.next
            sorted_head = self._sorted_insert(sorted_head, cur)
            cur = next_node
        self.head = sorted_head

    def _sorted_insert(self, head, node):
        if not head or node.data < head.data:
            node.next = head
            return node
        cur = head
        while cur.next and cur.next.data < node.data:
            cur = cur.next
        node.next = cur.next
        cur.next = node
        return head

def merge_sorted_lists(list1, list2):
    dummy = Node(0)
    tail = dummy
    a = list1.head
    b = list2.head

    while a and b:
        if a.data < b.data:
            tail.next = a
            a = a.next
        else:
            tail.next = b
            b = b.next
        tail = tail.next

    tail.next = a if a else b

    merged_list = LinkedList()
    merged_list.head = dummy.next
    return merged_list

# Приклади
if __name__ == "__main__":
    l1 = LinkedList()
    for val in [7, 23, 9, 1, -5]:
        l1.append(val)
    print("Початковий список:")
    l1.print_list()

    l1.reverse()
    print("Реверсований список:")
    l1.print_list()

    l1.insertion_sort()
    print("Відсортований список:")
    l1.print_list()

    l2 = LinkedList()
    for val in [2, 4, 6]:
        l2.append(val)
    print("Другий відсортований список:")
    l2.print_list()

    merged = merge_sorted_lists(l1, l2)
    print("Об'єднаний відсортований список:")
    merged.print_list()