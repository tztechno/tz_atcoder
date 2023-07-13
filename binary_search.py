#####################################################

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
  
#####################################################

def binary_search(l, r):
    while l < r:
        mid = (l + r) // 2
        # midを使った条件判定
        if condition(mid):
            r = mid
        else:
            l = mid + 1
    return l

# 二分探索で解を求める条件判定関数
def condition(x):
    # xを使った条件判定のロジックを実装
    # 条件を満たす場合はTrueを、満たさない場合はFalseを返す
    # 例: xがKより大きいかどうかを判定する場合
    return x > K

# 使用例
N, K = 100, 50  # 探索範囲や条件に応じて値を設定
result = binary_search(0, N)
print(result)

#####################################################
