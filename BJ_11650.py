n = int(input())
arr =[]
for _ in range(n):
    arr.append(list(map(int,input().split())))
arr.sort(key=lambda x : (x[0], x[1]))
for num in arr:
    print(num[0], num[1])