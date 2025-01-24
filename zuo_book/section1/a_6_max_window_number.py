

array = []
window_size = 3

queue = [] # 双端队列，保存一个降序的队列，队首是这个窗口的最大值。队列中的每个位置的值，都要大于窗口中处于他右侧的所有值。
out = [] # 输出队列
def max_number_in_window(array, window_size):
    if not array or window_size < 0 or window_size > len(array):
        raise Exception("输入的有问题")
    for i in range(len(array)):
        if len(queue) > 0:
            if i - window_size == queue[0]:
                queue.pop(0) # 超出窗口的，出队
            while len(queue) > 0 and array[queue[-1]] < array[i]:
                queue.pop()
            queue.append(i)
        else:
            queue.append(i)
        if i >= window_size-1:
            out.append(array[queue[0]]) # 保存最大值

array = [4,3,5,4,3,3,6,7]
window_size = 3
max_number_in_window(array, window_size)
print(out)


