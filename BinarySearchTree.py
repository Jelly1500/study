class TreeNode:
    def __init__(self, value, left, right):
        self.item = value
        self.left = left
        self.right = right

class BinarySearchTree:
    def __init__(self):
        self.__root = None
    
    # item 값을 검색하는 함수
    def search(self, item):
        return self.searchItem(self.__root, item)
    # 이진 검색 트리에서 item 값을 검색하는 함수
    def searchItem(self, treeNode, item):
        # 값을 찾을 수 없다면 (treeNode가 없다면)
        if treeNode == None:
            # 검색 실패(None 값을 리턴)
            return None
        # item 값이 현재 노드의 item 값보다 작다면
        elif treeNode.item > item:
            # 현재 노드의 왼쪽 자식과 비교한다(searchItem 함수에서 노드를 왼쪽 자식 노드로 바꾸면서 재귀)
            return self.searchItem(treeNode.left, item)
        # 원하던 노드를 찾았다면
        elif treeNode.item == item:
            # 현재 노드를 반환
            return treeNode
        # item 값이 현재 노드의 item 값보다 크다면
        else:
            # 현재 노드의 오른쪽 자식과 비교를 한다.(searchItem 함수에서 노드를 오른쪽 자식 노드로 바꾸면서 재귀)
            return self.searchItem(treeNode.right, item)
        
    # item 값을 삽입하는 함수
    def insert(self, item):
        self.__root = self.__insertItem(self.__root, item)
    
    def __insertItem(self, tNode:TreeNode, item) -> TreeNode:
        # 현재 참조하는 노드가 없는 경우
        if tNode == None:
            # item을 키값으로 가지고, 자식 노드가 없는 새로운 노드를 생성한다.
            tNode = TreeNode(item, None, None)
        # 같은 키값이 이미 존재하는 경우
        elif item == tNode.item:
            # 삽입 실패
            return None
        # 삽입할 키값보다 현재 노드의 키값이 큰 경우
        elif item < tNode.item:
            # 왼쪽 노드를 참조하면서 재귀
            tNode.left = self.__insertItem(tNode.left, item)
        # 삽입할 키값보다 현재 노드의 키값이 작은 경우
        else:
            # 오른쪽 노드를 참조하면서 재귀
            tNode.right = self.__insertItem(tNode.right, item)
        # 현재 TreeNode를 전달
        return tNode
    
    # item 값을 삭제하는 함수
    def delete(self, x):
        self.__root = self.__deleteItem(self.__root, x)

    def __deleteItem(self, tNode:TreeNode, x) -> TreeNode:
        # 제거할 노드가 없는 경우
        if tNode == None:
            # 제거 실패
            return None
        # 제거할 노드에 도달할 경우
        elif x == tNode.item:
            # tNode를 제거
            tNode = self.__deleteNode(tNode)
        # 제거할 노드의 아이템이 현재 가리키는 노드보다 작다면
        elif x < tNode.item :
            # 현재 노드의 왼쪽 서브트리를 탐색(재귀)
            tNode.left = self.__deleteItem(tNode.left, x)
        else:
            # 현재 노드의 오른쪽 서브트리를 탐색(재귀)
            tNode.right = self.__deleteItem(tNode.right, x)
        # root에 최종적으로 변경된 값 전달
        return tNode
    

    def __deleteNode(self, tNode:TreeNode) -> TreeNode:
        # case 1. 자식이 아예 없는 노드인 경우
        if tNode.left == None and tNode.right == None:
            # 해당 노드 삭제
            return None
        # case 2. 자식이 하나 있는 경우
        # 오른쪽 자식만 있는 경우
        elif tNode.left == None:
            # tNode.right를 반환, 그러면 tNode = tNode.right가 되므로 해당 노드는 삭제되고 그 자리에 tNode.right를 집어 넣게 된다.
            # 결국 BST 구조를 유지할 수 있게 된다.
            return tNode.right
        # 왼쪽 자식만 있는 경우
        elif tNode.right == None:
            # tNode.left를 반환. 이 경우에도 BST 구조를 유지하기 위해 해당 노드를 삭제하고, 그 자리에 tNode.left를 집어 넣는다.
            return tNode.left
        # case 3. 자식이 둘일 경우
        else:
            # 오른쪽 서브트리 중에서 가장 작은 키값과 그 노드를 찾아서 튜플로 입력받는다.
            (rtnItem, rtnNode) = self.__deleteMinItem(tNode.right)
            # 현재 노드의 키값을 rtnItem으로 바꾸고,
            tNode.item = rtnItem
            # 현재 노드를 rtnNode로 바꾼다. 즉 삭제한 노드의 자리에 직후원소를 집어 넣는다
            tNode = rtnNode
            # 트리의 변경 사항을 반환한다.
            return tNode
        
    # 해당 트리에서 가장 작은 값을 반환하는 함수
    def __deleteMinItem(self, tNode:TreeNode) -> tuple:
        # 현재 노드의 왼쪽 자식이 없다면 (가장 작은 값에 도달했다면)
        if tNode.left == None:
            # 그 값과 노드를 튜플로 반환
            return (tNode.item, tNode)
        # 아직 도달하지 못했다면
        else:
            # 계속 현재 노드의 좌측 자식으로 검색을 반복(재귀)
            (rtnItem, rtnNode) = self.__deleteMinItem(tNode.left)
            # 직후노드를 찾는 조건 자체가 왼쪽 노드가 없어야 하기 때문에 직후노드는 왼쪽 자식이 존재하지 않음
            # 직후노드를 삭제한 자리를 직후노드의 오른쪽 자식노드로 채워준다.
            tNode.left = rtnNode.right

            return (rtnItem, tNode)
        
    # 전위 순회 함수 : 루트 노드부터 전위 순회 시작!
    def pre_order_traverse(self):
        self.pre_order_trav(self.__root)

    # 전위 순회 : 현재 노드를 가장 먼저 방문(출력)하고, 그 다음에 왼쪽, 오른쪽 순서로 방문
    def pre_order_trav(self, tNode):
        if tNode != None:   # 현재 노드에 아이템이 존재한다면 
            print(tNode.item, end=" ")  # 방문했다는 증거를 남긴다(출력)
        if tNode.left != None:  # 현재 노드의 왼쪽 자식 노드가 존재한다면
            self.pre_order_trav(tNode.left) # 왼쪽 자식 노드로 전위 순회를 한다(재귀)
        if tNode.right != None: # 현재 노드의 오른쪽 자식 노드가 존재한다면
            self.pre_order_trav(tNode.right)    # 오른쪽 자식 노드로 전위 순회를 한다(재귀)

    # 중위 순회 함수 : 루트 노드부터 중위 순회 시작
    def in_order_traverse(self):
        self.in_order_trav(self.__root)
    # 중위 순회 : 왼쪽 자식노드를 가장 먼저 방문하고 그다음 현재 노드, 오른쪽 순서대로 방문(출력)한다.
    def in_order_trav(self, tNode):
        if tNode.left != None:  # 현재 노드의 왼쪽 자식 노드가 존재한다면
            self.in_order_trav(tNode.left)  # 왼쪽 자식 노드로 중위 순회를 한다(재귀)
        if tNode != None:   # 현재 노드에 아이템이 존재한다면
            print(tNode.item, end=" ")  # 방문했다는 증거를 남긴다(출력)
        if tNode.right != None: # 현재 노드의 오른쪽 자식 노드가 존재한다면
            self.in_order_trav(tNode.right) # 오른쪽 자식 노드로 중위 순회를 한다(재귀)

    # 후위 순회 함수 : 루트 노드부터 후위 순회 시작
    def post_order_traverse(self):
        self.post_order_trav(self.__root)
    # 후위 순회 : 왼쪽 자식노드, 오른쪽 자식노드를 모두 방문한 후에 현재 노드를 방문(출력)한다.
    def post_order_trav(self, tNode):
        if tNode.left != None:  # 현재 노드의 왼쪽 자식 노드가 존재한다면
            self.post_order_trav(tNode.left)    # 왼쪽 자식 노드로 후위 순회를 한다(재귀)
        if tNode.right != None: # 현재 노드의 오른쪽 자식 노드가 존재한다면
            self.post_order_trav(tNode.right)   # 오른쪽 자식 노드로 후위 순회를 한다(재귀)
        if tNode != None:   # 현재 노드에 아이템이 존재한다면
            print(tNode.item, end=" ")  # 방문했다는 증거를 남긴다(출력)

        
if __name__ == "__main__":
    bst1 = BinarySearchTree()
    a = [55, 15, 60, 8, 28, 90, 3, 18, 45, 41, 48, 30, 50, 38, 33, 32, 36]
    for i in a:
        bst1.insert(i)
    bst1.pre_order_traverse()
    print()
    bst1.in_order_traverse()
    print()
    bst1.post_order_traverse()
