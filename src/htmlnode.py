class HTMLNode:
    def __init__(
        self,
        tag: str | None = None,
        value: str | None = None,
        children: list[HTMLNode] | None = None,
        props: dict[str, str] | None = None,
    ) -> None:

        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self) -> str:
        prop_text = ""
        if self.props is None:
            return prop_text
        for prop, val in self.props.items():
            prop_text += f' {prop}="{val}"'
        return prop_text

    def __repr__(self) -> str:
        return f"{self.tag} {self.value} {self.children} {self.props}"
