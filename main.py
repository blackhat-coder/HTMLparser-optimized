
# HTMLparser is the module that does the parsing
from html.parser import HTMLparser 

# import os: to be compatible with different machines when choosing a HTML document to parse and debug
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
    
    
#Node class that contains the value of the tag as d_tag and the line of the tag.
class Node:
    def __init__(self,d_tag,line=0):                                       #constructor/initializer
        self.d_tag = d_tag
        self.line = line
    
    def __str__(self):
        return self.d_tag

    
# The debug class
class Htmlparserdebug(HTMLparser):
    # constructor/initializer for document upload.
    # document has to be in the same directory
    
    def __init__(self,file_name):
        file_path = os.path.join(os.getcwd(), file_name.txt)            # joins the cwd with the filename
        html_file = open(file_path, "r+")                               # open's the file as html_file 
    
    #just added this one for :)
    def terminate(self):
        html_file.close()
    
    # Debug function()
    # Checks the closing tag with the opening tag
    def debug(self):
        line = 0                                                        # To keep track of the lines
        stack = Stack()                                                 # An instance of the Stack() class
        
        for line in html_file:                                          # basically looping through the html file
            line += 1 
            HTMLparser.feed(line)                                       # for each line, feed it to the HTMLparser feed method
            
            if HTMLparser.handle_starttag(tag,attrs):                   # handles start tags
                stack.push(Node(tag,line)) 
                
                # for every instance of the Node(d_tag,line) class, pass the tag and the line of the start tag as arguements
                # and then push it to the stack
            
            if HTMLparser.handle_endtag(tag):                           # handles endtags
                check()                                                 # function() that handles end tags
    
    
    def __check(self): #private method
        
        # if start_tag is equal to the last element in the stack
        
        if HTMLparser.handle_starttag(tag) == stack.last_element.d_tag:
            stack.pop()
            break
        
        # if the end tag is not equal to the last element in the stack
        elif HTMLparser.handle_endtag(tag) != stack.last_element.d_tag:
         
            print(f"line:{line}, expected:{self.d_tag} closing </tag>") #debug message
            stack.pop()                                                 #then pop the stack
            check()                                                     #recursive call
    
 
