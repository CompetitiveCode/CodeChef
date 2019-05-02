# Answer to Buying New Tablet
# https://www.codechef.com/problems/TABLET


for _ in range(int(input())):
    n, price = map(int, input().split())
    res = 0
    for i in range(n):
        w, h, c = map(int, input().split())
        if c <= price:
            res = max(w*h, res)
    if res != 0:
        print(res)
    else:
        print('no tablet')
