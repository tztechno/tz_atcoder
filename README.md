# tz_atcoder

### latest

---
```

```
---
```

```
---
```

```
---
```

```
---
```

```
---
```

```
---
```
def f(a, b):
    return a*a*a-b*b*b
N=int(input())
for w in range(1,1000000):
    ok=1
    ng=int(1e9)
    while (ng-ok)>1:
        m=(ok+ng)//2
        if(f(w+m,m)<=N): ok=m
        else: ng=m
    if(f(ok+w,ok)==N):
        print(ok+w,ok)
        exit()
print(-1)
```
---
```
if bit & (1<<i): の条件は、2進数で表したときに bit の i 番目のビットが 1であるかどうか をチェックしています。

bit & (1<<i) は、bit の2進数表現の i番目 のビットが 1 である場合に真 (True) となり、0 であれば偽 (False) となります。
```
---

4. **変数 `k` の計算**
    ```python
    k = pow(10, len(str(N)), mod)
    ```
    `k` は \( 10 \) を \( N \) の桁数だけべき乗し、その結果を `mod` で割った余りです。

---

