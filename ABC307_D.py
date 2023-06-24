#titia

N=int(input())
S=input().strip()

LIST=[0]*(N+10)
#なぜ＋１０なのか

Q=[]
now=0
for i in range(N):
    if S[i]=="(":
        Q.append(i)
    elif S[i]==")":
        if Q: #Q が空でないかどうかがチェック
            x=Q.pop() #スタック Q から最上位のインデックス x を取り出し 
            LIST[x]+=1 #LIST[x] を 1 だけインクリメント。#削除対象の始まり
            LIST[i+1]-=1 #LIST[i+1] を 1 だけデクリメント。#削除の対象外の始まり
            #+1（始まり）と-1（　終わり）を記録する

for i in range(1,N+10):
    LIST[i]+=LIST[i-1]
    #要素の累積合計を取得
    #＋１は引き継がれる、-1で0になり止まる
    
ANS=[]
for i in range(N):
    if LIST[i]==0:#LIST 内の対応する要素が 0 の場合、消されず残る文字になる
        ANS.append(S[i])

print("".join(ANS))
