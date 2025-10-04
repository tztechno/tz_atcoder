################################################
import numpy as np

def min_distance(A0, A1, B0, B1):
    A0 = np.array(A0, dtype=float)
    A1 = np.array(A1, dtype=float)
    B0 = np.array(B0, dtype=float)
    B1 = np.array(B1, dtype=float)
    
    vA = A1 - A0
    vB = B1 - B0
    dA = np.linalg.norm(vA)
    dB = np.linalg.norm(vB)
    
    tA = dA
    tB = dB
    
    uA = vA / dA if dA > 1e-10 else np.zeros_like(vA)
    uB = vB / dB if dB > 1e-10 else np.zeros_like(vB)
    
    min_dist = float('inf')
    
    # 区間1: 両方移動中 (0 <= t <= min(tA, tB))
    t_max = min(tA, tB)
    if t_max > 0:
        P = A0 - B0
        Q = uA - uB
        
        Q_norm_sq = np.dot(Q, Q)
        if Q_norm_sq > 1e-10:
            t_min = -np.dot(P, Q) / Q_norm_sq
            t_min = np.clip(t_min, 0, t_max)
        else:
            t_min = 0
        
        dist = np.linalg.norm(A0 + t_min * uA - (B0 + t_min * uB))
        min_dist = min(min_dist, dist)
        
        # 境界もチェック
        dist_0 = np.linalg.norm(A0 - B0)
        dist_max = np.linalg.norm(A0 + t_max * uA - (B0 + t_max * uB))
        min_dist = min(min_dist, dist_0, dist_max)
    
    # 区間2: 一方が停止
    if tA < tB - 1e-10:
        # Aが停止、Bが移動 (tA <= t <= tB)
        # A1からBの経路への最短距離を求める
        # B(t) = B0 + t*uB なので、B(tA) から B(tB) の線分
        B_at_tA = B0 + tA * uB
        
        # A1から線分 B_at_tA→B1 への最短距離
        v = B1 - B_at_tA
        w = A1 - B_at_tA
        
        c1 = np.dot(w, v)
        c2 = np.dot(v, v)
        
        if c2 > 1e-10:
            t_param = c1 / c2
            t_param = np.clip(t_param, 0, 1)
            closest = B_at_tA + t_param * v
            dist = np.linalg.norm(A1 - closest)
            min_dist = min(min_dist, dist)
            
    elif tB < tA - 1e-10:
        # Bが停止、Aが移動 (tB <= t <= tA)
        A_at_tB = A0 + tB * uA
        
        v = A1 - A_at_tB
        w = B1 - A_at_tB
        
        c1 = np.dot(w, v)
        c2 = np.dot(v, v)
        
        if c2 > 1e-10:
            t_param = c1 / c2
            t_param = np.clip(t_param, 0, 1)
            closest = A_at_tB + t_param * v
            dist = np.linalg.norm(closest - B1)
            min_dist = min(min_dist, dist)
    
    # 最終位置
    min_dist = min(min_dist, np.linalg.norm(A1 - B1))
    
    return min_dist


T = int(input())
for _ in range(T):
    a0x, a0y, a1x, a1y = map(int, input().split())
    b0x, b0y, b1x, b1y = map(int, input().split())
    A0, A1 = (a0x, a0y), (a1x, a1y)
    B0, B1 = (b0x, b0y), (b1x, b1y)
    min_dist = min_distance(A0, A1, B0, B1)
    print(min_dist)
  
################################################
################################################
################################################
################################################
################################################
################################################
################################################
################################################

