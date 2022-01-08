from threading import Thread

'''
#写法1
def func(name):
    for i in range(10):
        print(name+str(i))

if __name__ == '__main__':
    t1=Thread(target=func,args=("周杰伦",))
    t2=Thread(target=func,args=("王力宏",))
    t3 = Thread(target=func, args=("sunhouzi",))
    t1.start()
    t2.start()
    t3.start()
'''


class MyThread(Thread):
    def __init__(self, name):
        super(MyThread, self).__init__()
        self.name = name

    def run(self):
        for i in range(100):
            print(self.name, i)


if __name__ == '__main__':
    t1 = MyThread("周杰伦")
    t2 = MyThread("12")
    t3 = MyThread("fasf")
    t1.start()
    t2.start()
    t3.start()
