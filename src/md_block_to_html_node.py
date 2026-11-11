from htmlnode import HTMLNode
from leafnode import LeafNode
from parentnode import ParentNode
from block_to_block_type import block_to_block_type
from blocknode import BlockType
from text_to_textnodes import text_to_textnodes
from textnode import TextNode, TextType, text_node_to_html_node


def md_block_to_html_node(md_block) -> HTMLNode:

    match block_to_block_type(md_block):
        case BlockType.HEADING:
            sections = md_block.split()
            count = sections[0].count("#")
            return HTMLNode(f"h{count}", sections[1])

        case BlockType.QUOTE:
            lines = md_block.split("\n")
            cleared_lines = list(map(lambda l: l[1:].strip(), lines))
            return HTMLNode("blockquote", "\n".join(cleared_lines))

        case BlockType.CODE:
            lines = md_block.split("\n")
            content = TextNode("\n".join(lines[1:-1]), text_type=TextType.CODE_TEXT)
            return ParentNode("pre", [text_node_to_html_node(content)])

        case BlockType.OL:
            li_nodes = list(map(lambda l: HTMLNode("li", l), md_block.split("\n")))

            return ParentNode("ol", li_nodes)

        case BlockType.UL:
            li_nodes = list(map(lambda l: HTMLNode("li", l), md_block.split("\n")))

            return ParentNode("ul", li_nodes)

        case BlockType.PARAGRAPH:
            text_nodes = list(map(text_node_to_html_node, text_to_textnodes(md_block)))
            return ParentNode("p", children=text_nodes)

        case _:
            raise Exception("invalid type")
