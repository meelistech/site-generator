def markdown_to_blocks(markdown: str) -> list[str]:
    blocks = markdown.split("\n\n")
    clean_blocks = []
    for i in range(len(blocks)):
        clean_block = blocks[i].strip()
        if clean_block != "":
            clean_blocks.append(clean_block)

    return clean_blocks
