import unittest
from md_to_blocks import markdown_to_blocks
from block_to_block_type import block_to_block_type
from blocknode import BlockType
from md_to_html_node import markdown_to_html_node


class TestBlockNode(unittest.TestCase):
    def test_markdown_to_blocks(self):
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

    def test_md_block_to_heading(self):
        block_type1 = block_to_block_type("# Heading 1")
        block_type2 = block_to_block_type("### Heading 3")
        block_type3 = block_to_block_type("######Heading 6")
        block_type4 = block_to_block_type("```\nprint('Hi')\n\n```")
        block_type5 = block_to_block_type("> first\n> second\nthird")
        block_type5_5 = block_to_block_type("> first\n> second\n>third")
        block_type6 = block_to_block_type("- This is a list\n- with items")
        block_type7 = block_to_block_type(". This is a list\n. with items")

        self.assertEqual(block_type1, BlockType.HEADING)
        self.assertEqual(block_type2, BlockType.HEADING)
        self.assertEqual(block_type3, BlockType.PARAGRAPH)
        self.assertEqual(block_type4, BlockType.CODE)
        self.assertEqual(block_type5, BlockType.PARAGRAPH)
        self.assertEqual(block_type5_5, BlockType.QUOTE)
        self.assertEqual(block_type6, BlockType.UL)
        self.assertEqual(block_type7, BlockType.OL)

    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = " ".join(node.to_html().split("\n"))
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )


def test_codeblock(self):
    md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

    node = markdown_to_html_node(md)
    html = node.to_html()
    self.assertEqual(
        html,
        "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
    )


if __name__ == "__main__":
    unittest.main()
