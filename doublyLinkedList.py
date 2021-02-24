class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        
    def append(self, data):
        if self.head == None:
            new_node = Node(data)
            new_node.prev = None
            self.head = new_node
            # self.head.next = None
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            new_node = Node(data)
            new_node.prev = cur
            cur.next = new_node
            new_node.next = None
                
    def prepend(self, data):
        if self.head == None:
            new_node = Node(data)
            new_node.prev = None
            self.head = new_node
        else:
            new_node = Node(data)
            self.head.prev = new_node
            new_node.next = self.head
            new_node.prev = None
            self.head = new_node
            
    def add_node_after(self, key, node):
        cur = self.head
        while cur:
            if cur.next is None and cur.data == key:
                self.append(node)
                return
            elif cur.data == key:
                new_node = Node(node)
                next_node = cur.next
                cur.next = new_node
                new_node.prev = cur
                new_node.next = next_node
                next_node.prev = new_node
            cur = cur.next
    
    def add_node_before(self, key, node):
        cur = self.head
        while cur:
            if cur.prev is None and cur.data == key:
                self.prepend(node)
                return
            elif cur.data == key:
                new_node = Node(node)
                prev_node = cur.prev
                prev_node.next = new_node
                new_node.next = cur
                new_node.prev = prev_node
            cur = cur.next
            
    def delete(self, key):
        cur = self.head
        while cur:
            if cur.data == key and cur == self.head:
                if not cur.next:
                    cur = None
                    self.head = None
                    return
                else:
                    nxt = cur.next
                    cur.next = None
                    cur = None
                    nxt.prev = None
                    self.head = nxt
                    return
            elif cur.data == key:
                if cur.next:
                    nxt = cur.next
                    prev = cur.prev
                    prev.next = nxt
                    nxt.prev = prev
                    cur.next = None
                    cur.prev = None
                    cur = None
                    return
                else:
                    if cur.next == None:
                        prev = cur.prev
                        prev.next = None
                        cur.prev = None
                        cur = None
                        return
            cur = cur.next

    def reverse(self):
        tmp = None
        cur = self.head
        while cur:
            tmp = cur.prev 
            cur.prev = cur.next
            cur.next = tmp
            cur = cur.prev
        if tmp:
            self.head = tmp.prev
    
    def delete_node(self, node):
        cur = self.head
        while cur:
            if cur == node and cur == self.head:
                if not cur.next:
                    cur = None
                    self.head = None
                    return
                else:
                    nxt = cur.next
                    cur.next = None
                    cur = None
                    nxt.prev = None
                    self.head = nxt
                    return
            elif cur == node:
                if cur.next:
                    nxt = cur.next
                    prev = cur.prev
                    prev.next = nxt
                    nxt.prev = prev
                    cur.next = None
                    cur.prev = None
                    cur = None
                    return
                else:
                    if cur.next == None:
                        prev = cur.prev
                        prev.next = None
                        cur.prev = None
                        cur = None
                        return
            cur = cur.next

            
    def remove_duplicated(self):
        cur = self.head
        seen = dict()
        while cur:
            if cur.data not in seen:
                seen[cur.data] = 1
                cur = cur.next
            else:
                nxt = cur.next
                self.delete_node(cur)
                cur = nxt
        
    def pairs_with_sum(self, num):
        pairs = list()
        cur = self.head
        q = None
        while cur:
            q = cur.next
            while q:
                if cur.data + q.data == num:
                    pairs.append("(" + str(cur.data) + "," + str(q.data) + ")")
                q = q.next
            cur = cur.next
        return pairs
            
    def print_list(self):
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next
    
dllist = DoublyLinkedList()
dllist.append(1)
dllist.append(2)
# dllist.append(4)

# dllist.append(4)
dllist.append(3)
# dllist.append(1)
# dllist.append(7)
dllist.append(4)
dllist.append(5)
print(dllist.pairs_with_sum(5))


# dllist.reverse()
# dllist.remove_duplicated()
# dllist.prepend(5)
# dllist.add_node_before(4, 6)
# dllist.delete(4)
dllist.print_list()