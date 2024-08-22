na = -1
n = 1
for i in range(0,16,1):
    x=n+na
    na=n
    n=x
    if n:
        print(n)