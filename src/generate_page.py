from md_to_html_node import markdown_to_html_node
from extract_title import extract_title
import os


def generate_page(from_path: str, template_path: str, dest_path: str):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path) as f:
        markdown = f.read()
        html_str = markdown_to_html_node(markdown).to_html()
        title = extract_title(markdown)

    with open(template_path) as f:
        template = f.read()
        r1 = template.replace("{{ Title }}", title)
        r2 = r1.replace("{{ Content }}", html_str)

    os.makedirs(os.path.dirname(dest_path), exist_ok=True)

    with open(dest_path, "w") as f:
        f.write(r2)
