###############################################
###############################################
###############################################
###############################################
[ds]
from collections import deque, defaultdict

def main():

    N, M = map(int, input().split())
    
    tubes = []
    for _ in range(M):
        k = int(input())
        a = list(map(int, input().split()))
        tubes.append(a)
    
    # 各色がどの筒の一番上にあるかを記録
    color_to_tubes = defaultdict(list)
    
    # 各筒の現在の先頭インデックス
    top_index = [0] * M
    
    # キューの準備：取り除けるペアを管理
    queue = deque()
    
    # 初期状態：各筒の一番上のボールをチェック
    for i in range(M):

        if top_index[i] < len(tubes[i]):

            color = tubes[i][top_index[i]]
            color_to_tubes[color].append(i)
            
            # 同じ色が2つ揃ったらキューに追加
            if len(color_to_tubes[color]) == 2:
                queue.append(color)
    
    removed_count = 0
    
    while queue: 要素がある間
        color = queue.popleft()
        tube1, tube2 = color_to_tubes[color]
        
        # ボールを取り除く
        top_index[tube1] += 1
        top_index[tube2] += 1
        
        removed_count += 2
        
        # 筒1の新しい一番上のボールをチェック
        if top_index[tube1] < len(tubes[tube1]):
            new_color1 = tubes[tube1][top_index[tube1]]
            color_to_tubes[new_color1].append(tube1)
            if len(color_to_tubes[new_color1]) == 2:
                queue.append(new_color1)
        
        # 筒2の新しい一番上のボールをチェック
        if top_index[tube2] < len(tubes[tube2]):
            new_color2 = tubes[tube2][top_index[tube2]]
            color_to_tubes[new_color2].append(tube2)
            if len(color_to_tubes[new_color2]) == 2:
                queue.append(new_color2)
    
    # すべてのボールが取り除けたかチェック
    if removed_count == 2 * N:
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()
###############################################
###############################################
###############################################
###############################################
###############################################
###############################################
