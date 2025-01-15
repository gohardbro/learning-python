def number_coroutine():
    while True: # 코루틴을 계속 유지하기 위해 무한 루프 사용
        x = (yield) # 코루틴 바깥에서 값 받아옴
        print(x)
        
co = number_coroutine()
next(co) # 코루틴 안의 yield까지 코드 실행(최초 실행)

# 코루틴에 값 보냄
co.send(1)
co.send(2)
co.send(3)
