def extract_title(markdown: str) -> str:
    lines = markdown.split("\n")
    for line in lines:
        stripped = line.strip()
        if stripped.startswith("# "):
            return stripped.split("# ")[1]

    raise Exception("No title found")
