import re
from blocknode import BlockType


def block_to_block_type(md_block: str) -> BlockType:
    if bool(re.match(r"^#{1,6} ", md_block)):
        return BlockType.HEADING

    if md_block.startswith("```\n") and md_block.endswith("\n```"):
        return BlockType.CODE

    lines = md_block.split("\n")

    if all(line.startswith(">") for line in lines):
        return BlockType.QUOTE

    if all(line.startswith("- ") for line in lines):
        return BlockType.UL

    if all(line.startswith(". ") for line in lines):
        return BlockType.OL

    return BlockType.PARAGRAPH
