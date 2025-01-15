def accumulate():
    total = 0
    while True:
        x = (yield)
        if x is None:
            return total
        total += x
        
def sum_corountine():
    while True:
        total = yield from accumulate()
        print(total)
        
co = sum_corountine()
next(co)

for i in range(1, 11):
    co.send(i)
co.send(None)

for i in range(1, 101):
    co.send(i)
co.send(None)