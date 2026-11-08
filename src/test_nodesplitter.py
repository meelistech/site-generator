import unittest
from nodesplitter import (
    split_nodes_delimiter,
    split_nodes_image,
    split_nodes_link,
    text_to_textnodes,
)
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

    ### Here start the TextNode to IMAGE and LINK splitting tests.

    def test_split_image(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        result = [
            TextNode("This is text with an ", TextType.TEXT),
            TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            TextNode(" and another ", TextType.TEXT),
            TextNode("second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"),
        ]
        self.assertEqual(result, new_nodes)

        node2 = TextNode("![Image](https://i.imgur.com/zjjcJKZ.png)", TextType.TEXT)
        self.assertEqual(
            split_nodes_image([node2]),
            [TextNode("Image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png")],
        )

    def test_split_image_with_remaining_text(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and some text.",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and some text.", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_split_link(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.TEXT,
        )

        result = [
            TextNode("This is text with a link ", TextType.TEXT),
            TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
            TextNode(" and ", TextType.TEXT),
            TextNode(
                "to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"
            ),
        ]
        new_nodes = split_nodes_link([node])

        self.assertEqual(result, new_nodes)

        node2 = TextNode(
            "This is text with a link ![image](https://i.imgur.com/zjjcJKZ.png) and [to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.TEXT,
        )
        self.assertListEqual(
            split_nodes_link([node2]),
            [
                TextNode(
                    "This is text with a link ![image](https://i.imgur.com/zjjcJKZ.png) and ",
                    TextType.TEXT,
                ),
                TextNode(
                    "to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"
                ),
            ],
        )

    def test_split_link_with_remaining_text(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and some text.",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and some text.", TextType.TEXT),
            ],
            new_nodes,
        )

    ### Test text to TextNode conversion tests ###

    def test_no_text(self):
        text = ""
        nodes = text_to_textnodes(text)
        self.assertEqual(nodes, [])

    def test_all_types(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        nodes = text_to_textnodes(text)

        result = [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode(
                "obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"
            ),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
        ]

        self.assertEqual(nodes, result)


if __name__ == "__main__":
    unittest.main()
