from abc import ABC, abstractmethod



class HTMLNode:
    def __init__(self,tag =  None,value = None,children = None,props = None):
        self.tag = tag
        self.value = value
        self.children = children or []
        self.props = props or {}
        pass
    '''
    def render(self):
        if self.tag is None:
            return self.value or ""
        
        props_str = " ".join(f"{key}=\"{value}\"" for key,value in self.props.items())
        open_tag = f"<{self.tag}{' '+props_str if props_str else ''}>"

        if self.children:
            children_str = "".join(child.render() for child in self.children)
            return f"{open_tag}{children_str}</{self.tag}>"
        elif self.value is not None:
            return f"{open_tag}{self.value}</{self.tag}>"
        else:
            return f"{open_tag}</{self.tag}>"
    '''
    @abstractmethod
    def to_html(self):
        opening_tag = f"<{self.tag}"
        if self.props:
            opening_tag+=" "+" ".join(f'{key}="{value}"' for key, value in self.props.items())
        #props_str = " ".join(f'{key}="{value}"' for key,value in self.props.items())
        opening_tag +='>'
        closing_tag = f"</{self.tag}>"
        children_html = "".join(child.to_html() for child in self.children) if self.children else ''
        return f"{opening_tag}{children_html}{closing_tag}"
    
    def props_to_html(self):

        return " ".join(f'{key}="{value}"' for key, value in self.props.items())
    
    def __repr__(self):
        return (
            f"HTMLNode(tag={repr(self.tag)}, value={repr(self.value)}, "
            f"children={repr(self.children)}, props={repr(self.props)})"
        )
        pass
