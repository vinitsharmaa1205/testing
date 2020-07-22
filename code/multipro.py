# import time
# '''measure time to script to run'''
# start = time.perf_counter()
#
# def do_something():
#     print('Sleeping 1 second')
#     time.sleep(5)
#     print('Done')
# for i in range(5):
#     do_something()
# finish = time.perf_counter()
#
# print(f'Finished in {round(finish-start,2)}second(s)')

import time
import multiprocessing
'''measure time to script to run'''
start = time.perf_counter()

def do_something():
    print('Sleeping 1 second')
    time.sleep(5)
    print('Done')

p1=multiprocessing.Process(target=do_something)
p2=multiprocessing.Process(target=do_something)
p1.start()
p2.start()
finish = time.perf_counter()

print(f'Finished in {round(finish-start,2)}second(s)')