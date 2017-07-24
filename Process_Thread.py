import os
os.getpid()#返回父进程的id

#多进程 multiprocessing 
#Unix/Linux 用fork() 而windows系统不支持，所以需要用到multiprocessing库。

#multiprocessing模块提供了一个Process类来代表一个进程对象。
from multiprocessing import Process
import os

# 子进程要执行的代码
def run_proc(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))

if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
    p = Process(target=run_proc, args=('test',))
    print('Child process will start.')
    p.start()
    p.join()
    print('Child process end.')
#注,这个需要shell中调用,IDE调用会出现问题。
#start 就是开始,执行run方法，而join是阻塞,等待子进行完成后，方往下进行，一般依次start 然后依次join.
#
# Pool 批量创建子进程
from multiprocessing import Pool
import os, time, random

def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))

if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
    p = Pool(4)
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done.')

# 调用join()之前必须先调用close()，调用close()之后就不能继续添加新的Process了。
# 对pool是实例对象close和join


子进程 subprocess

