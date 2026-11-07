import unittest
from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXT)
        node2 = TextNode("This is a text node", TextType.BOLD_TEXT)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXT)
        node2 = TextNode("This is a text node", TextType.IMAGE, "https://www.boot.dev")
        self.assertNotEqual(node, node2)

    def test_url_has_default(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXT)
        self.assertEqual(node.url, None)


if __name__ == "__main__":
    unittest.main()
