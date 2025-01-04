from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children = None , props=None):

        if not tag :
            raise ValueError("ParentNode must have a tag.")
        if not children or not all(isinstance(child, HTMLNode) for child in children):
            raise ValueError("ParentNode must have atleast one child.")

        if not isinstance(children,list):
            raise TypeError("Children must be a list.")
        super().__init__(tag = tag, value = None, children= children, props=props)

    def to_html(self):
        if not self.tag:
            raise ValueError("ParentNode must have a tag.")
        if not self.children:
            raise ValueError("ParentNode must have atleast one child.")

        props_str = self.props_to_html() if self.props else ''
        open_tag = f"<{self.tag}{' '+props_str if props_str else ''}>"

        children_str = "".join(child.to_html() for child in self.children)
        return f"{open_tag}{children_str}</{self.tag}>"
    
    def __repr__(self):
        
        return self.to_html()