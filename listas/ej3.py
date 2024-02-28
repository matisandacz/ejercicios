def reverse_list(l: List):
    l.head = reverse(l.head)
    return l

def reverse(n: Node):
    if(not n or not n.next_node):
        return n

    rev = reverse(n.next_node)
    n.next_node.next_node = n
    n.next_node = None
    return rev