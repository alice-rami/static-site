import unittest
from leafnode import LeafNode


def test_leaf_to_html_p(self):
    node = LeafNode("p", "Hello, world!")
    self.assertEqual(node.to_html(), "<p>Hello, world!</p>")


def test_leaf_to_html_a(self):
    node = LeafNode("a", "Hello, world!", {"color": "blue"})
    self.assertEqual(node.to_html(), '<a color="blue">Hello, world!</a>')


def test_leaf_to_html_div(self):
    node = LeafNode("div", "Hello, world!")
    self.assertEqual(node.to_html(), "<div>Hello, world!</div>")
