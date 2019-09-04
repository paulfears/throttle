import time
class throttle(object):
    def __init__(self, interval):
        self.interval = interval/1000 #converts secounds to millisecounds
        self.last_call = 0
    def __call__(self, func, *args, **kwargs):
        def wrapper():
            if(time.time()-self.last_call > self.interval):
                self.last_call = time.time()
                func(*args, **kwargs)
        return wrapper


if __name__ == '__main__':
    @throttle(500)
    def output_time():
        print(time.time())
    while(True):
        output_time()
