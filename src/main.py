from textnode import TextNode, TextType


def main():
    new_text_node = TextNode("hi", TextType.ITALIC_TEXT, "https://www.boot.dev")
    print(new_text_node)


main()
