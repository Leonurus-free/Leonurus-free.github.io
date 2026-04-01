import os

def generate_readme():
    base_dir = '.'
    exclude_dirs = {'.git', '.claude', '.obsidian', '.playwright-mcp', '.smtcmp_json_db'}

    readme_content = []
    readme_content.append("# 🍄Welcome to Leonurus-free's blogs🍄\n")
    readme_content.append("> [Github地址](https://github.com/Leonurus-free/Leonurus-free.github.io)\n")
    readme_content.append(">\n")
    readme_content.append("> [项目地址](https://leonurus-free.github.io/)\n\n")
    readme_content.append("----\n\n")
    readme_content.append("🐼 This project is used to record notes during the learning process！​​ 🐼\n\n")
    readme_content.append("---\n\n")

    # Dictionary to store files by category
    categories = {}
    root_files = []

    for root, dirs, files in os.walk(base_dir):
        # Filter out excluded directories
        dirs[:] = [d for d in dirs if d not in exclude_dirs]

        rel_path = os.path.relpath(root, base_dir)
        md_files = [f for f in files if f.endswith('.md') and f != 'README.md']

        if rel_path == '.':
            root_files = sorted(md_files)
        else:
            # Use the relative path as the category name
            cat_name = rel_path.replace('\\', '/')
            categories[cat_name] = sorted(md_files)

    # Add root files
    if root_files:
        readme_content.append("## \n\n")
        for f in root_files:
            name = os.path.splitext(f)[0]
            readme_content.append(f"* 🔥[{name}](.//{f})\n")
        readme_content.append("\n")

    # Add categories
    sorted_cats = sorted(categories.keys())
    for cat in sorted_cats:
        if not categories[cat]:
            continue
        readme_content.append(f"## {cat}\n\n")
        for f in categories[cat]:
            name = os.path.splitext(f)[0]
            # Fix path for markdown link
            path = f"./{cat}/{f}"
            readme_content.append(f"* 🔥[{name}]({path})\n")
        readme_content.append("\n")

    with open('README.md', 'w', encoding='utf-8') as f:
        f.writelines(readme_content)

if __name__ == '__main__':
    generate_readme()