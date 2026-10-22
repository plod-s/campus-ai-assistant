def timer(func):
    def wrapper():
        import time
        start = time.time()
        func()
        print(f'耗时 {time.time()-start:.4f} 秒')
    return wrapper


@timer
def slow():
    total = 0
    for i in range(1000000):
        total += i

slow()