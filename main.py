# coding: utf-8







from html.parser import HTMLParser 
import os
import datetime


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
        try:
            return (self.container[len(self.container) - 1])
        except Exception:
            return 0

    def length(self):
        return len(self.container)

    def index(self,d):
        return self.container[d]

    
stack = Stack()
c_wd = None
line = 0

class Node:
    def __init__(self,d_tag,l):
        self.d_tag = d_tag
        self.l = l 
    
    def __str__(self):
        return self.d_tag


class MyParser(HTMLParser):
    
    def handle_starttag(self, tag, attrs):
        node = Node(tag, line)
        stack.push(node)

    def handle_endtag(self, tag):
        for i in range(stack.length()-1,0,-1):
            d,f = stack.index(i),stack.index(i)

            cur_tag = d.d_tag
            cur_line = f.l
            if str(tag) == str(cur_tag):
                stack.pop()
                break

            elif str(tag) != str(cur_tag):
                print(f" error, line{cur_line}: expected closing tag {stack.index(i)} ")
                stack.pop()


       
class Htmlparserdebug(HTMLParser):
    
    def __init__(self):
        global c_wd
        c_wd = os.getcwd()

    def debug(self,file_name):
                                     
        html_file = open(file_name,"r+",encoding='utf-8')
        print(os.path.join(c_wd,file_name))
        print(datetime.datetime.now())
        print("")
        
        for line_check in html_file:
            global line
            line += 1
            dd = MyParser()
            dd.feed(line_check)
            

        html_file.close()                              


if __name__ == "__main__":
    main()
