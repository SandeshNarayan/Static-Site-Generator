from textnode import TextNode, TextType
import re
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes=[]
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        
        split_nodes = []
        split_text = old_node.text.split(delimiter)
        if len(split_text)%2==0:
            raise ValueError("Invalid markdown, formatted section not closed")
        for i in range(len(split_text)):
            if split_text[i]=="":
                continue
            if i%2==0:
                split_nodes.append(TextNode(split_text[i], TextType.TEXT))

            else:
                split_nodes.append(TextNode(split_text[i], text_type))
        new_nodes.extend(split_nodes)        
    return new_nodes 

def extract_markdown_images(raw_text):
    pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    match = re.findall(pattern, raw_text)
    return match

def extract_markdown_links(raw_text):
    pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    match = re.findall(pattern, raw_text)
    return match



def split_nodes_image(old_nodes):
    new_nodes=[]
    for old_node in old_nodes:
        if old_node.text_type!= TextType.TEXT:
            new_nodes.append(old_node)
            continue

        original_text = old_node.text
        images = extract_markdown_images(original_text)
        if len(images)==0:
            new_nodes.append(old_node)
            continue

        for image in images:
            sections = original_text.split(f"![{image[0]}]({image[1]})",1)
            if len(sections)!=2:
                raise ValueError("Invalid markdown, formatted section not closed")
            if sections[0] !="":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(
                TextNode(image[0], TextType.IMAGE, image[1])
            )
        
            original_text = sections[1]
        if original_text!="":
            new_nodes.append(TextNode(original_text, TextType.TEXT))
    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes=[]
    for old_node in old_nodes:
        if old_node.text_type!= TextType.TEXT:
            new_nodes.append(old_node)
            continue
        original_text = old_node.text
        links = extract_markdown_links(original_text)
        if len(links)==0:
            new_nodes.append(old_node)
            continue

        for link in links:
            sections = original_text.split(f"[{link[0]}]({link[1]})",1)
            if len(sections)!=2:
                raise ValueError("Invalid markdown, formatted section not closed")
            if sections[0]!="":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(
                TextNode(link[0], TextType.LINK, link[1])
            )
            original_text = sections[1]
        if original_text!="":
            new_nodes.append(TextNode(original_text, TextType.TEXT))
    return new_nodes



def text_to_textnodes(text):
    
    nodes = [TextNode(text, TextType.TEXT)]
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "*", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)

    return nodes
    
    
        
        
