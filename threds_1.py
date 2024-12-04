import threading

def func_1():
    for i in range(10):
        print("one")
def func_2():
    for i in range(10):
        print("two")

t1 = threading.Thread(target=func_1)
t2 = threading.Thread(target=func_2)

t1.start()
t2.start()