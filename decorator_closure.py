def trace(func): # 
    def wrapper():
        print(func.__name__, '함수 시작')
        func()
        print(func.__name__, '함수 종료')
    return wrapper

def hi():
    print('hi')

def bye():
    print('bye')
    
hi_trace = trace(hi)
bye_trace = trace(bye)
hi_trace()
bye_trace()
