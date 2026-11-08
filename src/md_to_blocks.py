def markdown_to_blocks(markdown: str) -> list[str]:
    return list(
        filter(lambda i: len(i), map(lambda l: l.strip(), markdown.split("\n\n")))
    )
