

class Node:
    def __init__(self, value, children):
        """
        Token:param value:
        List[Node]:param children:
        """
        self.value = value
        self.children = children

    def get_num_children(self):
        """
        Int:return:
        """
        return len(self.children);

    def get_child(self, ind):
        """
        Int:param ind:
        Node:return:
        """
        assert ind < self.get_num_children()
        return self.children[ind]

