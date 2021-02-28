def is_palindrom(s):
    i = 0
    j = len(s)-1
    while i<j:
        while not s[i].isalnum() and i<j:
            i += 1
        while not s[j].isalnum() and i<j:
            j -= 1    
            
        if s[i].lower() != s[j].lower():
            print("")
        i += 1
        j -= 1
        
    print("True")
    
        
s = "Was it a cat I saw?"
print(is_palindrom(s))
