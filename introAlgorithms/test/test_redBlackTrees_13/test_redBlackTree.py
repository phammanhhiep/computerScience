import logging

import pytest

from redBlackTrees_13.redBlackTree import RedBlackTree, Node, NilNode, AugmentedRBTree, AugmentedNode


@pytest.fixture
def aTree():
    tree = [Node(i) for i in range(10)]
    root = tree[5]
    root.set_left(tree[3])
    root.set_right(tree[7])
    tree[3].set_left(tree[1])
    tree[3].set_right(tree[4])
    tree[1].set_right(tree[2])
    tree[7].set_left(tree[6])
    tree[7].set_right(tree[9])
    tree[9].set_left(tree[8])

    return tree


@pytest.mark.skip
def test_RedBlackTree_right_rotate(aTree):
    rb = RedBlackTree(aTree[5])
    node = aTree[3]
    parent = node.get_parent()
    left = node.get_left()
    right_child_of_left = left.get_right()
    rb.right_rotate(node)

    assert left.equal_to(parent.get_left())
    assert left.has_right_as(node)
    assert node.has_left_as(right_child_of_left)
    assert left.has_parent_as(parent)


@pytest.mark.skip
def test_RedBlackTree_left_rotate(aTree):
    rb = RedBlackTree(aTree[5])
    node = aTree[7]
    parent = node.get_parent()
    right = node.get_right()
    left_child_of_right = right.get_left()  
    rb.left_rotate(node)

    assert right.equal_to(parent.get_right())
    assert right.has_left_as(node)
    assert node.has_right_as(left_child_of_right)
    assert right.has_parent_as(parent)


@pytest.mark.skip
def test_RedBlackTree_delete_fixup():
    logging.debug("When x is the left child: Test case 1 and case 2")
    tree = [Node(i) for i in range(10)]
    root = tree[3]
    root.set_left(tree[2])
    root.set_right(tree[7])
    tree[2].set_parent(root)
    tree[7].set_parent(root)
    tree[7].set_red()
    tree[7].set_left(tree[5])
    tree[7].set_right(tree[8])
    tree[8].set_parent(tree[7])
    tree[5].set_parent(tree[7])
    tree[5].set_left(tree[4])
    tree[5].set_right(tree[6])
    tree[4].set_parent(tree[5])
    tree[6].set_parent(tree[5])


    rb = RedBlackTree(root)
    rb.delete_fixup(tree[2])

    assert rb.root_node.equal_to(tree[7])
    assert rb.root_node.is_black()
    assert rb.root_node.has_right_as(tree[8])
    assert tree[8].is_black()
    assert rb.root_node.has_left_as(tree[3])
    assert tree[3].is_black()
    assert tree[3].has_left_as(tree[2])
    assert tree[2].is_black()
    assert tree[3].has_right_as(tree[5])
    assert not tree[5].is_black()
    assert tree[5].has_left_as(tree[4])
    assert tree[5].has_right_as(tree[6])
    assert tree[4].is_black()
    assert tree[6].is_black()


@pytest.mark.skip
def test_RedBlackTree_delete_fixup2():
    logging.debug("When x is the left child: Test case 1, case 3, and 4")
    tree = [Node(i) for i in range(10)]
    root = tree[3]
    root.set_left(tree[2])
    root.set_right(tree[7])
    tree[2].set_parent(root)
    tree[7].set_parent(root)
    tree[7].set_red()
    tree[7].set_left(tree[5])
    tree[7].set_right(tree[8])
    tree[8].set_parent(tree[7])
    tree[5].set_parent(tree[7])
    tree[5].set_left(tree[4])
    tree[5].set_right(tree[6])
    tree[4].set_parent(tree[5])
    tree[4].set_red()
    tree[6].set_parent(tree[5])


    rb = RedBlackTree(root)
    rb.delete_fixup(tree[2])

    assert rb.root_node.equal_to(tree[7])
    assert rb.root_node.is_black()
    assert rb.root_node.has_right_as(tree[8])
    assert tree[8].is_black()
    assert rb.root_node.has_left_as(tree[4])
    assert not tree[4].is_black()
    assert tree[4].has_left_as(tree[3])
    assert tree[3].is_black()
    assert tree[3].has_left_as(tree[2])
    assert tree[2].is_black()
    assert tree[4].has_right_as(tree[5])
    assert tree[5].is_black()
    assert tree[5].has_right_as(tree[6])
    assert tree[6].is_black()


@pytest.mark.skip
def test_RedBlackTree_delete_fixup3():
    logging.debug("When x is the right child: Test case 1 and case 2")
    tree = [Node(i) for i in range(10)]
    root = tree[6]
    root.set_right(tree[7])
    root.set_left(tree[2])
    tree[2].set_parent(root)
    tree[7].set_parent(root)
    tree[2].set_red()
    tree[2].set_left(tree[1])
    tree[1].set_parent(tree[2])
    tree[2].set_right(tree[5])
    tree[5].set_parent(tree[2])
    tree[5].set_left(tree[3])
    tree[5].set_right(tree[4])
    tree[3].set_parent(tree[5])
    tree[4].set_parent(tree[5])
    
    

    rb = RedBlackTree(root)
    rb.delete_fixup(tree[7])

    assert rb.root_node.equal_to(tree[2])
    assert rb.root_node.is_black()
    assert rb.root_node.has_right_as(tree[6])
    assert tree[6].is_black()
    assert rb.root_node.has_left_as(tree[1])
    assert tree[1].is_black()
    assert tree[6].has_left_as(tree[5])
    assert tree[6].is_black()
    assert tree[6].has_right_as(tree[7])
    assert not tree[5].is_black()
    assert tree[5].has_left_as(tree[3])
    assert tree[5].has_right_as(tree[4])
    assert tree[4].is_black()
    assert tree[6].is_black()


@pytest.mark.skip
def test_RedBlackTree_delete_fixup4():
    logging.debug("When x is the right child: Test case 1, and case 3 and 4")
    tree = [Node(i) for i in range(10)]
    root = tree[6]
    root.set_right(tree[7])
    root.set_left(tree[2])
    tree[2].set_parent(root)
    tree[7].set_parent(root)
    tree[2].set_red()
    tree[2].set_left(tree[1])
    tree[1].set_parent(tree[2])
    tree[2].set_right(tree[5])
    tree[5].set_parent(tree[2])
    tree[5].set_left(tree[3])
    tree[5].set_right(tree[4])
    tree[3].set_parent(tree[5])
    tree[4].set_parent(tree[5])
    tree[4].set_red()
    

    rb = RedBlackTree(root)
    rb.delete_fixup(tree[7])

    assert rb.root_node.equal_to(tree[2])
    assert rb.root_node.is_black()
    assert rb.root_node.has_right_as(tree[4])
    assert not tree[4].is_black()
    assert rb.root_node.has_left_as(tree[1])
    assert tree[1].is_black()
    assert tree[4].has_right_as(tree[6])
    assert tree[6].is_black()
    assert tree[6].has_right_as(tree[7])
    assert tree[4].has_left_as(tree[5])
    assert tree[5].is_black()
    assert tree[5].has_left_as(tree[3])
    assert tree[3].is_black()
    assert tree[7].is_black()


@pytest.mark.skip
def test_RedBlackTree_delete():
    tree = [Node(i) for i in range(10)]
    root = tree[6]
    root.set_right(tree[8])
    root.set_left(tree[2])
    tree[2].set_parent(root)
    tree[8].set_parent(root)
    tree[2].set_red()
    tree[8].set_red()
    tree[8].set_left(tree[7])
    tree[8].set_right(tree[9])
    tree[7].set_parent(tree[8])
    tree[9].set_parent(tree[8])
    tree[2].set_left(tree[1])
    tree[1].set_parent(tree[2])
    tree[2].set_right(tree[5])
    tree[5].set_parent(tree[2])
    tree[5].set_left(tree[3])
    tree[5].set_right(tree[4])
    tree[3].set_parent(tree[5])
    tree[4].set_parent(tree[5])
    tree[4].set_red()   
    tree[3].set_red()

    rb = RedBlackTree(root)
    rb.delete(tree[8])

    assert rb.root_node.equal_to(tree[6])
    assert rb.root_node.has_left_as(tree[2])
    assert rb.root_node.has_right_as(tree[9])
    assert tree[9].has_left_as(tree[7])
    assert not tree[9].has_right()
    assert tree[9].is_black()
    assert not tree[7].is_black()
    assert tree[7].has_parent_as(tree[9])


@pytest.mark.skip
def test_RedBlackTree_get_minimum():

    logging.info("When the tree is empty")
    root = NilNode()
    rb = RedBlackTree(root)

    try:
        min_node = rb.get_minimum()
        logging.debug("The function should throw exception, and the message should never appear. Min node: {}".format(min_node.get_key()))
    except ValueError as e:
        assert True
    else:
        assert False

    logging.info("When tree is not empty and the min node is an internal node")
    tree = [Node(i) for i in range(10)]
    root = tree[6]
    root.set_left(tree[5])
    tree[5].set_parent(root)
    rb = RedBlackTree(root)
    min_node = rb.get_minimum()
    
    assert min_node.equal_to(tree[5])

    logging.info("When the tree is not empty, and the min node is an parent whose left child is a NIL and right child is an internal node")
    tree = [Node(i) for i in range(10)]
    root = tree[6]
    root.set_left(tree[4])
    tree[4].set_parent(root)
    tree[4].set_right(tree[5])
    tree[5].set_parent(tree[4])
    rb = RedBlackTree(root)
    min_node = rb.get_minimum()
    
    assert min_node.equal_to(tree[4])   


@pytest.mark.skip
def test_RedBlackTree_insert_fixup():
    logging.debug("When parent of the inserted node is left child. Case 1: uncle of the node is red")
    tree = [Node(i) for i in range(10)]
    root = tree[6]
    root.set_left(tree[4])
    root.set_right(tree[7])
    tree[4].set_parent(root)
    tree[7].set_parent(root)
    tree[7].set_red()
    tree[4].set_red()
    tree[4].set_left(tree[3])
    tree[3].set_parent(tree[4])
    tree[3].set_red()

    rb = RedBlackTree(root)
    rb.insert_fixup(tree[3])

    assert rb.root_node.equal_to(tree[6])
    assert rb.root_node.is_black()
    assert tree[4].is_black()
    assert tree[7].is_black()


@pytest.mark.skip
def test_RedBlackTree_insert_fixup2():
    logging.debug("When parent of the inserted node is left child. Case 2 and case 3")
    tree = [Node(i) for i in range(10)]
    root = tree[6]
    root.set_left(tree[2])
    root.set_right(tree[7])
    tree[2].set_parent(root)
    tree[7].set_parent(root)
    tree[2].set_red()
    tree[2].set_left(tree[1])
    tree[2].set_right(tree[4])
    tree[4].set_parent(tree[2])
    tree[4].set_red()
    tree[4].set_left(tree[3])
    tree[4].set_right(tree[5])


    rb = RedBlackTree(root)
    rb.insert_fixup(tree[4])

    assert rb.root_node.equal_to(tree[4])
    assert rb.root_node.is_black()
    assert rb.root_node.has_left_as(tree[2])
    assert rb.root_node.has_right_as(tree[6])
    assert tree[6].has_right_as(tree[7])
    assert tree[6].has_left_as(tree[5])
    assert tree[2].is_red()
    assert tree[6].is_red()
    assert tree[7].is_black()
    assert tree[5].is_black()


@pytest.mark.skip
def test_RedBlackTree_insert_fixup3():
    logging.debug("When parent of the inserted node is right child. Case 2 and Case 3")
    tree = [Node(i) for i in range(10)]
    root = tree[2]
    root.set_left(tree[1])
    root.set_right(tree[6])
    tree[6].set_red()
    tree[6].set_right(tree[7])
    tree[6].set_left(tree[4])
    tree[4].set_red()
    tree[4].set_left(tree[3])
    tree[4].set_right(tree[5])

    rb = RedBlackTree(root)
    rb.insert_fixup(tree[4])

    assert rb.root_node.equal_to(tree[4])
    assert rb.root_node.is_black()
    assert rb.root_node.has_left_as(tree[2])
    assert rb.root_node.has_right_as(tree[6])
    assert tree[6].has_right_as(tree[7])
    assert tree[6].has_left_as(tree[5])
    assert tree[6].is_red()
    assert tree[2].is_red()     
    assert tree[7].is_black()
    assert tree[5].is_black()


@pytest.mark.skip
def test_RedBlackTree_insert():
    logging.debug("Insert a node and test insert_fixup case 2 and 3")
    tree = [Node(i) for i in range(10)] 
    root = tree[2]
    root.set_left(tree[1])
    root.set_right(tree[7])
    tree[7].set_right(tree[8])
    tree[7].set_left(tree[5])
    tree[5].set_right(tree[6])
    tree[5].set_left(tree[4])
    tree[4].set_red()
    tree[6].set_red()
    tree[7].set_red()

    rb = RedBlackTree(root)
    keys = rb.inorder_tree_walk()

    expected_keys = [1,2,4,5,6,7,8]

    assert len(expected_keys) == len(keys)
    for i,j in zip(keys, expected_keys):
        assert i == j

    rb.insert(tree[3])

    assert rb.root_node.equal_to(tree[5])
    assert rb.root_node.has_left_as(tree[2])
    assert rb.root_node.has_right_as(tree[7])
    assert rb.root_node.is_black() and tree[2].is_red() and tree[7].is_red() and tree[3].is_red()
    assert tree[2].has_left_as(tree[1])
    assert tree[2].has_right_as(tree[4])
    assert tree[4].has_left_as(tree[3])
    assert tree[7].has_right_as(tree[8])
    assert tree[7].has_left_as(tree[6])


@pytest.mark.skip
def test_RedBlackTree_inorder_tree_walk():
    tree = [Node(i) for i in range(10)]
    root = tree[5]
    root.set_left(tree[1])
    root.set_right(tree[8])
    tree[2].set_left(tree[1])
    tree[2].set_right(tree[4])
    tree[8].set_left(tree[7])


    rb = RedBlackTree(root)

    keys = rb.inorder_tree_walk()

    expected_keys = [1,2,4,5,7,8]
    for i,j in zip(keys, expected_keys):
        assert i == j


@pytest.mark.skip
def test_AugmentedRBTree_select_by_rank():
    tree = [AugmentedNode(i) for i in range(10)]
    root = tree[2]
    root.set_size(6)
    root.set_left(tree[1])
    root.set_right(tree[6])
    tree[6].set_size(4)
    tree[6].set_left(tree[5])
    tree[5].set_size(3)
    tree[5].set_left(tree[3])
    tree[3].set_size(2)
    tree[3].set_right(tree[4])

    arb = AugmentedRBTree(root)
    node = arb.select_by_rank(3)

    assert node.equal_to(tree[3])


@pytest.mark.skip
def test_AugmentedRBTree_get_rank():
    tree = [AugmentedNode(i) for i in range(10)]
    root = tree[2]
    root.set_size(6)
    root.set_left(tree[1])
    root.set_right(tree[6])
    tree[6].set_size(4)
    tree[6].set_left(tree[5])
    tree[5].set_size(3)
    tree[5].set_left(tree[3])
    tree[3].set_size(2)
    tree[3].set_right(tree[4])

    arb = AugmentedRBTree(root)
    rank = arb.get_rank(tree[5])
    expected_rank = 5

    assert rank == expected_rank


@pytest.mark.skip
def test_AugmentedRBTree_maintain_size():
    tree = [AugmentedNode(i) for i in range(10)]
    root = tree[2]
    root.set_left(tree[1])
    root.set_right(tree[6])
    tree[6].set_left(tree[5])
    tree[5].set_left(tree[3])
    tree[3].set_right(tree[4])

    arb = AugmentedRBTree(root)

    assert arb.root_node.get_size() == 6
    assert tree[1].get_size() == 1
    assert tree[6].get_size() == 4
    assert tree[5].get_size() == 3
    assert tree[3].get_size() == 2
    assert tree[4],get_size() == 1
    assert tree[3].get_left().get_size() == 0


@pytest.mark.skip
def test_AugmentedRBTree_right_rotate():
    tree = [AugmentedNode(i) for i in range(10)]
    root = tree[2]
    root.set_left(tree[1])
    root.set_right(tree[6])
    tree[6].set_left(tree[5])
    tree[5].set_left(tree[3])
    tree[3].set_right(tree[4])

    arb = AugmentedRBTree(root)
    arb.right_rotate(tree[6])

    assert tree[6].get_size() == 1
    assert tree[5].get_size() == 4


@pytest.mark.skip
def test_AugmentedRBTree_left_rotate():
    tree = [AugmentedNode(i) for i in range(10)]
    root = tree[2]
    root.set_left(tree[1])
    root.set_right(tree[6])
    tree[6].set_left(tree[5])
    tree[5].set_left(tree[3])
    tree[3].set_right(tree[4])

    arb = AugmentedRBTree(root)
    arb.left_rotate(tree[2])

    assert arb.root_node.equal_to(tree[6])
    assert tree[6].get_size() == 6
    assert tree[2].get_size() == 5


@pytest.mark.skip
def test_Node_has_parent():
    node = NilNode()
    assert not node.has_parent()
    assert node.get_key() is None