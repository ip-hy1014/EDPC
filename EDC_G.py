# トポロジカルソート
# EDPC_G
import sys
sys.setrecursionlimit(10**6)
n,m = map(int,input().split())
# edges[i]:頂点iから伸びている頂点たち（隣接リスト）
edges = []
for _ in range(n):
  edges.append([])
# 頂点に入ってくる辺の数（入次数）。始点の判定に使う
indeg = [0]*n
# 辺の入力を受け取り、隣接リストを作る
for _ in range(m):
  x,y = list(map(int,input().split()))
  edges[x-1].append(y-1)
  indeg[y-1] += 1
# length[i]:頂点iから始まるパスの最大長
length = [0] * n
# done[i]:既に計算済みであることを示すフラグ
done = [False] * n
# メモ化再帰の実装
def rec(i):
  # 計算済みであれば即座に値を返す
  if done[i]:
    return length[i]
  # そうでなければ値を計算する
  length[i] = 0
  for j in edges[i]:
    length[i] = max(length[i],rec(j)+1)
  # 計算済みフラグを立てて値を返す
  done[i] = True
  return length[i]
# 始点全てについてrecを呼び出す
for i in range(n):
  if indeg[i] == 0:
    rec(i)
print(max(length))