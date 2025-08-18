##################################################################
問題文
N個の英小文字列S1​,S2​,…,SN​および整数Lが与えられます。
長さLの英小文字列であって、S1​,S2​,…,SN​をすべて部分文字列として含むものの個数を998244353で割った余りを求めてください。
制約
1≤N≤8
1≤L≤100
N,Lは整数
Si​は長さが1以上10以下の英小文字からなる文字列Si!=Sj​(i!=j)
input given as
N L
S1
S2
.
.
SN
solve this in python
##################################################################
sample1
2 4
ab
c
------
153
##################################################################
sample2
5 50
bbfogggj
zkbach
eedirhyc
ffgd
oemmswj
--------
689020583
##################################################################

##################################################################

##################################################################

##################################################################
[Gemini AC]
import sys
sys.setrecursionlimit(10**6)

N, L = map(int, input().split())
S = [input() for _ in range(N)]
MOD = 998244353

# Aho-Corasick オートマトンの構築
trie = [[0] * 26 for _ in range(1)]
out = [0]
link = [0]
node_count = 1

def add_string(s, pattern_id):
    global node_count
    node = 0
    for char in s:
        c = ord(char) - ord('a')
        if not trie[node][c]:
            trie[node][c] = node_count
            trie.append([0] * 26)
            out.append(0)
            link.append(0)
            node_count += 1
        node = trie[node][c]
    out[node] |= (1 << pattern_id)

for i in range(N):
    add_string(S[i], i)

queue = []
for c in range(26):
    if trie[0][c]:
        queue.append(trie[0][c])

head = 0
while head < len(queue):
    node = queue[head]
    head += 1
    for c in range(26):
        if trie[node][c]:
            failure = link[node]
            while failure > 0 and not trie[failure][c]:
                failure = link[failure]
            if trie[failure][c]:
                link[trie[node][c]] = trie[failure][c]
            
            out[trie[node][c]] |= out[link[trie[node][c]]]
            
            queue.append(trie[node][c])

# 事前に遷移テーブルを計算
next_v = [[0] * 26 for _ in range(node_count)]
next_mask = [[0] * 26 for _ in range(node_count)]

for v in range(node_count):
    for c in range(26):
        curr_v = v
        while curr_v > 0 and not trie[curr_v][c]:
            curr_v = link[curr_v]
        
        if trie[curr_v][c]:
            next_v[v][c] = trie[curr_v][c]
        else:
            next_v[v][c] = 0 # 根に戻る
        
        next_mask[v][c] = out[next_v[v][c]]

# DP
dp = [[[0] * (1 << N) for _ in range(node_count)] for _ in range(L + 1)]
dp[0][0][0] = 1

for i in range(L):
    for v in range(node_count):
        for mask in range(1 << N):
            if dp[i][v][mask] == 0:
                continue
            
            for c in range(26):
                next_node = next_v[v][c]
                new_mask = mask | next_mask[v][c]
                dp[i+1][next_node][new_mask] += dp[i][v][mask]
                dp[i+1][next_node][new_mask] %= MOD

# 結果の計算
ans = 0
for v in range(node_count):
    ans += dp[L][v][(1 << N) - 1]
    ans %= MOD

print(ans)
##################################################################
[CGPT AC]
#!/usr/bin/env python3
import sys
from collections import deque

MOD = 998244353

def build_aho(patterns):
    # patterns: list of strings
    # returns: next_table (nodes x 26), fail (nodes), outmask (nodes)
    nodes = 1
    trie = [ [-1]*26 ]  # children
    outmask = [0]
    # insert
    for idx, p in enumerate(patterns):
        cur = 0
        for ch in p:
            c = ord(ch) - 97
            if trie[cur][c] == -1:
                trie[cur][c] = nodes
                trie.append([-1]*26)
                outmask.append(0)
                nodes += 1
            cur = trie[cur][c]
        outmask[cur] |= (1<<idx)
    # build fail
    fail = [0]*nodes
    q = deque()
    # set children of root and push depth1 nodes
    for c in range(26):
        v = trie[0][c]
        if v != -1:
            fail[v] = 0
            q.append(v)
        else:
            trie[0][c] = 0  # direct transition to root
    # BFS
    while q:
        u = q.popleft()
        for c in range(26):
            v = trie[u][c]
            if v != -1:
                f = fail[u]
                fail[v] = trie[f][c]
                outmask[v] |= outmask[fail[v]]
                q.append(v)
            else:
                trie[u][c] = trie[fail[u]][c]
    return trie, fail, outmask

def main():
    data = sys.stdin.read().strip().splitlines()
    if not data: 
        return
    it = iter(data)
    first = next(it).strip().split()
    N = int(first[0]); L = int(first[1])
    patterns = []
    for _ in range(N):
        patterns.append(next(it).strip())
    # if any pattern longer than L -> impossible
    for p in patterns:
        if len(p) > L:
            print(0)
            return
    # build automaton
    trie, fail, outmask = build_aho(patterns)
    states = len(trie)
    FULL = (1<<N) - 1
    # precompute transitions: for each state, list of (next_state, outmask[next_state]) for 26 letters
    transpairs = [ [(trie[s][c], outmask[trie[s][c]]) for c in range(26)] for s in range(states) ]
    # DP: two layers over length
    M = 1<<N
    # initialize dp for length 0: at root state 0 with mask = outmask[0] (some patterns may be empty? here patterns length >=1 so outmask[0]==0)
    dp = [ [0]*M for _ in range(states) ]
    dp[0][ outmask[0] ] = 1
    for _ in range(L):
        nxt = [ [0]*M for _ in range(states) ]
        for s in range(states):
            row = dp[s]
            if not any(row):
                continue
            tp = transpairs[s]
            # iterate masks
            for m, val in enumerate(row):
                if val == 0:
                    continue
                v = val
                # for each letter
                for ns, add in tp:
                    nm = m | add
                    nxt[ns][nm] += v
                    if nxt[ns][nm] >= MOD:
                        nxt[ns][nm] -= MOD
        dp = nxt
    # sum over states where mask == FULL
    ans = 0
    for s in range(states):
        ans = (ans + dp[s][FULL]) % MOD
    print(ans)

if __name__ == "__main__":
    main()
##################################################################
[Capilot TLE]
MOD = 998244353

def solve():
    import sys

    def main():
        N, L = map(int, sys.stdin.readline().split())
        patterns = [sys.stdin.readline().strip() for _ in range(N)]
        from collections import deque, defaultdict

        # Build Aho-Corasick automaton (for all patterns)
        class Node:
            def __init__(self):
                self.next = {}
                self.fail = None
                self.output = 0 # bitmask of patterns matched here

        root = Node()
        # Insert patterns, mark output bitmask
        for idx, pat in enumerate(patterns):
            node = root
            for ch in pat:
                if ch not in node.next:
                    node.next[ch] = Node()
                node = node.next[ch]
            node.output |= (1 << idx)

        # Build fail links
        q = deque()
        for child in root.next.values():
            child.fail = root
            q.append(child)
        while q:
            rnode = q.popleft()
            for key, unode in rnode.next.items():
                q.append(unode)
                fnode = rnode.fail
                while fnode and key not in fnode.next:
                    fnode = fnode.fail
                unode.fail = fnode.next[key] if fnode and key in fnode.next else root
                unode.output |= unode.fail.output

        # Map nodes to indices for DP
        all_nodes = []
        node_id = {}
        def collect_nodes(node):
            if node in node_id: return
            idx = len(all_nodes)
            node_id[node] = idx
            all_nodes.append(node)
            for child in node.next.values():
                collect_nodes(child)
        collect_nodes(root)
        total_nodes = len(all_nodes)

        trans = [[0]*26 for _ in range(total_nodes)]
        outmask = [0]*total_nodes
        for idx, node in enumerate(all_nodes):
            outmask[idx] = node.output
            for c in range(26):
                ch = chr(ord('a') + c)
                nnode = node
                while nnode and ch not in nnode.next:
                    nnode = nnode.fail
                nnode = nnode.next[ch] if nnode and ch in nnode.next else root
                trans[idx][c] = node_id[nnode]

        from collections import defaultdict
        DP = [defaultdict(int) for _ in range(L+1)]
        DP[0][(0, 0)] = 1

        for pos in range(L):
            for (state, mask), count in DP[pos].items():
                for c in range(26):
                    nstate = trans[state][c]
                    nmask = mask | outmask[nstate]
                    DP[pos+1][(nstate, nmask)] = (DP[pos+1][(nstate, nmask)] + count) % MOD

        full_mask = (1 << N) - 1
        ans = 0
        for (state, mask), count in DP[L].items():
            if mask == full_mask:
                ans = (ans + count) % MOD
        print(ans)

    main()

solve()
##################################################################
[kazuki]
from collections import deque

MOD = 998244353
ALPHA = 26

N, L = map(int, input().split())
S = [input() for _ in range(N)]

keep = [True] * N
for i in range(N):
    for j in range(N):
        if i != j and S[i] in S[j]:
            keep[i] = False
            break
S = [S[i] for i in range(N) if keep[i]]
N = len(S)

nexts = [[-1] * ALPHA]
link = [0]
out = [0]


def add_word(word, idx):
    v = 0
    for ch in word:
        c = ord(ch) - 97
        if nexts[v][c] == -1:
            nexts[v][c] = len(nexts)
            nexts.append([-1] * ALPHA)
            link.append(0)
            out.append(0)
        v = nexts[v][c]
    out[v] |= 1 << idx


for i, w in enumerate(S):
    add_word(w, i)

m = len(nexts)
go = [[0] * ALPHA for _ in range(m)]

q = deque()
for c in range(ALPHA):
    u = nexts[0][c]
    if u != -1:
        link[u] = 0
        go[0][c] = u
        q.append(u)
    else:
        go[0][c] = 0

while q:
    v = q.popleft()
    for c in range(ALPHA):
        u = nexts[v][c]
        if u != -1:
            link[u] = go[link[v]][c]
            out[u] |= out[link[u]]
            go[v][c] = u
            q.append(u)
        else:
            go[v][c] = go[link[v]][c]

full = (1 << N) - 1
Snum = m
dp = [[0] * (1 << N) for _ in range(Snum)]
dp[0][0] = 1

for _ in range(L):
    ndp = [[0] * (1 << N) for _ in range(Snum)]
    for s in range(Snum):
        row = dp[s]
        if not any(row):
            continue
        g = go[s]
        for c in range(ALPHA):
            ns = g[c]
            mask_add = out[ns]
            tgt = ndp[ns]
            for mask, val in enumerate(row):
                if val:
                    tgt[mask | mask_add] = (tgt[mask | mask_add] + val) % MOD
    dp = ndp

ans = sum(dp[s][full] for s in range(Snum)) % MOD
print(ans)

##################################################################
[yup]
import sys
input = sys.stdin.readline
from collections import deque
class AhoCorasick:
    def __init__(self, sigma=26):
        self.node = [[-1] * sigma]
        self.last = [0]
        self.sigma = sigma
    def add(self, arr, ID):
        v = 0
        for c in arr:
            if self.node[v][c] == -1:
                self.node[v][c] = len(self.node)
                self.node.append([-1] * self.sigma)
                self.last.append(0)
            v = self.node[v][c]
        self.last[v] |= 1 << ID
    def build(self):
        link = [0] * len(self.node)
        que = deque()
        for i in range(self.sigma):
            if self.node[0][i] == -1:
                self.node[0][i] = 0
            else:
                link[self.node[0][i]] = 0
                que.append(self.node[0][i])
        while que:
            v = que.popleft()
            self.last[v] |= self.last[link[v]]
            for i in range(self.sigma):
                u = self.node[v][i]
                if u == -1:
                    self.node[v][i] = self.node[link[v]][i]
                else:
                    link[u] = self.node[link[v]][i]
                    que.append(u)
mod=998244353
n,l=map(int,input().split())
AC=AhoCorasick()
for i in range(n):
  s=input().rstrip()
  AC.add([ord(c)-ord("a") for c in s], i)
AC.build()
m=len(AC.node)
dp=[[0]*(1<<n) for _ in range(m)]
dp[0][0]=1
for _ in range(l):
  dp2=[[0]*(1<<n) for _ in range(m)]
  for i in range(m):
    for j in range(1<<n):
      for k in range(26):
        ni=AC.node[i][k]
        nj=j|AC.last[ni]
        dp2[ni][nj]+=dp[i][j]
        dp2[ni][nj]%=mod
  dp=dp2
ans=0
for i in range(m):
  ans+=dp[i][-1]
  ans%=mod
print(ans)
##################################################################
[jva]
import sys
from collections import deque
input = sys.stdin.readline
MOD = 998244353

n, L = map(int, input().split())
p = [input().strip() for _ in range(n)]

A = 26
t = [[-1]*A]
o = [0]

for i, s in enumerate(p):
    v = 0
    for ch in s:
        c = ord(ch)-97
        if t[v][c] == -1:
            t[v][c] = len(t)
            t.append([-1]*A)
            o.append(0)
        v = t[v][c]
    o[v] |= (1<<i)

f = [0]*len(t)
q = deque()
for c in range(A):
    v = t[0][c]
    if v != -1:
        f[v] = 0
        q.append(v)
    else:
        t[0][c] = 0

while q:
    v = q.popleft()
    fv = f[v]
    o[v] |= o[fv]
    for c in range(A):
        to = t[v][c]
        if to != -1:
            f[to] = t[fv][c]
            q.append(to)
        else:
            t[v][c] = t[fv][c]

m = len(t)
fm = (1<<n)-1

d = [ [0]* (1<<n) for _ in range(m) ]
d[0][o[0]] = 1

for _ in range(L):
    nd = [ [0]* (1<<n) for _ in range(m) ]
    for v in range(m):
        row = d[v]
        for mask in range(1<<n):
            cur = row[mask]
            if cur:
                for c in range(A):
                    to = t[v][c]
                    nm = mask | o[to]
                    nd[to][nm] = (nd[to][nm] + cur) % MOD
    d = nd

ans = 0
for v in range(m):
    ans = (ans + d[v][fm]) % MOD
print(ans)

##################################################################
[toam]
from collections import deque


class AhoCorasick:
    def __init__(self, sigma=26):
        self.node = [[-1] * sigma]
        self.last = [0]
        self.sigma = sigma

    def add(self, arr, ID):
        v = 0
        for c in arr:
            if self.node[v][c] == -1:
                self.node[v][c] = len(self.node)
                self.node.append([-1] * self.sigma)
                self.last.append(0)
            v = self.node[v][c]
        self.last[v] |= 1 << ID

    def build(self):
        link = [0] * len(self.node)
        que = deque()
        for i in range(self.sigma):
            if self.node[0][i] == -1:
                self.node[0][i] = 0
            else:
                link[self.node[0][i]] = 0
                que.append(self.node[0][i])

        while que:
            v = que.popleft()
            self.last[v] |= self.last[link[v]]
            for i in range(self.sigma):
                u = self.node[v][i]
                if u == -1:
                    self.node[v][i] = self.node[link[v]][i]
                else:
                    link[u] = self.node[link[v]][i]
                    que.append(u)


mod = 998244353


N, L = map(int, input().split())
AC = AhoCorasick()
for i in range(N):
    AC.add([ord(c) - ord("a") for c in input()], i)

AC.build()
m = len(AC.node)
dp = [[0] * m for i in range(1 << N)]
dp[0][0] = 1
for _ in range(L):
    ndp = [[0] * m for i in range(1 << N)]
    for bit in range(1 << N):
        for v in range(m):
            for i in range(26):
                to = AC.node[v][i]
                nbit = bit | AC.last[to]
                ndp[nbit][to] = (dp[bit][v] + ndp[nbit][to]) % mod
    dp = ndp
print(sum(dp[-1]) % mod)

##################################################################
[titia TLE]
import sys
input = sys.stdin.readline

from collections import Counter

N,L=map(int,input().split())

S=[input().strip() for i in range(N)]

LIST=[[[] for i in range(len(S[j])+1)] for j in range(N)]

for i in range(N):
    for j in range(len(LIST[i])):
        LIST[i][j].append(j)

for i in range(N):
    s=S[i]
    for start in range(1,len(s)):
        for j in range(len(s)):
            if start+j<len(s) and s[j]==s[start+j]:
                #print(i,j,start)
                LIST[i][start+j+1].append(j+1)
            else:
                break

        #print(LIST)

for i in range(N):
    for j in range(len(LIST[i])):
        LIST[i][j].append(0)
                
        
    


mod=998244353

DP=dict()
DP[tuple([0]*N)]=1

for tt in range(L):
    #print(DP)
    NDP=Counter()

    for dp in DP:
        for j in range(26):
            ndp=list(dp)
            
            for i in range(N):
                if dp[i]==len(S[i]):
                    continue
                ndp[i]=0

                #print(LIST[i][dp[i]])

                for l in LIST[i][dp[i]]:
                    if ord(S[i][l])-97==j:
                        ndp[i]=l+1
                        break

            NDP[tuple(ndp)]=(NDP[tuple(ndp)]+DP[dp])%mod

    DP=NDP

X=[len(S[i]) for i in range(N)]

ANS=DP[tuple(X)]

print(ANS%mod)

##################################################################
[MyAi AC]
MOD = 998244353

class Node:
    def __init__(self):
        self.next = {}
        self.fail = None
        self.output = 0

def build_ac(words):
    root = Node()
    for i, w in enumerate(words):
        node = root
        for c in w:
            if c not in node.next:
                node.next[c] = Node()
            node = node.next[c]
        node.output |= (1 << i)
    queue = []
    for c in root.next:
        root.next[c].fail = root
        queue.append(root.next[c])
    while queue:
        rnode = queue.pop(0)
        for c, unode in rnode.next.items():
            queue.append(unode)
            fnode = rnode.fail
            while fnode and c not in fnode.next:
                fnode = fnode.fail
            unode.fail = fnode.next[c] if fnode and c in fnode.next else root
            unode.output |= unode.fail.output
    return root

def solve(L, words):
    root = build_ac(words)
    nodes = []
    node_id = {}
    def dfs(node):
        if node in node_id:
            return
        node_id[node] = len(nodes)
        nodes.append(node)
        for c in node.next.values():
            dfs(c)
    dfs(root)
    n_nodes = len(nodes)

    trans = [[0]*26 for _ in range(n_nodes)]
    for i, node in enumerate(nodes):
        for ci, c in enumerate("abcdefghijklmnopqrstuvwxyz"):
            nxt = node
            while nxt and c not in nxt.next:
                nxt = nxt.fail
            nxt = nxt.next[c] if nxt and c in nxt.next else root
            trans[i][ci] = node_id[nxt]

    dp = [[0]*(1<<len(words)) for _ in range(n_nodes)]
    dp[node_id[root]][0] = 1

    for _ in range(L):
        new_dp = [[0]*(1<<len(words)) for _ in range(n_nodes)]
        for i in range(n_nodes):
            for mask in range(1<<len(words)):
                val = dp[i][mask]
                if val == 0:
                    continue
                for ci in range(26):
                    nxt_id = trans[i][ci]
                    new_mask = mask | nodes[nxt_id].output
                    new_dp[nxt_id][new_mask] = (new_dp[nxt_id][new_mask] + val) % MOD
        dp = new_dp

    full = (1<<len(words))-1
    ans = sum(dp[i][full] for i in range(n_nodes)) % MOD
    return ans

N, L = map(int, input().split())
S = [input().strip() for _ in range(N)]
print(solve(L, S))

##################################################################
