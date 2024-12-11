# Pool + 阻塞执行
from multiprocessing import Pool
import time, os

def task(name):
    print(f"pid: {os.getpid()}, task name: {name}")
    time.sleep(1)
    

if __name__ == '__main__':
    start = time.time()
    print("father process start")
    p = Pool(3)
    for i in range(10):
        p.apply(func=task, args=(i,)) # 使用阻塞方式执行【一个一个执行】
    
    p.close() # 执行完毕后需要关闭 Pool
    p.join() # 必须在 terminate() or close() 之后使用
    
    print("father process finished")
    print(f"consume time: {time.time() - start}")