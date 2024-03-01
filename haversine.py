
############################################################################

import math

cities=[
  (35.6895,139.6917),
  (34.6937,135.5023),
  (43.0621,141.3544),
  (33.5904,130.4017)
  ]

N=len(cities)

X_Y=[]
for i in range (N):
    x,y=cities[i]
    X_Y.append([i,x,y,-1,10**9])#自分、自分の位置、最も近いもの、その距離

def haversine(lat1, lon1, lat2, lon2):
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    radius = 6371.0
    distance = radius * c
    return distance

for i in range (N):
    now=X_Y[i]#自分
    for j in range(N):
        com=X_Y[j]#相手
        if i!=j and haversine(now[1], now[2], com[1], com[2])<=now[4]:
            X_Y[i][4]=haversine(now[1], now[2], com[1], com[2])
            X_Y[i][3]=j
print(X_Y)

    

############################################################################

import math

def haversine(lat1, lon1, lat2, lon2):
    # 緯度経度をラジアンに変換
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])

    # Haversine式
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    # 地球の半径（単位: km）
    radius = 6371.0

    # ２点間の距離を計算
    distance = radius * c

    return distance

# 例: 東京の座標 (35.6895° N, 139.6917° E) とニューヨークの座標 (40.7128° N, -74.0060° W)
tokyo_lat, tokyo_lon = 35.6895, 139.6917
ny_lat, ny_lon = 40.7128, -74.0060

# ２点間の距離を求める
distance_km = haversine(tokyo_lat, tokyo_lon, ny_lat, ny_lon)
print(f"東京とニューヨークの距離: {distance_km} km")
