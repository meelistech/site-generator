import unittest

from md_blocks import markdown_to_blocks


class TestTextNode(unittest.TestCase):
    def test_md_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_md_blank_lines(self):
        md = """


Hello


"""
        self.assertEqual(markdown_to_blocks(md), ["Hello"])

    def test_md_blank_lines_between(self):
        md = """
Hello



There

"""
        self.assertEqual(markdown_to_blocks(md), ["Hello", "There"])

    def test_md_whitespace_between(self):
        md = """
Hello

                                  

There

"""
        self.assertEqual(markdown_to_blocks(md), ["Hello", "There"])

    def test_blank(self):
        md = """


        

                    


"""
        self.assertEqual(markdown_to_blocks(md), [])

    def test_2_blocks(self):
        md = """First line of one paragraph
Second line of that same paragraph

A separate paragraph"""

        self.assertEqual(
            markdown_to_blocks(md),
            [
                "First line of one paragraph\nSecond line of that same paragraph",
                "A separate paragraph",
            ],
        )


if __name__ == "__main__":
    unittest.main()
