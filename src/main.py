from textnode import TextNode, TextType
from clone_directory import clone_directory
from webpage import generate_page
def main():
    clone_directory("public", "static") 
    generate_page("content/index.md", "template.html", "public/index.html")
    node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
    print(node)

main()