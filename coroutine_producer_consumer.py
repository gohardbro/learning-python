def sum_corountine():
    total = 0
    while True:
        x = (yield total) # 코루틴 바깥에서 값을 받아오면서 바깥으로 값을 전달
        total += x
        
co = sum_corountine()
print(next(co)) # 0: 코루틴 안의 yield까지 코드를 실행하고 코루틴에서 나온 값 출력

# 코루틴에 값을 보내고 코루틴에서 나온 값 출력
print(co.send(1)) 
print(co.send(2))
print(co.send(3))
