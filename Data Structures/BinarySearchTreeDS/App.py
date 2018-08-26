from BinarySearchTreeDS.BST import BST;
binaryTree=BST()

binaryTree.insert(12)
binaryTree.insert(10)
binaryTree.insert(-2)
binaryTree.insert(10)
binaryTree.insert(-2)
binaryTree.traverseInOrder()
binaryTree.remove(-2)
binaryTree.remove(10)
binaryTree.remove(-2)
binaryTree.remove(10)
binaryTree.remove(12)
print("this is after remove")

binaryTree.traverseInOrder()


