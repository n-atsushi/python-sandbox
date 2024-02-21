import logging
import threading
import time

logging.basicConfig(
    level=logging.DEBUG, format='%(threadName)s: %(message)s'
)

def worker1():
    logging.debug('start')
    time.sleep(5)
    logging.debug('end')

def worker2():
    logging.debug('start')
    time.sleep(1)
    logging.debug('end')


if __name__ == '__main__':
    # t1 = threading.Thread(name='rename worker1',target=worker1)
    # t2 = threading.Thread(name='rename worker2', target=worker2)
    # t1.start()
    # t2.start()
    # t1.join()
    # t2.join()
    for _ in range(5):
        t = threading.Thread(target=worker1)
        t.setDaemon(True)
        t.start()
    for thread in threading.enumerate():
        if thread is threading.current_thread():
            print(thread)
            continue
        thread.join()
        print("hello")
