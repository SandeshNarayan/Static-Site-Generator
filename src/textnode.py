from enum import Enum

class TextType(Enum):
    NORMAL_TEXT = 'normal'
    BOLD_TEXT = 'bold'
    ITALIC_TEXT = 'italic'
    CODE_TEXT = 'code'
    LINKS = 'link'
    IMAGES = 'image'

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = TextType(text_type)
        self.url = url
        pass
    
    
    def __eq__(self, other):
        return isinstance(other, TextNode) and self.text == other.text and self.text_type == other.text_type and self.url == other.url
        pass

    def __repr__(self):
        return f"TextNode(text='{self.text}', text_type='{self.text_type.value}', url={self.url})"
        
        pass