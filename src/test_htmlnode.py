import unittest
from htmlnode import HTMLNode


class TestTextNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode("p", "Hello", props={"color": "red"})
        self.assertEqual(node.props_to_html(), ' color="red"')

    def test_no_props(self):
        node = HTMLNode("p", "Hello world")
        self.assertEqual(node.props_to_html(), "")

    def test_to_str(self):
        node = HTMLNode("p", "Hello world", props={"color": "red"})
        self.assertEqual(str(node), 'HTMLNode: <p color="red">Hello world</p>')
