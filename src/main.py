from textnode import TextNode, TextType
from clone_directory import clone_directory
from webpage import generate_pages_recursive
def main():
    clone_directory("public", "static") 
    generate_pages_recursive("content", "template.html", "public")
    node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
    print(node)

main()