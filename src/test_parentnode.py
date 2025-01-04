import unittest

from htmlnode import HTMLNode
from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    
    def test_missing_tag(self):
        """Test when no tag is provided for ParentNode."""
        with self.assertRaises(ValueError) as context:
            ParentNode("", [HTMLNode("p", "Test text")])
        self.assertEqual(str(context.exception), "ParentNode must have a tag.")
    
    def test_missing_children(self):
        """Test when no children are provided for ParentNode."""
        with self.assertRaises(ValueError) as context:
            ParentNode("div", [])
        self.assertEqual(str(context.exception),"ParentNode must have atleast one child.")

    def test_valid_parent_node(self):
        child1 = LeafNode("p", value="First child")
        child2 = LeafNode("a", value="Click me!", props={"href": "https://example.com"} )
        parent = ParentNode("div",[child1,child2], props={"class": "container"})

        
        expected_html = '<div class="container"><p>First child</p><a href="https://example.com">Click me!</a></div>'
        self.assertEqual(parent.to_html(), expected_html)

    def test_nested_parentnode(self):
        inner = ParentNode("div", [LeafNode("h1", "Heading")], props={"class":"inner"})
        outer = ParentNode("section", [inner, LeafNode("footer", "Footer text")], props={"class":"outer"})
        expected_html = '<section class="outer"><div class="inner"><h1>Heading</h1></div><footer>Footer text</footer></section>'
        self.assertEqual(outer.to_html(),expected_html)

    def test_missing_props(self):
        """Test when no props are provided for ParentNode."""
        child1 = LeafNode("p", "First child")
        parent = ParentNode("div", [child1])
        expected_html = '<div><p>First child</p></div>'
        self.assertEqual(parent.to_html(), expected_html)

   
    def test_parent_with_leaf_nodes(self):
        """Test ParentNode containing LeafNode objects."""
        child1 = LeafNode("p", "Paragraph inside")
        child2 = LeafNode("a", "Link", {"href": "https://link.com"})
        parent = ParentNode("section", [child1, child2])
        expected_html = '<section><p>Paragraph inside</p><a href="https://link.com">Link</a></section>'
        self.assertEqual(parent.to_html(), expected_html)

    def test_empty_children(self):
        """Test ParentNode with an empty list of children."""
        with self.assertRaises(ValueError) as context:
            ParentNode("article", [])
        self.assertEqual(str(context.exception), "ParentNode must have atleast one child.")
    
    def test_single_child(self):
        """Test ParentNode with only one child."""
        child = LeafNode("p", "Single child paragraph")
        parent = ParentNode("div", [child])
        expected_html = '<div><p>Single child paragraph</p></div>'
        self.assertEqual(parent.to_html(), expected_html)

    def test_multiple_children(self):
        """Test ParentNode with multiple children."""
        child1 = LeafNode("p", "First paragraph")
        child2 = LeafNode("a", "Link",  {"href": "https://google.com"})
        child3 = LeafNode("span", "Span text")
        parent = ParentNode("div", [child1, child2, child3])
        expected_html ='<div><p>First paragraph</p><a href="https://google.com">Link</a><span>Span text</span></div>'
        
        self.assertEqual(parent.to_html(), expected_html)
    
    def test_parent_with_child_without_props(self):
        """Test ParentNode where child does not have props."""
        child = LeafNode("p", "Paragraph without props")
        parent = ParentNode("section", [child])
        expected_html = '<section><p>Paragraph without props</p></section>'
        self.assertEqual(parent.to_html(), expected_html)

    def test_repr_with_props(self):
        """Test __repr__ method with properties."""
        child = LeafNode("a", "Link", props ={"href": "https://google.com"})
        parent = ParentNode("div", [child], props = {"class": "container"})
        expected_repr = '<div class="container"><a href="https://google.com">Link</a></div>'
        self.assertEqual(repr(parent), expected_repr)

    def test_repr_no_props(self):
        """Test __repr__ method without properties."""
        child = LeafNode("p", "Simple paragraph")
        parent = ParentNode("article", [child])
        expected_repr = "<article><p>Simple paragraph</p></article>"
        self.assertEqual(repr(parent), expected_repr)
    
if __name__ == "__main__":
    unittest.main()
