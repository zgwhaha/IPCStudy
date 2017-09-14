import logging
import threading
import time


def worker(arg):
    while not arg['stop']:
        logging.warning('Hi from myfunc')
        time.sleep(0.5)
def main():
    logging.basicConfig(level=logging.DEBUG, format='%(relativeCreated)6d %(threadName)s %')
    logging.basicConfig(level=logging.NOTSET)
    info = {'stop': False}
    thread = threading.Thread(target=worker, args=(info,))
    thread.start()
while True:
    try:
        logging.warning('Hello from main')
        time.sleep(0.75)
    except KeyboardInterrupt:
        info['stop'] = True
    break
    thread.join()
if __name__ == '__main__':
    main()