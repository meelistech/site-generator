import unittest
from process_md_links import extract_markdown_images, extract_markdown_links


class TestTextNode(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_link(self):
        matches = extract_markdown_links(
            "This is text with an [Imgur link](https://imgur.com)"
        )
        self.assertListEqual([("Imgur link", "https://imgur.com")], matches)

    def test_extract_md_img_or_link(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and ![to youtube](https://www.youtube.com/@bootdotdev)"
        link = extract_markdown_links(text)
        image = extract_markdown_images(text)
        self.assertEqual(link, [("to boot dev", "https://www.boot.dev")])
        self.assertEqual(image, [("to youtube", "https://www.youtube.com/@bootdotdev")])

    def test_extract_markdown_images_multiple(self):
        matches = extract_markdown_images(
            "Here's ![one](https://example.com/1.png) and ![two](https://example.com/2.png)"
        )
        self.assertListEqual(
            [
                ("one", "https://example.com/1.png"),
                ("two", "https://example.com/2.png"),
            ],
            matches,
        )

    def test_extract_markdown_links_multiple(self):
        matches = extract_markdown_links(
            "Here's [one](https://example.com/1.png) and [two](https://example.com/2.png)"
        )
        self.assertListEqual(
            [
                ("one", "https://example.com/1.png"),
                ("two", "https://example.com/2.png"),
            ],
            matches,
        )

    def test_no_links(self):
        text = "Hello there general."
        links = extract_markdown_links(text)
        images = extract_markdown_images(text)

        self.assertEqual(links, [])
        self.assertEqual(images, [])

    def test_empty_links_alt(self):
        text = "Here's ![](https://example.com/1.png) and [](https://example.com/2.png)"
        links = extract_markdown_links(text)
        images = extract_markdown_images(text)

        self.assertEqual(images, [("", "https://example.com/1.png")])
        self.assertEqual(links, [("", "https://example.com/2.png")])

    def test_empty_links(self):
        text = "Here's ![one]() and [two]()"
        links = extract_markdown_links(text)
        images = extract_markdown_images(text)

        self.assertEqual(images, [("one", "")])
        self.assertEqual(links, [("two", "")])


if __name__ == "__main__":
    unittest.main()
