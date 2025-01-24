'''
猫狗队列
'''

'''
还有一种实现是用一个代理类，代理类中保存原始的对象，以及进入队列的时间。
然后创建两个队列，分别保存猫和狗。弹出的时候，只要比较入队的时间，就可以保证按照原始的入队顺序弹出。
'''

class Pet:
    def __init__(self, type):
        self.type = type
    def get_pet_type(self):
        return self.type

class Dog(Pet):
    def __init__(self):
        super().__init__("dog")

class Cat(Pet):
    def __init__(self):
        super().__init__("cat")


class Queue:
    def __init__(self):
        self.queue = []
        self.dogCount = 0
        self.catCount = 0

    def add(self, pet):
        self.queue.append(pet)
        if isinstance(pet, Dog):
            self.dogCount +=1
        if isinstance(pet, Cat):
            self.catCount +=1

    def pollALl(self):
        while self.queue:
            print(self.queue.pop(0), end=" ")
        self.catCount = 0
        self.dogCount = 0

    def pollDog(self):
        queue_new = []
        while self.queue:
            pet = self.queue.pop(0)
            if isinstance(pet, Dog):
                print(pet, end=" ")
            else:
                queue_new.append(pet)
        self.queue = queue_new
        self.dogCount = 0

    def pollCat(self):
        queue_new = []
        while self.queue:
            pet = self.queue.pop(0)
            if isinstance(pet, Cat):
                print(pet, end=" ")
            else:
                queue_new.append(pet)
        self.queue = queue_new
        self.catCount = 0

    def isEmpty(self):
        return not self.queue

    def isDogEmpty(self):
        return self.dogCount == 0

    def isCatEmpty(self):
        return self.catCount == 0
