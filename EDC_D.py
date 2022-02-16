n,W = list(map(int,input().split()))
# 1始まりにするために先頭にダミーを入れる
ws = [0]
vs = [0]
for i in range(n):
  w,v = list(map(int,input().split()))
  ws.append(w)
  vs.append(v)
# value[i][w]:品物iまで見て重さ合計wである時の価値の総和の最大値
# 非常に小さい値で初期化しておく
value = []
for i in range(n+1):
  value.append([-10**18]*(W+1))
# 初期条件
value[0][0] = 0
# iが小さい順に求めていく
for i in range(1,n+1):
  for w in range(W+1):
    # 品物iを使わない場合
    value[i][w] = max(value[i][w],value[i-1][w])
    # 品物iを使う場合
    if w-ws[i]>=0:
      value[i][w] = max(value[i][w],value[i-1][w-ws[i]]+vs[i])
ans = max(value[n])
print(ans)