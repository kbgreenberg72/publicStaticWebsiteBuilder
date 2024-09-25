from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self,tag = None, children=None, props = None):
        super().__init__(tag=tag, value=None, children=children, props=props)
        
    def to_html(self):
        if self.tag == None or self.children == None:
            raise ValueError()
        pass
        

