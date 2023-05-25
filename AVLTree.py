class Node:
    def __init__(self, newItem, height, left=None, right=None):
        self.key = newItem
        self.left= left
        self.right = right
        self.height = height

class AVLTree:
    def __init__(self):
        self.root = None
    def height(self, tNode):
        if tNode == None:
            return 0
        return tNode.height
    
    def insert(self, key):
        self.root = self.insertItem(self.root, key)
    def insertItem(self, tNode, key):
        if tNode == None:
            return Node(key, 1)
        if tNode.key > key:
            tNode.left = self.insertItem(tNode.left,key)
        elif tNode.key < key:
            tNode.right = self.insertItem(tNode.right,key)
        tNode.height = 1+max(self.height(tNode.left), self.height(tNode.right))
        return self.balance(tNode)
    
    def delete(self, key):
        self.root = self.deleteItem(self.root, key)
    def deleteItem(self, tNode, key):
        if tNode == None:
            return None
        if tNode.key == key:
            return self.deleteNode(tNode)
        elif tNode.key > key:
            tNode.left = self.deleteItem(tNode.left,key)
        elif tNode.key < key:
            tNode.right = self.deleteItem(tNode.right, key)
        tNode.height = 1 + max(self.height(tNode.left), self.height(tNode.right))
        return self.balance(tNode)

    def deleteNode(self, tNode):
        # 삭제할노드의 자식이 하나도없는 경우
        if tNode.left == None and tNode.right == None:
            return None
        elif tNode.left != None:    # 삭제할 노드의 왼쪽에만 서브트리 있으면
            return tNode.left   # 왼쪽 래퍼런스 반환
        elif tNode.right != None:   # 삭제할 노드의 오른쪽에만 서브트리 있으면
            return tNode.right  # 오른쪽 래퍼런스 반환
        else:
            (rtnKey, rtnNode) = self.deleteMinNode(tNode.right)
            tNode.key = rtnKey
            tNode.right = rtnNode
            tNode.height = 1 + max(self.height(tNode.left), self.height(tNode.right))
            tNode = self.balance(tNode)
            return tNode

    def deleteMinNode(self, tNode):
        if tNode.left == None:
            return (tNode.item, tNode.right)
        else:
            (rtnKey, rtnNode) = self.deleteMinNode(tNode.left)
            tNode.left = rtnNode
            tNode.height = 1 + max(self.height(tNode.left), self.height(tNode.right))
            tNode = self.balance(tNode)
        return (rtnKey, rtnNode)


    def balance(self, tNode):
        if self.bf(tNode) >= 2: # 왼쪽이 오른쪽보다 2이상 더 깊을때
            if self.bf(tNode.left) <= -1:
                tNode.left = self.rotate_left(tNode.left)
            tNode = self.rotate_right(tNode)
        elif self.bf(tNode) <= -2: # 오른쪽이 왼쪽보다 2이상 더 깊을때
            if self.bf(tNode.right) >= 1:
                tNode.right = self.rotate_right(tNode.right)
            tNode = self.rotate_left(tNode)
        return tNode

    def bf(self, tNode):
        return self.height(tNode.left) - self.height(tNode.right)

    def rotate_right(self, tNode):
        LChild = tNode.left
        tNode.left = LChild.right
        LChild.right = tNode
        tNode.height = 1 + max(self.height(tNode.left), self.height(tNode.right))
        LChild.height = 1 + max(self.height(LChild.left), self.height(LChild.right))
        return LChild
    
    def rotate_left(self, tNode):
        RChild = tNode.right
        tNode.right = RChild.left
        RChild.left = tNode
        tNode.height = 1 + max(self.height(tNode.left), self.height(tNode.right))
        RChild.height = 1 + max(self.height(RChild.left), self.height(RChild.right))
        return RChild
    
    def preOrderTrav(self, tNode):
        print(str(tNode.key), end=" ")
        if tNode.left:
            self.preOrderTrav(tNode.left)
        if tNode.right:
            self.preOrderTrav(tNode.right)

    def inOrderTrav(self, tNode):
        if tNode.left:
            self.inOrderTrav(tNode.left)
        print(tNode.key, end=" ")
        if tNode.right:
            self.inOrderTrav(tNode.right)

    def postOrderTrav(self, tNode):
        if tNode.left:
            self.postOrderTrav(tNode.left)
        if tNode.right:
            self.preOrderTrav(tNode.right)
        print(tNode.key, end=" ")
    
if __name__ == "__main__":
    avl1 = AVLTree()
    a = [10,20,30,40,50,29]
    for i in a:
        avl1.insert(i)
    avl1.delete(50)
    avl1.preOrderTrav(avl1.root)
    print()
    avl1.inOrderTrav(avl1.root)
    print()
    avl1.postOrderTrav(avl1.root)
