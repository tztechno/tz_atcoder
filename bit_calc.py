####################################

if (i >> j) & 1 == 0:

## 整数 i の2進数表現において、ビット位置 j が0であるかどうかをチェックしています。
## 具体的には、i を右に j ビットシフトし、そしてその結果に対してビット単位のAND演算 (&) を行っています。

####################################

if mask & (1<<i):
# iがmaskに含まれるならば

if not mask & (1<<i):
# iがmaskに含まれないならば
  
####################################

a_candidates = [i for i in range(1 << H1) if bin(i).count('1') == H2]
b_candidates = [i for i in range(1 << W1) if bin(i).count('1') == W2]
for a_mask in a_candidates:
    for b_mask in b_candidates:
        a_ind = [i for i in range(H1) if (a_mask >> i) & 1]
        b_ind = [j for j in range(W1) if (b_mask >> j) & 1]
      
        A2 = [A0[i] for i in a_ind]                    
        A3 = [[row[j] for j in b_ind] for row in A2]   

--------------------------------------

for a_ind in combinations(range(H1), H2):
    for b_ind in combinations(range(W1), W2):
      
        A2 = [A0[i] for i in a_ind]                   
        A3 = [[row[j] for j in b_ind] for row in A2]  
  
####################################
