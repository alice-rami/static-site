from htmlnode import HTMLNode


class ParentNode(HTMLNode):
    def __init__(
        self,
        tag: str | None,
        children: list[HTMLNode] | None,
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

        return f"<{self.tag}>{content}</{self.tag}>"
