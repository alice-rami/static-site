from leafnode import LeafNode
from md_to_blocks import markdown_to_blocks
from md_block_to_html_node import md_block_to_html_node


def markdown_to_html_node(markdown: str) -> LeafNode:
    md_blocks = markdown_to_blocks(markdown)

    block_nodes = list(
        map(lambda block: md_block_to_html_node(block).to_html(), md_blocks)
    )

    return LeafNode("div", "".join(block_nodes))
