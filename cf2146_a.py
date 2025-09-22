###############################################
###############################################
A. Equal Occurrences
time limit per test1 second
memory limit per test256 megabytes

We call an array balanced if and only if the numbers of occurrences of any of its elements are the same. 
For example, [1,1,3,3,6,6] and [2,2,2,2] are balanced, 
but [1,2,3,3] is not balanced (the numbers of occurrences of elements 1 and 3 are different). 
Note that an empty array is always balanced.

You are given a non-decreasing array 𝑎 consisting of 𝑛 integers. 
Find the length of its longest balanced subsequence∗
.

∗
A sequence 𝑏
 is a subsequence of a sequence 𝑎
 if 𝑏 can be obtained from 𝑎 by the deletion of several (possibly, zero or all) element from arbitrary positions.

Input
Each test contains multiple test cases. The first line contains the number of test cases 𝑡
 (1≤𝑡≤500
). 

The description of the test cases follows.

The first line of each test case contains a single integer 𝑛
 (1≤𝑛≤100) — the length of 𝑎
.

The second line contains 𝑛
 integers 𝑎1,𝑎2,…,𝑎𝑛
 (1≤𝑎1≤𝑎2≤⋯≤𝑎𝑛≤𝑛) — the elements of 𝑎
.

Output
For each test case, output a single integer — the length of the longest balanced subsequence of 𝑎
.

Example
InputCopy
4
5
1 1 4 4 4
2
1 2
15
1 1 1 1 1 2 2 2 2 3 3 3 4 4 5
5
3 3 3 3 3
OutputCopy
4
2
9
5
###############################################
[gemini AC]
import sys
from collections import Counter

def solve():
    n = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))
    
    # Count frequencies of each number
    counts = Counter(a)
    
    # Get the list of frequencies
    freq_values = list(counts.values())
    
    max_len = 0
    
    # Iterate through all possible frequencies for a balanced subsequence
    # The maximum possible frequency is the length of the array, n.
    for k in range(1, n + 1):
        # Count how many distinct numbers appear at least k times
        distinct_count = 0
        for freq in freq_values:
            if freq >= k:
                distinct_count += 1
        
        # Calculate the length of the balanced subsequence for this k
        current_len = k * distinct_count
        
        # Update the maximum length found so far
        if current_len > max_len:
            max_len = current_len
            
    print(max_len)

def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()
###############################################
[deepseek AC]
t = int(input().strip())
results = []
for _ in range(t):
    n = int(input().strip())
    arr = list(map(int, input().split()))
    if n == 0:
        results.append(0)
        continue
    freqs = []
    count = 1
    for i in range(1, n):
        if arr[i] == arr[i-1]:
            count += 1
        else:
            freqs.append(count)
            count = 1
    freqs.append(count)
    
    max_freq = max(freqs) if freqs else 0
    best = 0
    for k in range(1, max_freq+1):
        groups = 0
        for f in freqs:
            if f >= k:
                groups += 1
        total = k * groups
        if total > best:
            best = total
    results.append(best)

for res in results:
    print(res)
###############################################
[my AC]
from collections import Counter

def longest_equal(lst):
    freq = Counter(lst)
    max_len = 0
    max_count = max(freq.values(), default=0)
    for c in range(1, max_count + 1):
        k = sum(1 for v in freq.values() if v >= c)
        max_len = max(max_len, k * c)
    return max_len

N=int(input())
A=[]
for _ in range(N):
  m=int(input())
  M=list(map(int,input().split()))  
  print(longest_equal(M)) 
          
###############################################

###############################################
###############################################
###############################################
[ai AC]
def solve():
    n = int(input())
    a = list(map(int, input().split()))
 
    # Step 1: Count frequencies of each number
    counts = {}
    for x in a:
        counts[x] = counts.get(x, 0) + 1
 
    # Step 2: Store the frequencies of the counts
    freq_counts = {}
    for val in counts.values():
        freq_counts[val] = freq_counts.get(val, 0) + 1
    
    max_len = 0
    
    # Iterate through all possible frequencies k
    for k in range(1, n + 1):
        num_elements = 0
        # Step 3: Count how many elements have frequency >= k
        for freq, count in freq_counts.items():
            if freq >= k:
                num_elements += count
        
        current_len = k * num_elements
        max_len = max(max_len, current_len)
        
    print(max_len)
 
 
t = int(input())
for _ in range(t):
    solve()
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
