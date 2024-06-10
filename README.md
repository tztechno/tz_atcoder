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
5. **ANS の計算**
    ```python
    ANS = N * (1 - (pow(k, N, mod))) * pow(1 - k, mod - 2, mod)
    ```
    `ANS` は次のように計算されます:
    - `pow(k, N, mod)` は \( k \) を \( N \) 乗した結果の `mod` での余りです。
    - `pow(1 - k, mod - 2, mod)` は `1 - k` の逆元です。
    - フェルマーの小定理により、逆元は `1 - k` を \( mod - 2 \) 乗した結果の `mod` での余りとなります。

---

4. **変数 `k` の計算**
    ```python
    k = pow(10, len(str(N)), mod)
    ```
    `k` は \( 10 \) を \( N \) の桁数だけべき乗し、その結果を `mod` で割った余りです。

---
1. **モジュールのインポートと標準入力の設定**
    ```python
    import sys
    input = sys.stdin.readline
    ```
    標準入力を高速に読み込むために `sys.stdin.readline` を使用
---
