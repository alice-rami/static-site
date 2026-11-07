class HTMLNode:
    def __init__(
        self,
        tag: str | None = None,
        value: str | None = None,
        children: list["HTMLNode"] | None = None,
        props: dict[str, str] | None = None,
    ):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        if self.props is None:
            return ""

        res = ""

        for key, value in self.props.items():
            res += f' {key}="{value}"'
        return res

    def __repr__(self):
        return f"HTMLNode: <{self.tag}{self.props_to_html()}>{self.value or self.children}</{self.tag}>"
