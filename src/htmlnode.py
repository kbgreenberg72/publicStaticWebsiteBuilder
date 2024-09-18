

class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        '''
        An HTMLNode without a tag will just render as raw text
        An HTMLNode without a value will be assumed to have children
        An HTMLNode without children will be assumed to have a value
        An HTMLNode without props simply won't have any attributes
        '''
        self.tag = tag # A string representing the HTML tag name
        self.value = value # A string representing the value of the HTML tag
        self.children = children # A list of HTMLNode objects representing the children of this node
        self.props = props # A dictionary of key-value pairs representing the attributes of the HTML tag. 
        
    def __eq__(self, other):
        if(self.tag == other.tag and
           self.value == other.value and
           self.children == other.children and
           self.props == other.props):
            return True
        return False
        
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
        
    def to_html(self):
        raise NotImplementedError()
    
    def props_to_html(self):
        props: list = []
        
        for item in self.props:
            props.append(f'{item}="{self.props[item]}"')
        
        string_return = " ".join(props)
        
        return string_return
    