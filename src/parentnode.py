from htmlnode import HTMLNode
import htmlnode


class ParentNode(HTMLNode):
    def __init__(
        self,
        tag: str,
        children: list[HTMLNode],
        props: dict[str, str] | None = None,
    ) -> None:

        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("ParentNode tag is missing")

        if self.children is None:
            raise ValueError("ParentNode children are missing")

        # child.to_html() for child in self.children
        html_string = ""
        for child in self.children:
            html_string += child.to_html()

        return f"<{self.tag}{self.props_to_html()}>{html_string}</{self.tag}>"
