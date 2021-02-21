class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None
        
    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next
        
    def append(self, data):
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            return
        
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node  
    
    def prepend(self, data):
        new_node = Node(data)
        
        new_node.next = self.head
        self.head = new_node
    
    def insert_after_node(self, prev_node, data):
        if not prev_node:
            print("No such node in the linked list")
        
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node
        
    def swap_nodes(self, key_1, key_2):
        if key_1 == key_2:
            return
        prev_1 = None
        curr_1=self.head
        while curr_1 and curr_1.data != key_1:
            prev_1 = curr_1
            curr_1 = curr_1.next
        
        prev_2 = None
        curr_2 =self.head
        while curr_2 and curr_2.data != key_2:
            prev_2 = curr_2
            curr_2 = curr_2.next
        
        if not curr_1 or not curr_2:
            return 
        
        if prev_1:
            prev_1.next=curr_2
        else:
            self.head = curr_2
            
        if prev_2:
            prev_2.next = curr_1
        else:
            self.head = curr_1
            
        curr_1.next, curr_2.next = curr_2.next, curr_1.next
            
            
    def length_iterative(self):
        x = 0
        cur_node = self.head
        while cur_node:            
            cur_node = cur_node.next
            x = x + 1
        return x
    
    def length_recursive(self, node):
        if node is None:
            return 0
        return 1 + self.length_recursive(node.next)
        
    def delete_node(self, key):
        cur_node = self.head
        if cur_node and cur_node.data == key:
            self.head = cur_node.next
            cur_node = None
        prev = None
        while cur_node and cur_node.data != key:
            prev = cur_node
            cur_node = cur_node.next
            
        if cur_node is None:
            print("Node not present")
            
        prev.next = cur_node.next
        cur_node = None
        
    def delete_node_at_pos(self, pos):
        cur_node = self.head
        
        if pos == 0:
            self.head = cur_node.next
            cur_node = None
            return
        prev = None
        
        count = 1
        
        while cur_node and count != pos:
            prev = cur_node
            cur_node = cur_node.next
            count +=1
        
        if cur_node is None:
            print("No such node")
        
        prev.next = cur_node.next
        cur_node = None
  
    def reverse_iterative(self):
        prev = None
        cur = self.head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = cur.next
            cur = nxt
        self.head = prev
    
    def reverse_recursive(self):
        def rev(cur, prev):
            if not cur:
                return prev
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
            return rev(cur, prev)
        self.head = rev(cur=self.head, prev=None) 
        
        
    def merge_sorted(self, llist):
        p = self.head
        q = llist.head
        s = None
        
        if p == None:
            return llist
        if q == None:
            return self
        if p.data <= q.data:
            s = p
            p = s.next
        else:
            s=q
            q=s.next
            
        new_head = s
        while p and q:
            if p.data<=q.data:
                s.next = p
                s = p
                p = s.next
            else:
                s.next = q
                s = q
                q = s.next
        if not p:
            s.next = p
        if not q:
            s.next = q
            
        return new_head
    
    def remove_duplicate(self):
        cur = self.head
        prev = None
        dic = dict()
        
        while cur:
            if cur.data in dic:
                prev.next, cur = cur.next, None
                # cur.next 
            else:
                dic[cur.data] = 1
                prev = cur
            cur = prev.next
    # def nth_node(self, n):
        #first method
        # total_len = length_iterative()
        # cur_node = self.head
        # while cur:
        #     if total_len == n:
        #         print_list(cur_node.data)
        #         return cur_node
        #     total_len -= 1
        #     cur = cur_node.next
        # if cur_node = None:
        #     return
       
        #second method
        # p = self.head
        # q = self.head
        # count = 0
        # while q and count < n:
        #     q = q.next
        #     count +=1
        
        # if not q:
        #     print(str(n) + "is greater than the lenth of the linked list")
        
        # while p and q:
        #     p = p.next
        #     q = q.next
        # return p.data
    
    def count_occurance(self, node, data):
        # count = 0 
        # cur_node = self.head
        # while cur_node:
        #     if cur_node.data == data:
        #         count += 1
        #     cur_node = cur_node.next
        # return count
        if not node:
            return 0
        if node.data == data:
            return 1 + self.count_occurance(node.next, data)
        else:
            return self.count_occurance(node.next, data)

            
    def rotate(self, key):
        q = self.head
        p = self.head
        
        prev = None
        count = 0
        
        while p and count < key:
            prev  = p
            p = p.next
            q = q.next
            count += 1
            
        p = prev
        
        while q:
            prev = q
            q = q.next
        q = prev
        q.next = self.head
        self.head = p.next
        p.next = None
                
     
    def is_palindrome(self):
        s = ""
        p = self.head
        while p:
            s += p.data
            p = p.next
        x =  s[::-1]
        if s == x:
            print("This is a palindrome")
        else:
            print("Not a palindrome")
        
        # p = self.head
        # s = []
        # while p:
        #     s.append(p.data)
        #     p = p.next
        # p = self.head
        # while p:
        #     data = s.pop()
        #     if p.data != data:
        #         return False
        #     p = p.next
        # return True
        
    
    def move_tail_to_head(self):
        p = self.head
        second_to_last = None
        
        while p.next:
            # if p.next == None:
            second_to_last = p
            p = p.next
        p.next = self.head
        second_to_last.next = None
        self.head = p
        
    def sum_two_list(self, llist):
        p = self.head
        q = llist.head
        
        x = ""
        y = ""
        while p:
            x += p.data
            p = p.next
        while q:
            y += q.data
            q = q.next
        
        z = (int(x) + int (y))
        print(z)
        
        
        
             
        
llist5 = Linkedlist()
llist5.append("R")
llist5.append("A")
llist5.append("C")
llist5.append("E")
llist5.append("C")
llist5.append("A")
llist5.append("R")

print(llist5.move_tail_to_head())


    
llist1 = Linkedlist()
llist1.append("1")
llist1.append("5")
llist1.append("7")
llist1.append("9")
llist1.append("13")


llist2 = Linkedlist()
llist2.append("2")
llist2.append("3")
llist2.append("4")
llist2.append("6")
llist2.append("8")
llist2.append("10")
llist2.append("11")
llist2.append("12")

llist4 = Linkedlist()
llist4.append("1")
llist4.append("2")
llist4.append("3")
llist4.append("1")
llist4.append("4")
llist4.append("1")
llist4.append("2")
# llist4.print_list()

# print(llist4.count_occurance(llist4.head, 4))

# llist1.rotate(3)
# llist1.print_list()

# x=llist4.remove_duplicate()
# llist4.print_list()
# x = llist1.merge_sorted(llist2)
# llist3 = Linkedlist()
# llist3.append(x)
# llist3.print_list()

# llist1.merge_sorted(llist2).print_list
# llist3.print_list()
# llist.prepend("E")
# llist.insert_after_node(llist.head.next.next, "F")
# llist.print_list()
# llist.swap_nodes("A", "C")
# llist.delete_node_at_pos(2)
# llist.reverse_recursive()
# print(llist.length_recursive(llist.head))

# x = "234"
# print(int(x) + int(x))

llist6 = Linkedlist()
llist6.append("3")
llist6.append("6")
llist6.append("5")

llist7 = Linkedlist()
llist7.append("2")
llist7.append("4")
llist7.append("8")

llist6.sum_two_list(llist7)


