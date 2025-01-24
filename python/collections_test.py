import collections
from collections import Counter, deque, OrderedDict, ChainMap, defaultdict

print(collections.__all__)
# ['deque', 'defaultdict', 'namedtuple', 'UserDict', 'UserList',
# 'UserString', 'Counter', 'OrderedDict', 'ChainMap']

# namedtuple()	创建命名元组子类的工厂函数，生成可以使用名字来访问元素内容的tuple子类
# deque	类似列表(list)的容器，实现了在两端快速添加(append)和弹出(pop)
# ChainMap	类似字典(dict)的容器类，将多个映射集合到一个视图里面
# Counter	字典的子类，提供了可哈希对象的计数功能
# OrderedDict	字典的子类，保存了他们被添加的顺序，有序字典
# defaultdict	字典的子类，提供了一个工厂函数，为字典查询提供一个默认值
# UserDict	封装了字典对象，简化了字典子类化
# UserList	封装了列表对象，简化了列表子类化
# UserString	封装了字符串对象，简化了字符串子类化（中文版翻译有误）


# 计数器 Counter

def run_counter():
    from collections import Counter
    import re
    text = 'remove an existing key one level down remove an existing key one level down'
    words = re.findall(r'\w+', text)
    print(Counter(words).most_common(10))
    #[('remove', 2), ('an', 2), ('existing', 2), ('key', 2), ('one', 2)('level', 2), ('down', 2)]

    # 计算列表中单词的个数
    cnt = Counter()
    for word in ['red', 'blue', 'red', 'green', 'blue', 'blue']:
        cnt[word] += 1
    print(cnt)
    # Counter({'red': 2, 'blue': 3, 'green': 1})

    # 上述这样计算有点嘛，下面的方法更简单，直接计算就行
    L = ['red', 'blue', 'red', 'green', 'blue', 'blue']
    print(Counter(L))
    # Counter({'red': 2, 'blue': 3, 'green': 1}

def str_sim(str_0,str_1,topn):
    '''计算两个字符串的相似性，交并比'''
    topn = int(topn)
    collect0 = Counter(dict(Counter(str_0).most_common(topn)))
    collect1 = Counter(dict(Counter(str_1).most_common(topn)))
    jiao = collect0 & collect1
    bing = collect0 | collect1
    sim = float(sum(jiao.values()))/float(sum(bing.values()))
    return(sim)
def run_dequeue():
    d = deque('ghi')
    d.append('j')
    print(d)
    #deque(['g', 'h', 'i', 'j'])

    d.appendleft('f')
    print(d)
    #deque(['f', 'g', 'h', 'i', 'j'])

    d.clear()

    d = deque('xiaoweuge')
    y = d.copy()
    print(y)
    #deque(['x', 'i', 'a', 'o', 'w', 'e', 'u', 'g', 'e'])

    d.count('a')
    # 1

    a = deque('abc')
    b = deque('cd')
    a.extend(b)
    print(a)
    # deque(['a', 'b', 'c', 'c', 'd'])

    a = deque('abc')
    b = deque('cd')
    a.extendleft(b)
    print(a)
    # deque(['d', 'c', 'a', 'b', 'c'])

    a = deque('abc')
    a.insert(1, 'X')
    # deque(['a', 'X', 'b', 'c'])

    d.pop()
    d.popleft()
    # d.remove(value='a')

    d.reverse()

def run_orderedDict():
    '''可以保持排序'''
    d = OrderedDict.fromkeys('abcde')
    d.popitem()
    # ('e', None)

    print(d)
    # OrderedDict([('a', None), ('b', None), ('c', None), ('d', None)])
    # last=False时，弹出第一个
    d = OrderedDict.fromkeys('abcde')
    ''.join(d.keys())
    # 'abcde'
    d.popitem(last=False)
    ''.join(d.keys())
    # 'bcde'


def run_chainMap():
    '''将多个字典视为1个'''
    baseline = {'music': 'bach', 'art': 'rembrandt'}
    adjustments = {'art': 'van gogh', 'opera': 'carmen'}
    ChainMap(adjustments, baseline)
    # ChainMap({'art': 'van gogh', 'opera': 'carmen'}, {'music': 'bach', 'art': 'rembrandt'})
    list(ChainMap(adjustments, baseline))
    # ['music', 'art', 'opera']
    # 存在重复元素时，也不会去重
    dcic1 = {'label1': '11', 'label2': '22'}
    dcic2 = {'label2': '22', 'label3': '33'}
    dcic3 = {'label4': '44', 'label5': '55'}
    last = ChainMap(dcic1, dcic2, dcic3)
    print(last)
    # ChainMap({'label1': '11', 'label2': '22'}, {'label2': '22', 'label3': '33'}, {'label4': '44', 'label5': '55'})

def run_defaultdict():
    '''使用dict时，如果引用的Key不存在，就会抛出KeyError。如果希望key不存在时，返回一个默认值，就可以用defaultdict。'''
    s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
    d = defaultdict(list)
    for k, v in s:
        d[k].append(v)

    sorted(d.items())
    # [('blue', [2, 4]), ('red', [1]), ('yellow', [1, 3])]

    s = 'mississippi'
    d = defaultdict(int)
    for k in s:
        d[k] += 1
    sorted(d.items())
    # [('i', 4), ('m', 1), ('p', 2), ('s', 4)]

    s = [('red', 1), ('blue', 2), ('red', 3), ('blue', 4), ('red', 1), ('blue', 4)]
    d = defaultdict(set)
    for k, v in s:
        d[k].add(v)

    sorted(d.items())
    # [('blue', {2, 4}), ('red', {1, 3})]