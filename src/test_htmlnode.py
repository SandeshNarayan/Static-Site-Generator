import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):

    def test_props_to_html(self):
        node = HTMLNode(props={"href": "https://www.google.com", "target": "_blank"})
        expected_props = 'href="https://www.google.com" target="_blank"'
        self.assertEqual(node.props_to_html(), expected_props)

    def test_repr(self):
        node = HTMLNode(tag="p", value="Hello, World!", children=[], props={"class": "text"})
        expected_repr = (
            "HTMLNode(tag='p', value='Hello, World!', children=[], props={'class': 'text'})"
        )
        self.assertEqual(repr(node), expected_repr)

    def test_empty_node(self):
        node = HTMLNode()
        expected_repr = "HTMLNode(tag=None, value=None, children=[], props={})"
        self.assertEqual(repr(node), expected_repr)

    def test_node_with_children(self):
        child1 = HTMLNode(tag="span", value="Child 1")
        child2 = HTMLNode(tag="span", value="Child 2")
        parent = HTMLNode(tag="div", children=[child1, child2])
        self.assertEqual(parent.children, [child1, child2])

if __name__ == "__main__":
    unittest.main()