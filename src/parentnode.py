from htmlnode import HTMLNode
from leafnode import LeafNode


class ParentNode(HTMLNode):
    def __init__(
        self,
        tag: str | None,
        children: list[HTMLNode | LeafNode] | None,
        props: dict[str, str] | None = None,
    ):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if not self.tag:
            raise ValueError("tag is required")

        if not self.children:
            raise ValueError("children is required")

        content = ""
        for child in self.children:
            content += child.to_html()

        return f"<{self.tag}{self.props_to_html()}>{content}</{self.tag}>"
