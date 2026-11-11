import os
import shutil

from textnode import TextNode, TextType
from htmlnode import HTMLNode


def list_and_copy(source_dir: str, target_dir: str) -> None:
    print(f"creating dir {target_dir}")
    os.mkdir(target_dir)
    items = os.listdir(source_dir)
    for item in items:
        item_path = os.path.join(source_dir, item)
        if os.path.isfile(item_path):
            print(f"copying {item} from {item_path} to {target_dir}")
            shutil.copy(item_path, target_dir)
        else:
            target_path = os.path.join(target_dir, item)
            list_and_copy(item_path, target_path)


def copy_from_static_to_public() -> None:
    if os.path.exists("public"):
        shutil.rmtree("public")

    list_and_copy("static", "public")


def main():
    copy_from_static_to_public()


main()
