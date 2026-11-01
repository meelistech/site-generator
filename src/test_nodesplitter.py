import unittest
from nodesplitter import split_nodes_delimiter
from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_code(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        result = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, result)

    def test_bold(self):
        node = TextNode("This is text with a **bold block** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        result = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("bold block", TextType.BOLD),
            TextNode(" word", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, result)

    def test_italic(self):
        node = TextNode("This is text with a _italic block_ word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        result = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("italic block", TextType.ITALIC),
            TextNode(" word", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, result)

    def test_block_start(self):
        node = TextNode("`This is text with a `code block word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        result = [
            TextNode("This is text with a ", TextType.CODE),
            TextNode("code block word", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, result)

    def test_single_delimiter_error(self):
        node = TextNode("`This is text with a code block word", TextType.TEXT)
        self.assertRaises(ValueError, split_nodes_delimiter, [node], "`", TextType.TEXT)

    def test_multiple_blocks(self):
        node = TextNode("**This** is **text** with multiple blocks.", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        result = [
            TextNode("This", TextType.BOLD),
            TextNode(" is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with multiple blocks.", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, result)

    def test_multiple_fill_blocks(self):
        node = TextNode("**This is ****text with multiple blocks.**", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        result = [
            TextNode("This is ", TextType.BOLD),
            TextNode("text with multiple blocks.", TextType.BOLD),
        ]
        self.assertEqual(new_nodes, result)


if __name__ == "__main__":
    unittest.main()
