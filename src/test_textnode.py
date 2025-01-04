import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXT)
        node2 = TextNode("This is a text node", TextType.BOLD_TEXT)
        self.assertEqual(node, node2)

    def test_ne(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a different text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXT)
        self.assertEqual(repr(node), "TextNode(text='This is a text node', text_type='bold', url=None)")

    def test_ne(self):
        node = TextNode("This is a text node", TextType.NORMAL_TEXT)
        node2 = TextNode("This is a text node", TextType.BOLD_TEXT)
        self.assertNotEqual(node, node2)
    def test_inequality_with_different_url(self):
        node1 = TextNode("Hello", TextType.BOLD_TEXT, "http://example.com")
        node2 = TextNode("Hello", TextType.BOLD_TEXT, "http://another-example.com")
        self.assertNotEqual(node1, node2)

    def test_equality_when_url_is_none(self):
        node1 = TextNode("Hello", TextType.NORMAL_TEXT)
        node2 = TextNode("Hello", TextType.NORMAL_TEXT, None)
        self.assertEqual(node1, node2)

    def test_repr_output(self):
        node = TextNode("Hello", TextType.NORMAL_TEXT)
        expected_repr = "TextNode(text='Hello', text_type='normal', url=None)"
        self.assertEqual(repr(node), expected_repr)

    def test_invalid_text_type(self):
        with self.assertRaises(ValueError):
            TextNode("Hello", "invalid_type")



if __name__ == "__main__":
    unittest.main()