import unittest
from leafnode import LeafNode

class testLeafNode(unittest.TestCase):
    def test_printHTML(self):
        node = LeafNode("p", "This is a paragraph of text.")
        node2 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        print(node.to_html())
        print(node2.to_html())
    

if __name__ == "__main__":
    unittest.main()