from textnode import TextNode, TextType
from process_md_links import extract_markdown_images, extract_markdown_links


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


def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []
    for node in old_nodes:
        text = node.text
        links = extract_markdown_images(text)

        if len(links) == 0 and len(text) != 0:
            new_nodes.append(node)

        for alt, address in links:
            sections = text.split(f"![{alt}]({address})", 1)
            text = sections[-1]
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(TextNode(alt, TextType.IMAGE, address))

    return new_nodes


def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []
    for node in old_nodes:
        text = node.text
        links = extract_markdown_links(text)

        if len(links) == 0 and len(text) != 0:
            new_nodes.append(node)

        for alt, address in links:
            sections = text.split(f"[{alt}]({address})", 1)
            text = sections[-1]
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(TextNode(alt, TextType.LINK, address))

    return new_nodes

def text_to_textnodes(text: str) -> list[TextNode]:
    splitters = {TextType.BOLD: "**", TextType.ITALIC: "_", TextType.CODE: "`", TextType.LINK: "link", TextType.IMAGE: "img"}
    nodes = [TextNode(text, TextType.TEXT)]
    for tt, delimiter in splitters.items():
        if tt == TextType.LINK:
            nodes = split_nodes_link(nodes)
        elif tt == TextType.IMAGE:
            nodes = split_nodes_image(nodes)
        else:
            nodes = split_nodes_delimiter(nodes, delimiter, tt)
    return nodes
