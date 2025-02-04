import re
from htmlnode import HTMLNode
from textnode import *
from parentnode import ParentNode
from inline_markdown import text_to_textnodes

def markdown_to_blocks(markdown):

    blocks = markdown.split("\n\n")
    blocks = [block.strip() for block in blocks if block]

    return blocks

def block_to_block_type(block):

    lines = block.split("\n")
    if re.match(r"^#{1,6} ", lines[0]):
        return "heading"

    if len(lines)>1 and lines[0].startswith("```") and lines[-1].startswith("```"):
        return "code"
    
    if all(re.match(r"^\* ", line) or re.match(r"^- ", line) for line in lines):
        return "unordered_list"
    
    if re.match(r"^1. ", lines[0]):
        number = 1
        for line in lines:
            if re.match(f"^{number}. ", line):
                number += 1
            else:
                return "paragraph"
        return "ordered_list"
    
    if all(re.match(r"^> ", line) for line in lines):
        return "quote"
    
    return "paragraph"

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children_nodes = []

    for block in blocks:
        html_node = block_to_html_node(block)
        children_nodes.append(html_node)
        

    return ParentNode("div", children_nodes, None)

def block_to_html_node(block):
    block_type = block_to_block_type(block)
    if block_type == "heading":
        return heading_to_html_node(block)
    elif block_type == "code":
        return code_to_html_node(block)
    elif block_type == "unordered_list":
        return ul_to_html_node(block)
    elif block_type == "ordered_list":
        return ol_to_html_node(block)
    elif block_type == "quote":
        return quote_to_html_node(block)
    else:
        return paragraph_to_html_node(block)
    
def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children = []
    for text_node in text_nodes:
        children.append(text_node_to_html_node(text_node))
    return children


def heading_to_html_node(block):
    level = len(block.split(" ")[0])
    text = block[level+1:]
    children = text_to_children(text)
    return ParentNode(f"h{level}", children)

def code_to_html_node(block):
    text = block[4:-3]
    children = text_to_children(text)
    return ParentNode("pre", children)

def ul_to_html_node(block):
    items = block.split("\n")
    html_nodes = []
    for item in items:
        children = text_to_children(item[2:])
        html_nodes.append(ParentNode("li", children))
    return ParentNode("ul", html_nodes)

def ol_to_html_node(block):
    items = block.split("\n")
    html_nodes = []
    for item in items:
        children = text_to_children(item[3:])
        html_nodes.append(ParentNode("li", children))
    return ParentNode("ol", html_nodes)


def quote_to_html_node(block):
    lines = block.split("\n")
    new_lines = []
    for line in lines:
        new_lines.append(line.lstrip(">").strip())
    text = " ".join(new_lines)
    children = text_to_children(text)
    return ParentNode("blockquote", children)

def paragraph_to_html_node(block):
    lines = block.split("\n")
    paragraph = " ".join(lines)
    children = text_to_children(paragraph)
    return ParentNode("p", children)



        
    
