from textnode import TextNode, TextType
from htmlnode import HTMLNode


def main():
    new_text_node = TextNode("hi", TextType.ITALIC_TEXT, "https://www.boot.dev")
    print(new_text_node)

    new_html_node = HTMLNode("p", "Hello world", None, {"color": "red"})
    print(new_html_node)

    new_html_node_div = HTMLNode("div", children=[new_html_node])
    print(new_html_node_div)


main()
