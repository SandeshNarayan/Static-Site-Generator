import re

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
    
    if all(re.match(r"^\* ", line) for line in lines):
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

    
        
        
    
