class Stack():
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
        
    def pop(self):
        return self.items.pop()
        
    def print_stack(self):
        return self.items
    
    def is_empty(self):
        return self.items == []
        
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        
def reverse_string(stack, input_str):
    for i in range(len(input_str)):
        stack.push(input_str[i])
    
    reverseString = ""
    while not stack.is_empty():
        reverseString += stack.pop()
        # TODO: write code...
    return reverseString
    
def is_match(p1, p2):
    if p1 == "(" and p2 == ")":
        return True
    elif p1 == "{" and p2 == "}":
        return True
    elif p1 == "[" and p2 == "]":
        return True
    else:
        return False
            
def balanced_paren(paren_string):
    s = Stack()
    is_balanced = True
    index = 0
    
    while index < len(paren_string) and is_balanced:
        paren = paren_string[index]
        if paren in "([{":
            s.push(paren)
        else:
            if s.is_empty():
                is_balanced = False
            else:
                top = s.pop()
                if not is_match(top, paren):
                    is_balanced = False
        index += 1
    
    if s.is_empty and is_balanced:
        return True
    else:
        return False
                # TODO: write code...
        
s = Stack()
s.push("Trent")
s.push("Robbo")
s.push("Hendo")
# s.pop()
# input_str = "Allison"

print(balanced_paren("{]"))

# print(reverse_string(s, input_str))