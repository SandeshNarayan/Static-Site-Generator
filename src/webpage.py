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