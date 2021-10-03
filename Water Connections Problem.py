n = 0
p = 0

rd = [0]*1100
wt = [0]*1100

cd = [0]*1100
a = []
b = []
c = []

ans = 0

def dfs(w):
	global ans
	if (cd[w] == 0):
		return w
	if (wt[w] < ans):
		ans = wt[w]
	return dfs(cd[w])

def solve(arr):
	global ans
	i = 0
	while (i < p):
		q = arr[i][0]
		h = arr[i][1]
		t = arr[i][2]
		
		cd[q] = h
		wt[q] = t
		rd[h] = q
		i += 1
	a = []
	b = []
	c = []
	for j in range(1, n + 1):
		if (rd[j] == 0 and cd[j]):
			
			ans = 1000000000
			w = dfs(j)
			a.append(j)
			b.append(w)
			c.append(ans)
	print(len(a))
	for j in range(len(a)):
		print(a[j], b[j], c[j])

n = 9
p = 6

arr = [[7, 4, 98], [5, 9, 72], [4, 6, 10 ],
		[2, 8, 22 ], [9, 7, 17], [3, 1, 66]]

solve(arr)
