'''
 仅使用递归函数，逆序一个栈
'''

stack = []

def get_last_element(stack):
    item = stack.pop()
    if not stack:
        return item
    else:
        last_element = get_last_element(stack)
        stack.append(item)
        return last_element

def reverse_stack(stack):
    if not stack:
        return stack
    last_element = get_last_element()
    reverse_stack(stack)
    stack.append(last_element)
    return stack