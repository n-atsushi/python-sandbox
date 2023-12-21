import time
def function_timer(func):
    def wrapper():
        t1 = time.time()
        func()
        t2 = time.time() - t1
        print(f'Took {t2} seconds')
    return wrapper

@function_timer
def do_this():
    time.sleep(1)
        
@function_timer
def do_that():
    time.sleep(5)

do_that()
do_this()
print('Done')