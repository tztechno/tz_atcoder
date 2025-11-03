###############################################
from sortedcontainers import SortedSet

s = SortedSet()
または初期化時にリストや集合を渡すこともできます：

s = SortedSet([5, 1, 3, 2, 4])
print(s)  # SortedSet([1, 2, 3, 4, 5])
###############################################
###############################################
###############################################
###############################################
###############################################
###############################################
[hobbit]
from sortedcontainers import SortedDict

N = int(input())
X = [*map(int, input().split())]

ans = 0
INF = 10**18
D = SortedDict()
D[0] = INF
for x in X:
    pos = D.bisect_left(x)
    if pos == len(D):  # 末尾に追加
        pre_x, pre_d = D.peekitem()  # 今の末尾取得 (x,dist)
        if pre_d != INF:
            ans -= pre_d
        d = abs(x - pre_x)
        mn = min(pre_d, d)
        D[pre_x] = mn
        D[x] = d
        ans += mn + d
    else:  # 1<=pos, pos!=0
        r = pos
        l = r - 1
        l_x, l_d = D.peekitem(l)
        r_x, r_d = D.peekitem(r)
        a = x - l_x
        b = r_x - x
        D[x] = min(a, b)
        D[l_x] = min(a, l_d)
        D[r_x] = min(r_d, b)
        ans -= l_d + r_d
        ans += D[x] + D[l_x] + D[r_x]
    print(ans)

###############################################
###############################################
[yphs]
from collections import defaultdict
from sortedcontainers import SortedSet

INF = 1 << 100

N = int(input())
X = list(map(int, input().split()))

cnt = defaultdict(int)
md = defaultdict(int)
for x in X:
    md[x] = INF
cnt[0] = 1
md[0] = INF
ss = SortedSet([0, INF])

ans = 0
for x in X:
    ss.add(x)
    pos = ss.bisect_left(x)
    l, r = ss[pos-1], ss[pos+1]

    ans -= md[x]*cnt[x]
    cnt[x] += 1
    if cnt[x] >= 2:
        md[x] = 0
    md[x] = min(md[x], x-l, r-x)
    ans += md[x]*cnt[x]

    if md[l] > x-l and cnt[l] == 1:
        ans -= md[l] if md[l] < INF else 0
        ans += x-l
        md[l] = x-l

    if md[r] > r-x and cnt[r] == 1:
        ans -= md[r] if md[r] < INF else 0
        ans += r-x
        md[r] = r-x

    print(ans)

###############################################
###############################################
[titia]
import sys
input = sys.stdin.readline

# https://github.com/tatyam-prime/SortedSet/blob/main/SortedSet.py
import math
from bisect import bisect_left, bisect_right
from typing import Generic, Iterable, Iterator, TypeVar
T = TypeVar('T')

class SortedSet(Generic[T]):
    BUCKET_RATIO = 16
    SPLIT_RATIO = 24
    
    def __init__(self, a: Iterable[T] = []) -> None:
        "Make a new SortedSet from iterable. / O(N) if sorted and unique / O(N log N)"
        a = list(a)
        n = len(a)
        if any(a[i] > a[i + 1] for i in range(n - 1)):
            a.sort()
        if any(a[i] >= a[i + 1] for i in range(n - 1)):
            a, b = [], a
            for x in b:
                if not a or a[-1] != x:
                    a.append(x)
        n = self.size = len(a)
        num_bucket = int(math.ceil(math.sqrt(n / self.BUCKET_RATIO)))
        self.a = [a[n * i // num_bucket : n * (i + 1) // num_bucket] for i in range(num_bucket)]

    def __iter__(self) -> Iterator[T]:
        for i in self.a:
            for j in i: yield j

    def __reversed__(self) -> Iterator[T]:
        for i in reversed(self.a):
            for j in reversed(i): yield j
    
    def __eq__(self, other) -> bool:
        return list(self) == list(other)
    
    def __len__(self) -> int:
        return self.size
    
    def __repr__(self) -> str:
        return "SortedSet" + str(self.a)
    
    def __str__(self) -> str:
        s = str(list(self))
        return "{" + s[1 : len(s) - 1] + "}"

    def _position(self, x: T) -> tuple[list[T], int, int]:
        "return the bucket, index of the bucket and position in which x should be. self must not be empty."
        for i, a in enumerate(self.a):
            if x <= a[-1]: break
        return (a, i, bisect_left(a, x))

    def __contains__(self, x: T) -> bool:
        if self.size == 0: return False
        a, _, i = self._position(x)
        return i != len(a) and a[i] == x

    def add(self, x: T) -> bool:
        "Add an element and return True if added. / O(√N)"
        if self.size == 0:
            self.a = [[x]]
            self.size = 1
            return True
        a, b, i = self._position(x)
        if i != len(a) and a[i] == x: return False
        a.insert(i, x)
        self.size += 1
        if len(a) > len(self.a) * self.SPLIT_RATIO:
            mid = len(a) >> 1
            self.a[b:b+1] = [a[:mid], a[mid:]]
        return True
    
    def _pop(self, a: list[T], b: int, i: int) -> T:
        ans = a.pop(i)
        self.size -= 1
        if not a: del self.a[b]
        return ans

    def discard(self, x: T) -> bool:
        "Remove an element and return True if removed. / O(√N)"
        if self.size == 0: return False
        a, b, i = self._position(x)
        if i == len(a) or a[i] != x: return False
        self._pop(a, b, i)
        return True
    
    def lt(self, x: T) -> T | None:
        "Find the largest element < x, or None if it doesn't exist."
        for a in reversed(self.a):
            if a[0] < x:
                return a[bisect_left(a, x) - 1]

    def le(self, x: T) -> T | None:
        "Find the largest element <= x, or None if it doesn't exist."
        for a in reversed(self.a):
            if a[0] <= x:
                return a[bisect_right(a, x) - 1]

    def gt(self, x: T) -> T | None:
        "Find the smallest element > x, or None if it doesn't exist."
        for a in self.a:
            if a[-1] > x:
                return a[bisect_right(a, x)]

    def ge(self, x: T) -> T | None:
        "Find the smallest element >= x, or None if it doesn't exist."
        for a in self.a:
            if a[-1] >= x:
                return a[bisect_left(a, x)]
    
    def __getitem__(self, i: int) -> T:
        "Return the i-th element."
        if i < 0:
            for a in reversed(self.a):
                i += len(a)
                if i >= 0: return a[i]
        else:
            for a in self.a:
                if i < len(a): return a[i]
                i -= len(a)
        raise IndexError
    
    def pop(self, i: int = -1) -> T:
        "Pop and return the i-th element."
        if i < 0:
            for b, a in enumerate(reversed(self.a)):
                i += len(a)
                if i >= 0: return self._pop(a, ~b, i)
        else:
            for b, a in enumerate(self.a):
                if i < len(a): return self._pop(a, b, i)
                i -= len(a)
        raise IndexError
    
    def index(self, x: T) -> int:
        "Count the number of elements < x."
        ans = 0
        for a in self.a:
            if a[-1] >= x:
                return ans + bisect_left(a, x)
            ans += len(a)
        return ans

    def index_right(self, x: T) -> int:
        "Count the number of elements <= x."
        ans = 0
        for a in self.a:
            if a[-1] > x:
                return ans + bisect_right(a, x)
            ans += len(a)
        return ans

N=int(input())
A=list(map(int,input().split()))

LIST=[0]*(N+1)
S=SortedSet()
S.add((0,0))
ANS=0

for i in range(N):
    a=A[i]
    S.add((a,i+1))

    k=S.index((a,i+1))

    X=[]

    if k-1>=0:
        c,ind=S[k-1]
        
        Y=[a-c]
        X.append(a-c)

        if k-2>=0:
            cc,ind2=S[k-2]
            Y.append(c-cc)

        MIN=min(Y)

        ANS+=MIN-LIST[ind]
        LIST[ind]=MIN

    if k+1<len(S):
        c,ind=S[k+1]
        
        Y=[c-a]
        X.append(c-a)

        if k+2<len(S):
            cc,ind2=S[k+2]
            Y.append(cc-c)

        MIN=min(Y)

        ANS+=MIN-LIST[ind]
        LIST[ind]=MIN

    MIN=min(X)

    ANS+=MIN-LIST[i+1]
    LIST[i+1]=MIN


    print(ANS)


###############################################
