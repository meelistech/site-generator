import re


def extract_markdown_images(text: str) -> list[tuple[str, str]]:
    matches = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
    return matches


def extract_markdown_links(text):
    matches = re.findall(r"(?<!\!)\[(.*?)\]\((.*?)\)", text)
    return matches


# If regex fails try these.
# images
# r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
# regular links
# r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
