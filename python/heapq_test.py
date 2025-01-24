

'''
heapq 是小顶堆，要改成大顶堆的话，需要元素加负号
'''

# heapq.heappush(heap, item)
# 将值 item 推送到 heap，保持堆不变。
# heapq.heappop(heap)
# 从 堆 弹出并返回最小的项目，保持堆不变。 如果堆为空，则会引发 IndexError。 要访问最小的项目而不弹出它，请使用 heap[0]。
# heapq.heappushpop(heap, item)
# 将项推入堆，然后从堆中弹出并返回最小的项。 组合操作比 heappush() 更有效地运行，然后单独调用 heappop()。
# heapq.heapify(x)
# 将列表 x 在线性时间内就地转换为堆。

# heapq.nlargest(n, iterable, key=None)
# 从 iterable 定义的数据集中返回一个包含 n 个最大元素的列表。 key，如果提供，指定一个参数的函数，用于从 iterable 中的每个元素提取比较键（例如，key=str.lower）。 相当于：sorted(iterable, key=key, reverse=True)[:n]。
# heapq.nsmallest(n, iterable, key=None)
# 从 iterable 定义的数据集中返回一个包含 n 个最小元素的列表。 key，如果提供，指定一个参数的函数，用于从 iterable 中的每个元素提取比较键（例如，key=str.lower）。 相当于：sorted(iterable, key=key)[:n]。

import math
import heapq
from io import StringIO
def show_tree(tree, total_width=36, fill=' '):
    """Pretty-print a tree."""
    output = StringIO()
    last_row = -1
    for i, n in enumerate(tree):
        if i:
            row = int(math.floor(math.log(i + 1, 2)))
        else:
            row = 0
        if row != last_row:
            output.write('\n')
        columns = 2 ** row
        col_width = int(math.floor(total_width / columns))
        output.write(str(n).center(col_width, fill))
        last_row = row
    print(output.getvalue())
    print('-' * total_width)
    print()

data = [19, 9, 4, 10, 11]

heap = []
print('random :', data)
print()

for n in data:
    print('add {:>3}:'.format(n))
    heapq.heappush(heap, n)
    show_tree(heap)


print('random    :', data)
heapq.heapify(data)
print('heapified :')
show_tree(data)
print()

for i in range(2):
    smallest = heapq.heappop(data)
    print('pop    {:>3}:'.format(smallest))
    show_tree(data)

print('all       :', data)
print('3 largest :', heapq.nlargest(3, data))
print('from sort :', list(reversed(sorted(data)[-3:])))
print('3 smallest:', heapq.nsmallest(3, data))
print('from sort :', sorted(data)[:3])