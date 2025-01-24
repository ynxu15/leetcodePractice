

class Node():
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BiTree:

    def __init__(self):
        self.root = None

    def traverse(self, root: Node):
        if root is None:
            return
        # 先序遍历操作

        self.traverse(root.left)

        # 中序遍历操作

        self.traverse(root.right)

        # 后序遍历操作

    def levelOrderTraverse(self):
        if self.root is None:
            return
        from collections import deque
        q = deque()
        q.append(self.root)
        while q:
            cur = q.popleft()
            print(cur.val)

            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)


    def levelOrderTraverse2(self):
        '''记录深度'''
        if self.root is None:
            return
        from collections import deque
        q = deque()
        q.append(self.root)
        depth = 1
        while q:
            sz = len(q)
            for i in range(sz):
                cur = q.popleft()
                print(f'depth = {depth}, val={cur.val}')

                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            depth += 1

    def levelOrderTraverse3(self):
        '''记录更多信息'''
        class State:
            def __init__(self, node, depth):
                self.node = node
                self.depth = depth
        if self.root is None:
            return
        from collections import deque
        q = deque()
        q.append(State(self.root, 1))
        while q:
            cur = q.popleft()
            print(f'depth = {cur.depth}, val={cur.val}')

            if cur.node.left:
                q.append(State(cur.left, cur.depth+1))
            if cur.node.right:
                q.append(State(cur.right, cur.depth+1))

    def isEmpty(self):
        return not self.root

    def addNode(self, val):
        '''满二叉树的形式插入'''
        node = Node(val)

        if self.root is None:
            self.root = node
            return

        queue = [self.root]
        while queue:
            curr = queue.pop(0)
            if curr.left == None:
                curr.right = node
                return
            else:
                queue.append(curr.left)

            if curr.left == None:
                curr.right = None
                return
            else:
                queue.append(curr.right)

    def __preOrderAccess(self, node):
        if node == None:
            return

        print(node.val, end = " ")
        self.__preOrderAccess(node.left)
        self.__preOrderAccess(node.right)
    def preOrderTraverse(self):
        return self.__preOrderAccess(self.root)
    def preOrderTraverse1(self):
        '''非递归形式'''
        if not self.root:
            return
        stack = [self.root]
        while stack:
            node = stack.pop()
            print(node.val, end=" ")
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

    def __postOrderAccess(self, node):
        if node == None:
            return
        self.__postOrderAccess(node.left)
        self.__postOrderAccess(node.right)
        print(node.val, end=" ")

    def postOrderTraverse(self):
        return self.__postOrderAccess(self.root)
    def postOrderTraverse1(self):
        '''非递归形式的打印'''
        if not self.root:
            return
        stack = [self.root]
        accessed = set()
        while stack:
            node = stack[-1]
            if node in accessed:
                node = stack.pop()
                print(node.val, "  ")
            else:
                if node.right:
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)
                accessed.add(node)

    def postOrderTraverse2(self):
        '''非递归形式的打印，使用一个前指针解决'''
        if not self.root:
            return

        curr = None
        pre_curr = None # 当前节点之前访问的那个节点
        # 首先找到最左的那个节点
        stack = []
        curr = self.root
        while curr != None:
            stack.append(curr)

        while stack:
            curr = stack.pop()
            if curr.right == None or curr.right == pre_curr:
                # 没有右孩子，或者右孩子已经被访问过了，就可以打印当前节点
                print(curr.val, end=" ")
                pre_curr = curr
            else:
                # 有右孩子，且没有被访问过的情况
                stack.append(curr)
                curr = curr.right
                while curr:
                    stack.append(curr)
                    curr = curr.right

    def __midOrderAccess(self, node):
        if node == None:
            return
        self.__midOrderAccess(node.left)
        print(node.val, end=" ")
        self.__midOrderAccess(node.right)
    def midOrderTraverse(self):
        return self.__midOrderAccess(self.root)

    def midOrderTraverse1(self):
        '''非递归形式的打印，使用一个前指针解决'''
        if not self.root:
            return

        pre_curr = None  # 当前节点之前访问的那个节点
        # 首先找到最左的那个节点
        stack = []
        curr = self.root
        while stack or curr != None:
            # 针对每个节点，找到所有的左树节点。
            while curr != None:
                stack.append(curr)
                curr = curr.left
            # 打印节点内容，并将右侧子树放到栈中
            if stack:
                curr = stack.pop()
                print(curr.val, end=" ")
                curr = curr.right
    def levelOrderTraverse(self):
        if not self.root:
            return
        queue = [self.root]
        while queue:
            node = queue.pop(0)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            print(node.val, end = "  ")
