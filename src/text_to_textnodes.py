from textnode import TextNode, TextType
from split_nodes import split_nodes_delimiter, split_nodes_link, split_nodes_image


def text_to_textnodes(text: str) -> list[TextNode]:
    text_node = TextNode(text, TextType.PLAIN_TEXT)
    return split_nodes_link(
        split_nodes_image(
            split_nodes_delimiter(
                split_nodes_delimiter(
                    split_nodes_delimiter([text_node], "**", TextType.BOLD_TEXT),
                    "_",
                    TextType.ITALIC_TEXT,
                ),
                "`",
                TextType.CODE_TEXT,
            )
        )
    )
