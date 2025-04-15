A = ['a', '?', 'b', '?', 'c']
B = ['x', 'y']

# '?' の位置を見つけて、順番にBの要素で置換
b_iter = iter(B)
A = [next(b_iter) if x == '?' else x for x in A]

print(A)
