'''
用一个栈实现另一个栈的排序
'''

class StackSort:
    def __init__(self):
        self.stack = []

    def sort(self):
        if not self.stack:
            return
        stack_tmp = []
        while self.stack:
            item = self.stack.pop()
            if not stack_tmp:
                stack_tmp.append(item)
                continue
            if item <= stack_tmp[-1]:
                stack_tmp.append(item)
            else:
                # 放回原来的栈，并将当前的Item放到合适位置
                while stack_tmp:
                    item2 = stack_tmp.pop()
                    if item <= item2:
                        self.stack.append(item)
                        item = None
                        self.stack.append(item2)
                        break
                    else:
                        self.stack.append(item2)
                if item:
                    self.stack.append(item)
        while stack_tmp:
            item = stack_tmp.pop()
            self.stack.append(item)
        return
