import threading

from time import ctime,sleep


def music(func):
    for i in range(2):
        print ("I was listening to %s. %s" %(func,ctime()))
        sleep(1)

def move(func):
    for i in range(2):
        print ("I was at the %s! %s" %(func,ctime()))
        sleep(1)



if __name__ == '__main__':
    threads = []
    t1 = threading.Thread(target=music, args=('爱情买卖',))
    threads.append(t1)
    t2 = threading.Thread(target=move, args=(r'阿凡达\n',))#r表示无特殊含义的字符串
    threads.append(t2)

    for t in threads:
       # t.setDaemon(True)
        t.start()

    print ("all over %s" %ctime())