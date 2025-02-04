from textnode import TextNode, TextType
from clone_directory import clone_directory
def main():
    clone_directory("public", "static") 
    node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
    print(node)

main()