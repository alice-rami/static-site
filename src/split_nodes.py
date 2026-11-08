from textnode import TextType, TextNode
from extract_md import extract_markdown_images, extract_markdown_links


def split_nodes_delimiter(
    old_nodes: list[TextNode], delimiter: str, text_type: TextType
) -> list[TextNode]:
    new_nodes: list[TextNode] = []

    for old_node in old_nodes:
        if old_node.text_type != TextType.PLAIN_TEXT:
            new_nodes.append(old_node)
        else:
            if old_node.text.count(delimiter) % 2 != 0:
                raise Exception("invalid Markdown syntax")
            split_text = old_node.text.split(delimiter)
            for i in range(0, len(split_text)):
                if i % 2 == 0:
                    new_nodes.append(TextNode(split_text[i], TextType.PLAIN_TEXT))
                else:
                    new_nodes.append(TextNode(split_text[i], text_type))
    return new_nodes


def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes: list[TextNode] = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.PLAIN_TEXT:
            new_nodes.append(old_node)
            continue
        elif len(old_node.text) == 0:
            continue
        links_data = extract_markdown_links(old_node.text)
        if len(links_data) == 0:
            new_nodes.append(old_node)
            continue

        original_text = old_node.text
        for link_text, link_url in links_data:

            sections = original_text.split(f"[{link_text}]({link_url})", 1)

            if len(sections[0]):
                new_nodes.append(TextNode(sections[0], TextType.PLAIN_TEXT))

            new_nodes.append(TextNode(link_text, TextType.LINK, link_url))

            original_text = sections[1]

        if len(original_text):
            new_nodes.append(TextNode(original_text, TextType.PLAIN_TEXT))

    return new_nodes


def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes: list[TextNode] = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.PLAIN_TEXT:
            new_nodes.append(old_node)
            continue
        elif len(old_node.text) == 0:
            continue
        images_data = extract_markdown_images(old_node.text)
        if len(images_data) == 0:
            new_nodes.append(old_node)
            continue

        original_text = old_node.text
        for image_alt, image_link in images_data:

            sections = original_text.split(f"![{image_alt}]({image_link})", 1)

            if len(sections[0]):
                new_nodes.append(TextNode(sections[0], TextType.PLAIN_TEXT))

            new_nodes.append(TextNode(image_alt, TextType.IMAGE, image_link))

            original_text = sections[1]

        if len(original_text):
            new_nodes.append(TextNode(original_text, TextType.PLAIN_TEXT))

    return new_nodes
