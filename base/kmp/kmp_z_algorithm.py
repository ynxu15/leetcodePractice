
class KMP:
    def search(self, s1, s2):
        s1_len, s2_len = len(s1), len(s2)

        if s1_len < s2_len:
            return -1
        def build_next(s):
            next = [-1] * len(s)
            if len(s) < 2:
                return next
            next[1] = 0

            i, cn = 2, 0
            while i < len(s):
                if s[i-1] == s[cn]:
                    next[i] = cn+1
                    cn += 1
                    i += 1
                elif cn > 0:
                    cn = next[cn]
                else:
                    next[i] = 0
                    i += 1
            return next

        next = build_next(s2)
        i, j = 0, 0
        while i<s1_len and j< s2_len:
            if s1[i] == s2[j]:
                i += 1
                j += 1
            elif j == 0:
                i += 1
            else:
                j = next[j]
        if j == s2_len:
            return i-s2_len
        return -1


if __name__ == '__main__':

    s1 = 'aabc'
    s2 = 'abc'

    kmp = KMP()
    print(kmp.search(s1, s2))