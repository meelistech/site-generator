import unittest
from htmlnode import HTMLNode
from leafnode import LeafNode
from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_leaf_to_html(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

        node2 = LeafNode(
            "div",
            "Hello, world!",
            {"class": "greeting", "href": "https://boot.dev"},
        )
        self.assertEqual(
            node2.to_html(),
            '<div class="greeting" href="https://boot.dev">Hello, world!</div>',
        )
        node3 = LeafNode("p", "This is a paragraph of text.")
        self.assertEqual(node3.to_html(), "<p>This is a paragraph of text.</p>")

        node4 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(
            node4.to_html(), '<a href="https://www.google.com">Click me!</a>'
        )

    def test_leaf_no_value(self):
        node3 = LeafNode("a", None, None)
        with self.assertRaises(ValueError):
            node3.to_html()

    def test_leaf_no_tag(self):
        node4 = LeafNode(None, "val", None)
        self.assertEqual(node4.to_html(), "val")


if __name__ == "__main__":
    unittest.main()
