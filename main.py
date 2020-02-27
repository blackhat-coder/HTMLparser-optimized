

from html.parser import HTMLparser
import os


# Stack implementation
class Stack:

    def __init__(self):
        self.container = []
    
    def push(self, k):
        self.container.append(k)
    
    def pop(self):
        try:
            self.container.pop(len(self.container)-1)
        except Exception:
            print('They are no more items in the stack')
    
    def last_element(self):
        return (self.container[len(self.container) - 1])
    

class Node:
    def __init__(self,d_tag,line=0):
        self.d_tag = d_tag
        self.line = line
    
    def __str__(self):
        return self.d_tag

class Htmlparserdebug(HTMLparser):
    def __init__(self,file_name):
        
        file_path = os.path.join(os.getcwd(), file_name.txt)
        html_file = open(file_path, "r+")
    
    def terminate(self):
        html_file.close()
    
    def debug(self):
        line = 0
        stack = Stack()
        
        for line in html_file:
            line += 1
            HTMLparser.feed(line)
            if HTMLparser.handle_starttag(tag,attrs):
                stack.append(Node(tag,line))
            
            if HTMLparser.handle_endtag(tag):
                check()
    
    
    def __check(self):
        
        if HTMLparser.handle_starttag(tag) == stack.last_element.d_tag:
            stack.pop()
            break
        
        elif HTMLparser.handle_endtag(tag) != stack.last_element.d_tag:
            # error statement
            stack.pop()
            check()
    
    
    
