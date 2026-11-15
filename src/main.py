import os
import shutil
import sys

from generate_page import generate_pages_recursive


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
    if os.path.exists("docs"):
        shutil.rmtree("docs")

    list_and_copy("static", "docs")


def main():
    basepath: str = "/"
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    copy_from_static_to_public()

    generate_pages_recursive("content/", "template.html", "docs/", basepath=basepath)


main()
