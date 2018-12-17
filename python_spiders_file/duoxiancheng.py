import threading


class A(threading.Thread):
    def __init__(self):
        """初始化该线程"""
        threading.Thread.__init__(self)


    def run(self):
        """该线程要执行的内容"""
        for i in range(10):
            print("我是线程A")


class B(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)


    def run(self):
        for i in range(10):
            print("我是线程B")


# 实例化线程A为t1
t1 = A()
t2 = B()
# 启动线程t1
t1.start()
t2.start()