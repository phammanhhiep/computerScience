import logging

from elementaryDataStructures_10 import stack, linkedlist

logging.basicConfig(filename="inoderTreeWalk.log", level=logging.DEBUG)


def inoderTreeWalk1(root_node):
    # Nonrecursive version
    s = stack.Stack(100)
    a = []
    while root_node is not None:
        if root_node.has_right():
            s.push(root_node.get_right())
        s.push(root_node)
        if root_node.has_left():
            left = root_node.get_left()
            s.push(left)
            root_node = left
        else:
            a.append(root_node.get_key())
            try:
                s.pop()
                root_node = s.pop()
            except Exception as e:
                logging.debug("Stack is empty. Set root as None.")
                root_node = None
    return a


  