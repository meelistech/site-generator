import unittest
from htmlnode import HTMLNode
from textnode import TextNode, TextType


class TestHTMLNode(unittest.TestCase):
    def test_default(self):
        node = HTMLNode()
        # node2 = HTMLNode(None, None, None, None)
        # self.assertEqual(node.props_to_html(), node2.props_to_html())
        self.assertIsNone(node.tag)
        self.assertIsNone(node.value)
        self.assertIsNone(node.children)
        self.assertIsNone(node.props)
        self.assertEqual(node.props_to_html(), "")

    def test_prop_to_html(self):
        node_props = HTMLNode(
            "tag", "val", None, {"href": "https://www.google.com"}
        ).props_to_html()
        self.assertEqual(node_props, ' href="https://www.google.com"')

    def test_props_to_html(self):
        node_props = HTMLNode(
            "tag", "val", None, {"href": "https://www.google.com", "target": "_blank"}
        ).props_to_html()
        self.assertEqual(node_props, ' href="https://www.google.com" target="_blank"')

    def test_to_html_raises(self):
        node = HTMLNode()
        with self.assertRaises(NotImplementedError):
            node.to_html()

    def test_neq_type(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_url_default(self):
        node = TextNode("This is a text node", TextType.TEXT)
        self.assertEqual(node.url, None)

    def test_url_defaule_eq(self):
        node = TextNode("This is a text node", TextType.TEXT, "boot.dev")
        node2 = TextNode("This is a text node", TextType.TEXT)
        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()
