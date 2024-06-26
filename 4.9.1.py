def f(x, n):
    if n == 0:
        return 1
    elif n < 0:
        return 1 / f(x, -n)
    elif n % 2 == 0:
        return f(x, n//2) * f(x, n//2)
    else:
        return x * f(x, n-1)

# 測試程式
x = 2
n = 3
result = f(x, n)
print(f"{x} 的 {n} 次方是 {result}")