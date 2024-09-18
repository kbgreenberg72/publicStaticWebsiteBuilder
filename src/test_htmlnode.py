import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("h1", "Hello this is a test",props = {"href": "https://google.com"})
        node2 = HTMLNode("h1", "Hello this is a test",props = {"href": "https://google.com"})
        node3 = HTMLNode("p", "Hello World",props = {"target": "_blank"})
        self.assertEqual(node,node2)
        
    def test_notEq(self):
        node = HTMLNode("h1", "Hello this is a test",props = {"href": "https://google.com"})
        node2 = HTMLNode("h1", "Hello this is a test",props = {"href": "https://google.com"})
        node3 = HTMLNode("p", "Hello World",props = {"target": "_blank"})
        self.assertNotEqual(node, node3)
        
    def test_rep(self):
        node = HTMLNode("h1", "Hello this is a test",props = {"href": "https://google.com"})
        node2 = HTMLNode("h1", "Hello this is a test",props = {"href": "https://google.com"})
        node3 = HTMLNode("p", "Hello World",props = {"target": "_blank"})
        print(node2, "\n",node3)


if __name__ == "__main__":
    unittest.main()