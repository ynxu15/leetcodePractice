'''
用栈来求解汉诺塔问题
'''

lstack, mstack, rstack = [], [], []
n = 2

lstack.append(0)
for i in range(n, 0, -1):
    lstack.append(i)
mstack.append(0)
rstack.append(0)

print(lstack)
print(mstack)
print(rstack)

cache_map = {}
def solve_hanoi(lstack, mstack, rstack):
    if (lstack[-1], mstack[-1], rstack[-1]) in cache_map:
        return 10000000
    cache_map[(lstack[-1], mstack[-1], rstack[-1])] = None

    # 解决这个问题了
    if lstack[-1] == 0 and mstack[-1] == 0:
        return 0

    move_count1, move_count2, move_count3, move_count4 = 10000, 10000, 10000, 10000

    # 1. l -> m
    if lstack[-1] != 0:
        item = lstack.pop()
        mstack.append(item)
        move_count1 = solve_hanoi(lstack, mstack, rstack)
        # 恢复
        item = mstack.pop()
        lstack.append(item)
    # 2. m -> r
    if mstack[-1] != 0:
        item = mstack.pop()
        rstack.append(item)
        move_count2 = solve_hanoi(lstack, mstack, rstack)
        # 恢复
        item = rstack.pop()
        mstack.append(item)

    # 3. m -> l
    if mstack[-1] != 0:
        item = mstack.pop()
        lstack.append(item)
        move_count3 = solve_hanoi(lstack, mstack, rstack)
        # 恢复
        item = lstack.pop()
        mstack.append(item)

    # 4. r -> m
    if rstack[-1] != 0:
        item = rstack.pop()
        mstack.append(item)
        move_count4 = solve_hanoi(lstack, mstack, rstack)
        # 恢复
        item = mstack.pop()
        rstack.append(item)

    return min(move_count1, move_count2, move_count3, move_count4) + 1

print(solve_hanoi(lstack, mstack, rstack))
