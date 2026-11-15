from md_to_html_node import markdown_to_html_node
from extract_title import extract_title
import os


def generate_page(from_path: str, template_path: str, dest_path: str, basepath: str):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path) as f:
        markdown = f.read()
        html_str = markdown_to_html_node(markdown).to_html()
        title = extract_title(markdown)

    with open(template_path) as f:
        template = f.read()
        r1 = template.replace("{{ Title }}", title)
        r2 = r1.replace("{{ Content }}", html_str)
        r3 = r2.replace('href="/', f'href="{basepath}')
        r4 = r3.replace('src="/', f'src="{basepath}')

    os.makedirs(os.path.dirname(dest_path), exist_ok=True)

    with open(dest_path, "w") as f:
        f.write(r4)


def generate_pages_recursive(
    dir_path_content: str, template_path: str, dest_dir_path: str, basepath: str
) -> None:
    items = os.listdir(dir_path_content)
    for item in items:
        item_from_path = os.path.join(dir_path_content, item)
        item_to_path = os.path.join(dest_dir_path, item)
        if os.path.isfile(item_from_path):
            generate_page(
                from_path=item_from_path,
                template_path=template_path,
                dest_path=item_to_path.replace(".md", ".html"),
                basepath=basepath,
            )
        else:
            generate_pages_recursive(
                dir_path_content=item_from_path,
                template_path=template_path,
                dest_dir_path=item_to_path,
                basepath=basepath,
            )
