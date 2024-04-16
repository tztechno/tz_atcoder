######################################################################
######################################################################
######################################################################
######################################################################
######################################################################
######################################################################
H, W, N = map(int, input().split())
T = input()
dp = {'L': 1, 'R': -1, 'U': W, 'D': -W}
grid = 0
for _ in range(H):
    grid = (grid<<W)+int(input().replace('#', '0').replace('.', '1'), 2)
now = grid
for _t in T:
    shift = dp[_t]
    if shift > 0:
        now <<= shift
    else:
        now >>= -shift
    now &= grid
print(now.bit_count())
######################################################################
######################################################################
H, W, N = map(int, input().split())
T = input()
S = [input() for _ in range(H)]
ans = 0
for i in range(1, H - 1):
	for j in range(1, W - 1):
		if S[i][j] == '.':
			ok = True
			ni, nj = i, j
			for c in T:
				if c == 'L':
					nj -= 1
				if c == 'R':
					nj += 1
				if c == 'U':
					ni -= 1
				if c == 'D':
					ni += 1
				if S[ni][nj] == '#':
					ok = False
					break
			if ok:
				ans += 1
print(ans)
######################################################################
######################################################################
H, W, N = map(int, input().split())
T = input()
S = [list(input()) for h in range(H)]

count = 0
for I in range(1, H - 1):
    for J in range(1, W - 1):
        if S[I][J] == '#':
            continue
        i = I
        j = J
        for t in T:
            if t == 'L':
                j -= 1
            elif t == 'R':
                j += 1
            elif t == 'U':
                i -= 1
            else:
                i += 1

            if S[i][j] == '#':
                break
        else:
            count += 1

print(count)

######################################################################
######################################################################
######################################################################
######################################################################

TLE: python,php,kotlin,
AC: C++,C#,rust,go,java,

######################################################################

#kotlin,TLE

import java.util.Scanner

fun movePiece(pos: Pair<Int, Int>, t: CharArray, s: Array<CharArray>, map: Map<Char, Pair<Int, Int>>): Int {
    var c = 1
    var currentPos = pos
    for (direction in t) {
        val moveBy = map[direction]
        currentPos = Pair(currentPos.first + moveBy!!.first, currentPos.second + moveBy.second)
        if (currentPos.first < 0 || currentPos.first >= s.size || currentPos.second < 0 || currentPos.second >= s[0].size) {
            continue
        }
        if (s[currentPos.first][currentPos.second] == '#') {
            c = 0
            break
        }
    }
    return c
}

fun main() {
    val scanner = Scanner(System.`in`)

    val (h, w, n) = scanner.nextLine().split(" ").map { it.toInt() }

    val t = scanner.nextLine().toCharArray()

    val s = Array(h) { CharArray(w) }
    val p = mutableListOf<Pair<Int, Int>>()

    for (i in 0 until h) {
        val line = scanner.nextLine().toCharArray()
        s[i] = line
        for (j in 0 until w) {
            if (line[j] == '.') {
                p.add(Pair(i, j))
            }
        }
    }

    val map = mapOf('U' to Pair(-1, 0), 'D' to Pair(1, 0), 'R' to Pair(0, 1), 'L' to Pair(0, -1))

    var count = 0
    for (pos in p) {
        val add = movePiece(pos, t, s, map)
        count += add
    }

    println(count)
}


######################################################################

＃javaでAC

import java.util.Scanner;
import java.util.ArrayList;
import java.util.HashMap;

public class Main {

    public static int movePiece(int[] pos, char[] t, char[][] s, HashMap<Character, int[]> map) {
        int c = 1;
        int[] currentPos = new int[]{pos[0], pos[1]};
        for (char direction : t) {
            int[] moveBy = map.get(direction);
            currentPos[0] += moveBy[0];
            currentPos[1] += moveBy[1];
            if (currentPos[0] < 0 || currentPos[0] >= s.length || currentPos[1] < 0 || currentPos[1] >= s[0].length) {
                continue;
            }
            if (s[currentPos[0]][currentPos[1]] == '#') {
                c = 0;
                break;
            }
        }
        return c;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        String[] inputs = scanner.nextLine().split(" ");
        int h = Integer.parseInt(inputs[0]);
        int w = Integer.parseInt(inputs[1]);
        int n = Integer.parseInt(inputs[2]);

        char[] t = scanner.nextLine().toCharArray();

        char[][] s = new char[h][w];
        ArrayList<int[]> p = new ArrayList<>();

        for (int i = 0; i < h; i++) {
            String line = scanner.nextLine();
            char[] row = line.toCharArray();
            s[i] = row;
            for (int j = 0; j < w; j++) {
                if (row[j] == '.') {
                    p.add(new int[]{i, j});
                }
            }
        }

        HashMap<Character, int[]> map = new HashMap<>();
        map.put('U', new int[]{-1, 0});
        map.put('D', new int[]{1, 0});
        map.put('R', new int[]{0, 1});
        map.put('L', new int[]{0, -1});

        int count = 0;
        for (int[] pos : p) {
            int add = movePiece(pos, t, s, map);
            count += add;
        }

        System.out.println(count);
    }
}

​
######################################################################

#C#に変換、ACぎり
​
using System;
using System.Collections.Generic;
​
class Program
{
    static int MovePiece((int, int) pos, char[] t, char[][] s, Dictionary<char, (int, int)> map)
    {
        int c = 1;
        var currentPos = pos;
        foreach (var direction in t)
        {
            var moveBy = map[direction];
            currentPos.Item1 += moveBy.Item1;
            currentPos.Item2 += moveBy.Item2;
            if (s[currentPos.Item1][currentPos.Item2] == '#')
            {
                c = 0;
                break;
            }
        }
        return c;
    }
​
    static void Main(string[] args)
    {
        string[] inputs = Console.ReadLine().Split();
        int h = int.Parse(inputs[0]);
        int w = int.Parse(inputs[1]);
        int n = int.Parse(inputs[2]);
​
        char[] t = Console.ReadLine().ToCharArray();
​
        char[][] s = new char[h][];
        List<(int, int)> p = new List<(int, int)>();
​
        for (int i = 0; i < h; i++)
        {
            s[i] = Console.ReadLine().ToCharArray();
            for (int j = 0; j < w; j++)
            {
                if (s[i][j] == '.')
                {
                    p.Add((i, j));
                }
            }
        }
​
        Dictionary<char, (int, int)> map = new Dictionary<char, (int, int)>
        {
            {'U', (-1, 0)},
            {'D', (1, 0)},
            {'R', (0, 1)},
            {'L', (0, -1)}
        };
​
        int count = 0;
        foreach (var pos in p)
        {
            int add = MovePiece(pos, t, s, map);
            count += add;
        }
​
        Console.WriteLine(count);
    }
}
​
######################################################################

#goに変換,AC
​
package main
​
import (
    "bufio"
    "fmt"
    "os"
)
​
func movePiece(pos [2]int, t []rune, s [][]rune, m map[rune][2]int) int {
    c := 1
    currentPos := pos
    for _, direction := range t {
        moveBy := m[direction]
        currentPos[0] += moveBy[0]
        currentPos[1] += moveBy[1]
        if s[currentPos[0]][currentPos[1]] == '#' {
            c = 0
            break
        }
    }
    return c
}
​
func main() {
    scanner := bufio.NewScanner(os.Stdin)
​
    var h, w, n int
    fmt.Scan(&h, &w, &n)
​
    var t []rune
    scanner.Scan()
    t = []rune(scanner.Text())
​
    var s [][]rune
    var p [][2]int
​
    for i := 0; i < h; i++ {
        scanner.Scan()
        line := scanner.Text()
        row := []rune(line)
        s = append(s, row)
        for j := 0; j < w; j++ {
            if row[j] == '.' {
                p = append(p, [2]int{i, j})
            }
        }
    }
​
    m := map[rune][2]int{
        'U': {-1, 0},
        'D': {1, 0},
        'R': {0, 1},
        'L': {0, -1},
    }
​
    count := 0
    for _, pos := range p {
        add := movePiece(pos, t, s, m)
        count += add
    }
​
    fmt.Println(count)
}
​
######################################################################

#php変換ではTLE
​
<?php
​
function move_piece($pos, $t, $s, $map) {
    $c = 1;
    $current_pos = $pos;
    foreach ($t as $direction) {
        $move_by = $map[$direction];
        $current_pos[0] += $move_by[0];
        $current_pos[1] += $move_by[1];
        if ($s[$current_pos[0]][$current_pos[1]] === '#') {
            $c = 0;
            break;
        }
    }
    return $c;
}
​
$input = explode(" ", readline());
$h = (int)$input[0];
$w = (int)$input[1];
$n = (int)$input[2];
​
$t = str_split(readline());
​
$s = [];
$p = [];
for ($i = 0; $i < $h; $i++) {
    $si = str_split(readline());
    $s[] = $si;
    for ($j = 0; $j < $w; $j++) {
        if ($si[$j] === '.') {
            $p[] = [$i, $j];
        }
    }
}
​
$map = [
    'U' => [-1, 0],
    'D' => [1, 0],
    'R' => [0, 1],
    'L' => [0, -1]
];
​
$count = 0;
foreach ($p as $pos) {
    $add = move_piece($pos, $t, $s, $map);
    $count += $add;
}
​
echo $count . PHP_EOL;
​
?>
​
######################################################################

#C++変換でAC

#include <iostream>
#include <vector>
#include <unordered_map>
​
using namespace std;
​
int move_piece(pair<int, int> pos, vector<char>& t, vector<vector<char>>& s, unordered_map<char, pair<int, int>>& map) {
    int c = 1;
    pair<int, int> current_pos = pos;
    for (char direction : t) {
        auto move_by = map[direction];
        current_pos.first += move_by.first;
        current_pos.second += move_by.second;
        if (s[current_pos.first][current_pos.second] == '#') {
            c = 0;
            break;
        }
    }
    return c;
}
​
int main() {
    int h, w, n;
    cin >> h >> w >> n;
    
    vector<char> t(n);
    for (int i = 0; i < n; ++i) {
        cin >> t[i];
    }
​
    vector<vector<char>> s(h, vector<char>(w));
    vector<pair<int, int>> p;
    for (int i = 0; i < h; ++i) {
        for (int j = 0; j < w; ++j) {
            cin >> s[i][j];
            if (s[i][j] == '.') {
                p.push_back({i, j});
            }
        }
    }
​
    unordered_map<char, pair<int, int>> map = {
        {'U', {-1, 0}},
        {'D', {1, 0}},
        {'R', {0, 1}},
        {'L', {0, -1}}
    };
​
    int count = 0;
    for (auto pos : p) {
        int add = move_piece(pos, t, s, map);
        count += add;
    }
​
    cout << count << endl;
​
    return 0;
}
​
######################################################################

#rust変換でAC
​
use std::io::{self, BufRead};
​
fn main() {
    let stdin = io::stdin();
    let mut lines = stdin.lock().lines().map(|x| x.unwrap());
​
    let mut input = lines.next().unwrap();
    let mut iter = input.split_whitespace();
    let h: usize = iter.next().unwrap().parse().unwrap();
    let w: usize = iter.next().unwrap().parse().unwrap();
    let n: usize = iter.next().unwrap().parse().unwrap();
​
    let t: Vec<char> = lines.next().unwrap().chars().collect();
​
    let mut s: Vec<Vec<char>> = Vec::new();
    let mut p: Vec<(usize, usize)> = Vec::new();
​
    for _ in 0..h {
        let line: Vec<char> = lines.next().unwrap().chars().collect();
        s.push(line.clone());
        for j in 0..w {
            if line[j] == '.' {
                p.push((s.len() - 1, j));
            }
        }
    }
​
    let mut map: std::collections::HashMap<char, (i32, i32)> = std::collections::HashMap::new();
    map.insert('U', (-1, 0));
    map.insert('D', (1, 0));
    map.insert('R', (0, 1));
    map.insert('L', (0, -1));
​
    let mut count = 0;
    for pos in p.iter() {
        let add = move_piece(*pos, &t, &s, &map);
        count += add;
    }
​
    println!("{}", count);
}
​
fn move_piece(pos: (usize, usize), t: &Vec<char>, s: &Vec<Vec<char>>, map: &std::collections::HashMap<char, (i32, i32)>) -> usize {
    let mut c = 1;
    let mut current_pos = (pos.0 as i32, pos.1 as i32);
    for &direction in t.iter() {
        let move_by = map.get(&direction).unwrap();
        current_pos.0 += move_by.0;
        current_pos.1 += move_by.1;
        if s[current_pos.0 as usize][current_pos.1 as usize] == '#' {
            c = 0;
            break;
        }
    }
    c as usize
}

######################################################################

#minor改善
#python
#TLE2

H,W,N=map(int,input().split())
T=list(input())
S=[]
P=[]
for i in range(H):
  si=list(input())
  S+=[si]
  for j in range(W):
    if si[j]=='.':
      P+=[(i,j)]

map=dict()
map['U']=(-1,0)
map['D']=(1,0)
map['R']=(0,1)
map['L']=(0,-1)

def move(p,T):
  c=1
  for t in T:
    p=(p[0]+map[t][0],p[1]+map[t][1])
    if S[p[0]][p[1]]=='#':
      c=0
      break
  if c==1:
    return 1
  else:
    return 0

C=0
for p in P:
  ad=move(p,T)
  C+=ad

print(C)

######################################################################

[my AC]
[prepare map dict]
[fuction of list of start * list of direction]

H,W,N=map(int,input().split())
T=list(input())

S=[]
P=[]
for i in range(H):
  si=list(input())
  S+=[si]
  for j in range(W):
    if si[j]=='.':
      P+=[(i,j)]

map={'U':(-1,0),'D':(1,0),'R':(0,1),'L':(0,-1)}

def move(P,T):
  s=0
  for p in P:
    flag=1
    for t in T:
      p=(p[0]+map[t][0],p[1]+map[t][1])
      if S[p[0]][p[1]]=='#':
        flag=0
        break
    if flag==1:
      s+=1
  return s

ans=move(P,T)
print(ans)

######################################################################
