from parentnode import ParentNode
from md_to_blocks import markdown_to_blocks
from block_to_block_type import block_to_block_type
from md_block_to_html_node import md_block_to_html_node


def markdown_to_html_node(markdown: str) -> ParentNode:
    md_blocks = markdown_to_blocks(markdown)

    block_nodes = list(map(md_block_to_html_node, md_blocks))
    print(block_nodes)

    return ParentNode("div", block_nodes)
