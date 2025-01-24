'''
MaxTree
'''

class Node:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# 最大值序列
# root比子树都要大
queue = []
stack = []
def gen_max_tree(array):
    pass