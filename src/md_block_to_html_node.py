from parentnode import ParentNode
from leafnode import LeafNode
from block_to_block_type import block_to_block_type
from blocknode import BlockType
from text_to_textnodes import text_to_textnodes
from textnode import TextNode, TextType, text_node_to_html_node


def text_to_html_str(text: str) -> str:
    textnodes = text_to_textnodes(text)
    return "".join(list(map(lambda t: text_node_to_html_node(t).to_html(), textnodes)))


def get_li_text(text: str) -> str:
    if text.startswith("-"):
        return text[1:].strip()
    dot_idx = text.index(".")
    return text[dot_idx + 1 :].strip()


def get_li(text: str) -> list[str]:
    return list(
        map(
            lambda l: LeafNode(
                tag="li", value=(text_to_html_str(get_li_text(l)))
            ).to_html(),
            text.split("\n"),
        )
    )


def md_block_to_html_node(md_block) -> LeafNode:

    block_type = block_to_block_type(md_block)

    match block_type:
        case BlockType.HEADING:
            sections = md_block.split()
            count = sections[0].count("#")
            node = LeafNode(tag=f"h{count}", value=" ".join(sections[1:]))
            return node

        case BlockType.QUOTE:
            lines = md_block.split("\n")
            cleared_lines = list(map(lambda l: l[1:].strip(), lines))
            node = LeafNode(tag="blockquote", value="\n".join(cleared_lines))
            return node

        case BlockType.CODE:
            lines = md_block.split("\n")
            content = TextNode("\n".join(lines[1:-1]), text_type=TextType.CODE_TEXT)
            node = LeafNode(tag="pre", value=text_node_to_html_node(content).to_html())
            return node

        case BlockType.OL:

            li_nodes = get_li(md_block)
            node = LeafNode(tag="ol", value="".join(li_nodes))
            return node

        case BlockType.UL:
            li_nodes = get_li(md_block)
            node = LeafNode(tag="ul", value="".join(li_nodes))
            return node

        case BlockType.PARAGRAPH:
            node = LeafNode("p", value=text_to_html_str(md_block))
            return node

        case _:
            raise Exception("invalid type")
