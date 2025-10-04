################################################
[claude TLE9]
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
  
###############################################
[claude AC]
def min_distance(A0, A1, B0, B1):
    # ベクトルの引き算
    def sub(p1, p2):
        return (p1[0] - p2[0], p1[1] - p2[1])
    
    # ベクトルの内積
    def dot(v1, v2):
        return v1[0] * v2[0] + v1[1] * v2[1]
    
    # ベクトルの長さの2乗
    def norm_sq(v):
        return v[0] * v[0] + v[1] * v[1]
    
    # ベクトルの長さ
    def norm(v):
        return norm_sq(v) ** 0.5
    
    # ベクトルのスカラー倍
    def mul(v, s):
        return (v[0] * s, v[1] * s)
    
    # ベクトルの足し算
    def add(v1, v2):
        return (v1[0] + v2[0], v1[1] + v2[1])
    
    vA = sub(A1, A0)
    vB = sub(B1, B0)
    dA = norm(vA)
    dB = norm(vB)
    
    tA = dA
    tB = dB
    
    # 単位方向ベクトル
    if dA > 1e-10:
        uA = (vA[0] / dA, vA[1] / dA)
    else:
        uA = (0.0, 0.0)
    
    if dB > 1e-10:
        uB = (vB[0] / dB, vB[1] / dB)
    else:
        uB = (0.0, 0.0)
    
    min_dist_sq = float('inf')
    
    # 区間1: 両方移動中
    t_max = min(tA, tB)
    if t_max > 0:
        P = sub(A0, B0)
        Q = sub(uA, uB)
        
        Q_norm_sq = norm_sq(Q)
        if Q_norm_sq > 1e-10:
            t_min = -dot(P, Q) / Q_norm_sq
            t_min = max(0, min(t_min, t_max))
        else:
            t_min = 0
        
        pos_diff = sub(add(A0, mul(uA, t_min)), add(B0, mul(uB, t_min)))
        min_dist_sq = min(min_dist_sq, norm_sq(pos_diff))
        
        # 境界
        min_dist_sq = min(min_dist_sq, norm_sq(sub(A0, B0)))
        pos_diff = sub(add(A0, mul(uA, t_max)), add(B0, mul(uB, t_max)))
        min_dist_sq = min(min_dist_sq, norm_sq(pos_diff))
    
    # 区間2: 一方が停止
    if tA < tB - 1e-10:
        B_at_tA = add(B0, mul(uB, tA))
        v = sub(B1, B_at_tA)
        w = sub(A1, B_at_tA)
        
        c1 = dot(w, v)
        c2 = norm_sq(v)
        
        if c2 > 1e-10:
            t_param = max(0, min(1, c1 / c2))
            closest = add(B_at_tA, mul(v, t_param))
            min_dist_sq = min(min_dist_sq, norm_sq(sub(A1, closest)))
            
    elif tB < tA - 1e-10:
        A_at_tB = add(A0, mul(uA, tB))
        v = sub(A1, A_at_tB)
        w = sub(B1, A_at_tB)
        
        c1 = dot(w, v)
        c2 = norm_sq(v)
        
        if c2 > 1e-10:
            t_param = max(0, min(1, c1 / c2))
            closest = add(A_at_tB, mul(v, t_param))
            min_dist_sq = min(min_dist_sq, norm_sq(sub(closest, B1)))
    
    # 最終位置
    min_dist_sq = min(min_dist_sq, norm_sq(sub(A1, B1)))
    
    return min_dist_sq ** 0.5

T = int(input())
for _ in range(T):
    a0x, a0y, a1x, a1y = map(int, input().split())
    b0x, b0y, b1x, b1y = map(int, input().split())
    A0, A1 = (a0x, a0y), (a1x, a1y)
    B0, B1 = (b0x, b0y), (b1x, b1y)
    print(min_distance(A0, A1, B0, B1))
###############################################
[titia]

import sys
input = sys.stdin.readline

T=int(input())

for tests in range(T):
    N=int(input())
    S=input().strip()

    X=[]

    one=0
    zero=0

    for s in S:
        if s=="0":
            zero+=1
        else:
            one+=1
            
        if X==[]:
            X.append([s,1])
        else:
            if X[-1][0]==s:
                X[-1][1]+=1
            else:
                X.append([s,1])

    #print(X)

    ANS=1<<63

    for com,ko in X:
        if com=="0":
            z=zero-ko
            o=one

            ANS=min(ANS,z*2+o)
        else:
            z=zero
            o=one-ko

            ANS=min(ANS,z+o*2)

    print(ANS)

###############################################
[eman]

import sys; input = sys.stdin.readline
def f(a,b,c,d): return ((a-c)**2+(b-d)**2)**0.5
def g(p):
    if p>tt: tx,ty = tgx,tgy
    else:
        q = tt-p
        tx = (tsx*q+tgx*p)/tt
        ty = (tsy*q+tgy*p)/tt
    if p>aa: ax,ay = agx,agy
    else:
        q = aa-p
        ax = (asx*q+agx*p)/aa
        ay = (asy*q+agy*p)/aa
    return f(tx,ty,ax,ay)
def h(l,r):
    ll,rr = g(l),g(r)
    for _ in range(50):
        c1,c2 = (2*l+r)/3,(l+2*r)/3
        cc1,cc2 = g(c1),g(c2)
        if cc1>cc2: l,ll = c1,cc1
        else: r,rr = c2,cc2
    return min(ll,rr)
for _ in range(int(input())):
    tsx,tsy,tgx,tgy = map(int,input().split())
    asx,asy,agx,agy = map(int,input().split())
    tt,aa = f(tsx,tsy,tgx,tgy),f(asx,asy,agx,agy)
    print(min(h(0,min(tt,aa)),h(min(tt,aa),max(tt,aa))))
###############################################
###############################################
###############################################
###############################################
###############################################
###############################################
###############################################
###############################################
###############################################
###############################################

###############################################
###############################################
###############################################
###############################################
###############################################
###############################################

###############################################
###############################################
###############################################
###############################################
###############################################
###############################################
################################################
################################################
################################################
################################################
################################################
################################################
################################################

