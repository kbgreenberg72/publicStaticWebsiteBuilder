import unittest

from htmlnode import HTMLNode, ParentNode, LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_to_html_props(self):
        node = HTMLNode(
            "div",
            "hello world",
            None,
            {"class": "greeting", "href": "https://google.com"},
             )
        self.assertEqual(
            node.props_to_html(),
            'class="greeting" href="https://google.com"',
        )
    
    def test_values(self):
        node = HTMLNode(
            "div",
            "testing",
        )
        self.assertEqual(
            node.tag,
            "div",
        )
        self.assertEqual(
            node.value,
            "testing",
        )
        self.assertEqual(
            node.children,
            None,
        )
        self.assertEqual(
            node.props,
            None,
        )
    
    def test_repr(self):
        node = HTMLNode(
            "p",
            "testing",
            None,
            {"class": "primary"},
        )
        self.assertEqual(
            node.__repr__(),
            "HTMLNode(p, testing, children: None, {'class': 'primary'})"
        )

    def test_to_html_no_children(self):
        node = LeafNode("p","testing")
        self.assertEqual(node.to_html(), "<p>testing</p>")
    
    def test_to_html_no_tag(self):
        node = LeafNode(None,"testing")
        self.assertEqual(node.to_html(), "testing")
    
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div",[child_node])
        self.assertEqual(parent_node.to_html(),"<div><span>child</span></div>")
    
    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
    
    def test_to_html_many_children(self):

if __name__ == "__main__":
    unittest.main()