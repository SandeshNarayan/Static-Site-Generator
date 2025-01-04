from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props = None):
        if value is None:
            raise ValueError("LeafNode must have a value")
        super().__init__(tag=tag, value=value, children=None, props=props)
        pass

    def to_html(self):

        if not self.value:
            raise ValueError("LeafNode must have a value.")

        
        if self.tag is None:
            return self.value
        
        props_str = " ".join(f'{key}="{value}"' for key, value in self.props.items())
        open_tag = f"<{self.tag}{(' '+props_str) if props_str else ''}>"

        return f"{open_tag}{self.value}</{self.tag}>"
            
    def __repr__(self):
        return f"LeafNode(tag='{self.tag}', value='{self.value}', props={self.props})"
