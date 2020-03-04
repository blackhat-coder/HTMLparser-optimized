# coding: utf-8



from html.parser import HTMLParser 
import os


class Stack:
    def __init__(self):
        self.container = []
    
    def push(self, k):
        self.container.append(k)
    
    def pop(self):
        try:
            self.container.pop(len(self.container)-1)
        except Exception:
            return (f"wrong pop")
    
    def last_element(self):
        return (self.container[len(self.container) - 1])

    def length(self):
        return len(self.container)

    def index(self,d):
        return str(self.container[d])

    
stack = Stack()  

class Node:
    def __init__(self,d_tag,line=0):
        self.d_tag = d_tag
        self.line = line
    
    def __str__(self):
        return self.d_tag

class MyParser(HTMLParser):
    
    def handle_starttag(self, tag, attrs):
        stack.push(Node(tag))

    def handle_endtag(self, tag):
        
        for i in range(stack.length()-1,0,-1):
            if str(tag) == stack.index(i):
                stack.pop()
                break

            elif str(tag) != stack.index(i):
                print(f" error, line: expected closing tag {stack.index(i)} ")
                stack.pop()


class Htmlparserdebug(HTMLParser):

    # def __init__(self,file_name="none.txt",html_file=None):
    #     # file_path = os.path.join(os.getcwd(), file_name)
    #     # self.html_file = open(file_path, "r+")
    #     # html_file = open(file_path, "r+")
    
    html_file = open('text.txt',"r+")
    def document(self):
    	pass

    def terminate(self):
        html_file.close()
    
    def debug(self):
        html_file = open('text.txt',"r+")                                
        
        line = 0
        for line_check in html_file:
            line += 1
            print(f"line:{line-1}")
            dd = MyParser()
            dd.feed(line_check)                                 




obj = Htmlparserdebug()
obj.debug()

