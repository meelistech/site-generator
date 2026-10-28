import unittest
from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_neq_text(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is another text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

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
