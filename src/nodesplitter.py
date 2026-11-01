from textnode import TextNode, TextType


def split_nodes_delimiter(
    old_nodes: list[TextNode], delimiter: str, text_type: TextType
) -> list[TextNode]:

    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        # check for matching delimiter
        if node.text.count(delimiter) % 2 != 0:
            raise ValueError("delimiters are not matching")

        # We split the
        parts = node.text.split(delimiter)
        while parts != []:
            if len(parts) == 1:
                last = parts.pop(0)
                if last != "":
                    new_nodes.append(TextNode(last, TextType.TEXT))
                break

            first = parts.pop(0)
            second = parts.pop(0)
            for item in [
                TextNode(first, TextType.TEXT),
                TextNode(second, text_type),
            ]:
                if item.text != "":
                    new_nodes.append(item)

    return new_nodes
