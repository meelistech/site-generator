from htmlnode import HTMLNode


class LeafNode(HTMLNode):
    def __init__(
        self,
        tag: str | None,
        value: str,
        props: dict[str, str] | None = None,
    ) -> None:

        super().__init__(tag, value, None, props)

    def to_html(self):

        if self.value is None:
            raise ValueError("leaf nodes must have a value")

        if self.tag is None:
            return self.value

        prop_string = self.props_to_html()
        return f"<{self.tag}{prop_string}>{self.value}</{self.tag}>"

    def props_to_html(self) -> str:
        prop_text = ""
        if self.props is None:
            return prop_text
        for prop, val in self.props.items():
            prop_text += f' {prop}="{val}"'
        return prop_text

    def __repr__(self) -> str:
        return f"LeafNode: tag:{self.tag} value:{self.value} props:{self.props}"
