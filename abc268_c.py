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
[deepseek AC]
def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    P = list(map(int, data[1:1+n]))
    
    # 各回転量における満足人数をカウントする配列
    count = [0] * n
    
    for j in range(n):
        # 人jが満足する回転量を計算
        # 3つの料理位置について
        for offset in [-1, 0, 1]:
            # 料理が届く位置: (P[j] + offset) % n
            dish_pos = (P[j] + offset) % n
            if dish_pos < 0:
                dish_pos += n
            
            # この料理が人jに届く回転量i
            # i ≡ (dish_pos - j) % n
            i_val = (dish_pos - j) % n
            if i_val < 0:
                i_val += n
            
            count[i_val] += 1
    
    print(max(count))

if __name__ == "__main__":
    main()
###############################################
[gemini AC]
import sys
N = int(input())
P = list(map(int, input().split()))

score_counts = [0] * N

for i, p in enumerate(P):
    j1 = (p - 1 - i + N) % N
    score_counts[j1] += 1

    j2 = (p - i + N) % N
    score_counts[j2] += 1

    j3 = (p + 1 - i + N) % N
    score_counts[j3] += 1
    
print(max(score_counts))
###############################################
[my gemini AC]
N=int(input())
P=list(map(int,input().split()))

score=[0]*N

for i,p in enumerate(P): #dishごとにどれだけ動いたときに満足か
  j1=(p-i-1+N)%N
  score[j1]+=1
  j2=(p-i+N)%N
  score[j2]+=1
  j3=(p-i+1+N)%N
  score[j3]+=1

print(max(score))
      
###############################################
[my TLE]
N=int(input())
P=list(map(int,input().split()))

MAX=0
for i in range(N):#回転量
  m=0
  for j in range(N):#各人において
    if j in [P[(j-1+i)%N],P[(j+i)%N],P[(j+1+i)%N]]:
      m+=1
  MAX=max(MAX,m)
print(MAX)

###############################################
[my TLE]
N=int(input())
P=list(map(int,input().split()))

score=[0]*N

for j in range(N):#回転量
  for i,p in enumerate(P):
    dish=(i+j)%N
    if -1<=dish-p<=1:
      score[j]+=1
    if dish==N-1 and p==0:
      score[j]+=1      
    if dish==0 and p==N-1:
      score[j]+=1     
      
print(max(score))
###############################################
###############################################
###############################################
###############################################
