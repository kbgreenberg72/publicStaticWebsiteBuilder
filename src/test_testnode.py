import unittest

from textnode import TextNode

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a test node", "bold")
        node2 = TextNode("This is a test node", "bold")
        node3 = TextNode("This needs to be different", "italic", "https://helpme.com")
        self.assertEqual(node, node2)
        self.assertIsNone(node.url)
        self.assertIsNotNone(node3.url)
        self.assertEqual(node.text_type,node2.text_type)
        self.assertNotEqual(node, node3)
        
        
        
if __name__ == "__main__":
    unittest.main()