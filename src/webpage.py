import os
from markdown_blocks import markdown_to_html_node

def extract_title(markdown):
    # return None if no title found
    lines = markdown.split("\n")
    for line in lines:
        if line.strip().startswith("# "):
            return line.strip()[2:]
    return None


def generate_page(from_path, template_path, dest_path):
    print("Generating page from {from_path} to {dest_path} using {template_path}")

    try:
        with open(from_path, 'r') as f:
            markdown = f.read()
            f.close()
        
        with open(template_path, 'r') as f:
            template = f.read()
            f.close()
    
    except Exception as e:
        print(f"Error: Unable to read file: {str(e)}")
        return
    
    content = markdown_to_html_node(markdown).to_html()
    title = extract_title(markdown)
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", content)
    
    try:
        with open(dest_path, "w") as f:
            f.write(template)
    except Exception as e:
        print(f"Error: Unable to write to file: {str(e)}")

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    
    for root, _, files in os.walk(dir_path_content):
        for file in files:

            if file.endswith(".md"):
                
                from_path = os.path.join(root, file)
                rel_path = os.path.relpath(from_path, dir_path_content)
                dest_path = os.path.join(dest_dir_path, os.path.splitext(rel_path)[0] + ".html")
                os.makedirs(os.path.dirname(dest_path), exist_ok=True)
                generate_page(from_path, template_path, dest_path)
            