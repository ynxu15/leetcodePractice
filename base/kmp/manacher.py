

class Manacher:
    def __init__(self):
        pass

    def search(self, s):
        manachers = ["#"]
        for c in s:
            manachers.append(c)
            manachers.append("#")

        p = [0] * len(manachers)
        r, c = 0, 0  # 最右侧边界，最右侧边界对应的中心位置。
        maxl = 0
        n = len(manachers)
        for i in range(len(manachers)):
            length = if r > i: min(p[2*c-i], r-i) else 1
            while i+length < n and i - length >= 0 and manachers[i+length] == manachers[i-length]:
                length += 1
            # 以i为中心，回文半径length，能不能更新r和c
            if i + length > r:
                r = i + length
                c = i
            # 记住最大的回文半径
            maxl = max(maxl, length)
            p[i] = length
        return maxl - 1




